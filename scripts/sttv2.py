import sys
import json
import hashlib
import requests
import dotenv
from pathlib import Path

dotenv.load_dotenv()

# --- CONFIG ---
API_KEY = dotenv.get_key(dotenv.find_dotenv(), "EL_STT")
if not API_KEY:
    print("Error: EL_STT not found in .env")
    sys.exit(1)

API_URL = "https://api.elevenlabs.io/v1/speech-to-text"
MODEL = "scribe_v1"


def cache_path(audio_path: Path) -> Path:
    """Return path to cached JSON based on audio hash."""
    h = hashlib.sha1(audio_path.read_bytes()).hexdigest()[:16]
    return audio_path.with_suffix(f".{h}.json")


def save_outputs(audio_path: Path, transcript: dict):
    """Save transcript as .json and .txt (with speaker separation)."""
    # JSON
    json_path = audio_path.with_suffix(".json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(transcript, f, ensure_ascii=False, indent=2)

    print(f"Saved: {json_path}, {txt_path}")


def transcribe(audio_path: Path):
    cache = cache_path(audio_path)
    if cache.exists():
        print("Using cached transcript.")
        with open(cache, "r", encoding="utf-8") as f:
            return json.load(f)

    headers = {"xi-api-key": API_KEY}
    files = {"file": open(audio_path, "rb")}
    data = {"model_id": MODEL, "diarize": "true"}

    r = requests.post(API_URL, headers=headers, files=files, data=data)
    if r.status_code != 200:
        print("Error:", r.status_code, r.text)
        sys.exit(1)

    transcript = r.json()
    with open(cache, "w", encoding="utf-8") as f:
        json.dump(transcript, f, ensure_ascii=False, indent=2)

    return transcript


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python stt.py path/to/audio.mp3")
        sys.exit(1)

    audio_path = Path(sys.argv[1])
    transcript = transcribe(audio_path)
    save_outputs(audio_path, transcript)
