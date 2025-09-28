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
    """Save transcript as .json, .srt, and .txt."""
    # JSON
    json_path = audio_path.with_suffix(".json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(transcript, f, ensure_ascii=False, indent=2)

    # TXT
    txt_path = audio_path.with_suffix(".txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(transcript.get("text", ""))

    # SRT
    srt_path = audio_path.with_suffix(".srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(transcript.get("segments", []), start=1):
            start = seg["start"]
            end = seg["end"]
            text = seg["text"].strip()

            def fmt(t):
                ms = int((t - int(t)) * 1000)
                s = int(t) % 60
                m = (int(t) // 60) % 60
                h = int(t) // 3600
                return f"{h:02}:{m:02}:{s:02},{ms:03}"

            f.write(f"{i}\n{fmt(start)} --> {fmt(end)}\n{text}\n\n")

    print(f"Saved: {json_path}, {txt_path}, {srt_path}")

def transcribe(audio_path: Path):
    cache = cache_path(audio_path)
    if cache.exists():
        print("Using cached transcript.")
        with open(cache, "r", encoding="utf-8") as f:
            return json.load(f)

    headers = {"xi-api-key": API_KEY}
    files = {"file": open(audio_path, "rb")}
    data = {"model_id": MODEL}

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
