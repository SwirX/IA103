// Configuration - modify these paths according to your repo structure
const PODCASTS_PATH = 'podcasts/';
const EXERCISES_PATH = '';

let currentSection = 'podcasts';
let currentAudio = null;
let currentPodcastData = {};
let currentPdfDoc = null;
let currentPageNum = 1;
let currentFilePath = '';

// PDF.js configuration
pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

function showSection(section) {
    document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
    event.target.closest('.nav-btn').classList.add('active');
    document.querySelectorAll('.content-section').forEach(sec => sec.classList.remove('active'));
    document.getElementById(section).classList.add('active');
    currentSection = section;

    if (section === 'podcasts' && !document.getElementById('podcasts').querySelector('.podcast-list')) {
        loadPodcasts();
    } else if (section === 'files' && !document.getElementById('files').querySelector('.file-tree')) {
        loadFiles();
    }

    closePodcastModal();
    closeViewer();
}

const PODCAST_FILES = [
    { name: 'm101.mp3', title: 'Module 101' },
    { name: 'm102ch1-3.mp3', title: 'Module 102 Chapitre 1-3' },
    { name: 'm103ch1-2.mp3', title: 'Module 103 Chapitre 1-2' },
];

function loadPodcasts() {
    const podcastsContainer = document.getElementById('podcasts');
    
    if (PODCAST_FILES.length === 0) {
        podcastsContainer.innerHTML = '<p style="text-align: center; color: #666;">No podcast files found.</p>';
        return;
    }

    const listHTML = PODCAST_FILES.map((file) => {
        const fileExtension = file.name.split('.').pop().toUpperCase();
        return `
            <div class="podcast-item" onclick="openPodcastModal('${file.name}', '${file.title}', '${fileExtension}')">
                <div class="podcast-icon">
                    <i class="fas fa-podcast"></i>
                </div>
                <div class="podcast-info">
                    <div class="podcast-title">${file.title}</div>
                    <div class="podcast-meta">
                        <span><i class="fas fa-file-audio"></i> ${fileExtension}</span>
                        <span><i class="fas fa-clock"></i> Click to play</span>
                    </div>
                </div>
                <button class="play-button" onclick="event.stopPropagation(); openPodcastModal('${file.name}', '${file.title}', '${fileExtension}')">
                    <i class="fas fa-play"></i>
                </button>
            </div>
        `;
    }).join('');

    podcastsContainer.innerHTML = `
        <div class="podcast-list">
            <h2 style="margin-bottom: 20px; color: #333;">
                <i class="fas fa-podcast"></i> Available Podcasts
            </h2>
            ${listHTML}
        </div>
    `;
}

const EXERCISE_STRUCTURE = [
    {
        class: 'Classe 14 (Aberahman Salhi)',
        exercises: [
            {
                name: 'TD1',
                files: [
                    { name: 'Answers', path: 'c14/TD/1/answers/answers.md', isAnswer: true },
                    { name: 'PDF', path: 'c14/TD/1/original/Confluence.pdf', isAnswer: false }
                ]
            },
            {
                name: 'TD2',
                files: [
                    { name: 'PDF', path: 'c14/TD/2/original/algorithme.pdf', isAnswer: false },
                    { name: 'Answers', path: 'c14/TD/2/answers/answers.md', isAnswer: true }
                ]
            },
            {
                name: 'TD4',
                files: [
                    { name: 'PDF', path: 'c14/TD/4/original/Confluence.pdf', isAnswer: false },
                    { name: 'Answers', path: 'c14/TD/4/answers/answers.md', isAnswer: true }
                ]
            }
        ]
    },
    {
        class: 'Classe 12 (Abdelkarim Kherimiche)',
        exercises: [
            {
                name: 'TD1',
                files: [
                    { name: 'PDF', path: 'c12/TD/1/original/original.pdf', isAnswer: false },
                    { name: 'Answers', path: 'c12/TD/1/answers/answers.md', isAnswer: true }
                ]
            },
            {
                name: 'TD2',
                files: [
                    { name: 'PDF', path: 'c12/TD/2/original/original.pdf', isAnswer: false },
                    { name: 'Answers', path: 'c12/TD/2/answers/answers.md', isAnswer: true }
                ]
            },
            {
                name: 'TD2-p2',
                files: [
                    { name: 'PDF', path: 'c12/TD/2-v2/original/original.pdf', isAnswer: false },
                    { name: 'Questions', path: 'c12/TD/2-v2/original/questions.png', isAnswer: false },
                    { name: 'Answers', path: 'c12/TD/2-v2/answers/answers.md', isAnswer: true }
                ]
            },
            {
                name: 'TD3',
                files: [
                    { name: 'Enonce', path: 'c12/TD/3/original/Ex3-enonce.jpg', isAnswer: false },
                    { name: 'Questions', path: 'c12/TD/3/original/Ex3-questions.jpg', isAnswer: false },
                    { name: 'Answers', path: 'c12/TD/3/answers/answers.md', isAnswer: true }
                ]
            },
            {
                name: 'TD4',
                files: [
                    { name: 'Exercice', path: 'c12/TD/4/original/Ex4-enonce.jpg', isAnswer: false },
                    { name: 'Exercice', path: 'c12/TD/4/original/Ex4-questions.jpg', isAnswer: false },
                    { name: 'Answers', path: 'c12/TD/4/answers/answers.md', isAnswer: true }
                ]
            },
            {
                name: 'TD5',
                files: [
                    { name: 'Exercice', path: 'c12/TD/5/original/LDD.pdf', isAnswer: false },
                    { name: 'EX2', path: 'c12/TD/5/answers/ex2.sql', isAnswer: true },
                    { name: 'EX3', path: 'c12/TD/5/answers/ex3.sql', isAnswer: true }
                ]
            }
        ]
    }
];

function loadFiles() {
    const filesContainer = document.getElementById('files');
    
    if (EXERCISE_STRUCTURE.length === 0) {
        filesContainer.innerHTML = '<p style="text-align: center; color: #666;">No exercise files found.</p>';
        return;
    }

    let foldersHTML = '';
    
    EXERCISE_STRUCTURE.forEach(classItem => {
        let exerciseHTML = '';
        let totalFiles = 0;
        
        classItem.exercises.forEach(exercise => {
            if (exercise && exercise.files && exercise.files.length > 0) {
                totalFiles += exercise.files.length;
                exerciseHTML += `
                    <div class="folder" style="margin-left: 20px; margin-bottom: 10px;">
                        <div class="folder-header" onclick="toggleFolder(this)" style="background: #f1f3f4;">
                            <i class="fas fa-chevron-right folder-icon"></i>
                            <i class="fas fa-clipboard-list"></i>
                            <span>${exercise.name}</span>
                            <span style="margin-left: auto; font-size: 0.8rem; color: #666;">${exercise.files.length} files</span>
                        </div>
                        <div class="folder-content">
                            ${exercise.files.map(file => `
                                <div class="file-item" onclick="viewFile('${file.path}', '${file.name}')">
                                    <i class="fas ${getFileIcon(file.path)}" style="color: ${file.isAnswer ? '#28a745' : '#6c757d'};"></i>
                                    <span>${file.isAnswer ? '📝 ' : ''}${file.name}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
            }
        });
        
        if (totalFiles > 0) {
            foldersHTML += `
                <div class="folder">
                    <div class="folder-header" onclick="toggleFolder(this)">
                        <i class="fas fa-chevron-right folder-icon"></i>
                        <i class="fas fa-graduation-cap"></i>
                        <span>${classItem.class.toUpperCase()} - TD Exercises</span>
                        <span style="margin-left: auto; font-size: 0.8rem; color: #666;">${totalFiles} files</span>
                    </div>
                    <div class="folder-content">
                        ${exerciseHTML}
                    </div>
                </div>
            `;
        }
    });

    filesContainer.innerHTML = `
        <div class="file-tree">
            <h2 style="margin-bottom: 20px; color: #333;"><i class="fas fa-folder-open"></i> Exercise Files</h2>
            ${foldersHTML}
        </div>
    `;
}

function getFileIcon(path) {
    const ext = path.split('.').pop().toLowerCase();
    if (ext === 'pdf') return 'fa-file-pdf';
    if (['jpg', 'jpeg', 'png', 'gif', 'svg'].includes(ext)) return 'fa-file-image';
    if (ext === 'md') return 'fa-file-alt';
    return 'fa-file';
}

function toggleFolder(header) {
    header.parentElement.classList.toggle('open');
}

async function openPodcastModal(fileName, displayName, fileExtension) {
    const modal = document.getElementById('podcast-modal');
    const audio = document.getElementById('modal-audio');
    const audioUrl = `${PODCASTS_PATH}${fileName}`;
    const transcriptUrl = `${PODCASTS_PATH}${fileName.replace(/\.[^/.]+$/, '')}.json`;
    
    document.getElementById('modal-podcast-title').textContent = displayName;
    document.getElementById('modal-podcast-meta').innerHTML = `
        <span><i class="fas fa-file-audio"></i> ${fileExtension}</span>
        <span><i class="fas fa-clock"></i> Loading...</span>
    `;
    document.getElementById('modal-download').onclick = () => {
        const a = document.createElement('a');
        a.href = audioUrl;
        a.download = fileName;
        a.click();
    };
    
    audio.src = audioUrl;
    currentAudio = audio;
    
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    document.title = `${displayName} - IA103 Podcasts`;
    
    await loadTranscript(transcriptUrl, displayName);
    setupAudioPlayer();
    
    audio.addEventListener('loadedmetadata', () => {
        const duration = formatTime(audio.duration);
        document.getElementById('modal-podcast-meta').innerHTML = `
            <span><i class="fas fa-file-audio"></i> ${fileExtension}</span>
            <span><i class="fas fa-clock"></i> ${duration}</span>
        `;
    });
}

async function loadTranscript(transcriptUrl, podcastName) {
    const container = document.getElementById('transcript-text');
    
    try {
        const response = await fetch(transcriptUrl);
        if (!response.ok) {
            container.innerHTML = '<p style="text-align: center; color: #666;">No transcript available for this podcast.</p>';
            return;
        }
        
        const transcriptData = await response.json();
        currentPodcastData = transcriptData;
        
        document.getElementById('stat-language').textContent = 
            `${transcriptData.language_code || 'Unknown'} (${(transcriptData.language_probability * 100 || 0).toFixed(1)}%)`;
        document.getElementById('stat-confidence').textContent = 
            `${(transcriptData.language_probability * 100 || 0).toFixed(1)}%`;
        document.getElementById('stat-id').textContent = 
            transcriptData.transcription_id || 'N/A';
        
        renderTranscript(transcriptData.words || []);
    } catch (error) {
        console.error('Error loading transcript:', error);
        container.innerHTML = '<p style="text-align: center; color: #e74c3c;">Error loading transcript.</p>';
    }
}

function renderTranscript(words) {
    const container = document.getElementById('transcript-text');
    
    if (!words || words.length === 0) {
        container.innerHTML = '<p style="text-align: center; color: #666;">No transcript data available.</p>';
        return;
    }
    
    const speakers = {};
    let currentSpeaker = null;
    let currentSegment = [];
    
    words.forEach((word) => {
        if (word.type === 'spacing') {
            if (currentSegment.length > 0) {
                currentSegment.push(word);
            }
            return;
        }
        
        if (word.speaker_id !== currentSpeaker) {
            if (currentSpeaker !== null && currentSegment.length > 0) {
                if (!speakers[currentSpeaker]) speakers[currentSpeaker] = [];
                speakers[currentSpeaker].push([...currentSegment]);
            }
            currentSpeaker = word.speaker_id;
            currentSegment = [word];
        } else {
            currentSegment.push(word);
        }
    });
    
    if (currentSpeaker !== null && currentSegment.length > 0) {
        if (!speakers[currentSpeaker]) speakers[currentSpeaker] = [];
        speakers[currentSpeaker].push([...currentSegment]);
    }
    
    const allSegments = [];
    Object.keys(speakers).forEach(speakerId => {
        speakers[speakerId].forEach(segment => {
            allSegments.push({ speakerId, segment });
        });
    });
    
    allSegments.sort((a, b) => {
        const aFirstWord = a.segment.find(w => w.type === 'word');
        const bFirstWord = b.segment.find(w => w.type === 'word');
        return (aFirstWord?.start || 0) - (bFirstWord?.start || 0);
    });
    
    const segmentsHTML = allSegments.map(({ speakerId, segment }) => {
        const speakerNum = speakerId.replace('speaker_', '');
        const speakerClass = `speaker-${parseInt(speakerNum) % 2}`;
        
        const wordsHTML = segment.map((word) => {
            if (word.type === 'spacing') {
                return word.text || ' ';
            } else {
                return `<span class="transcript-word" data-start="${word.start}" data-end="${word.end}" onclick="seekToTime(${word.start})">${word.text}</span>`;
            }
        }).join('');
        
        return `
            <div class="speaker-segment ${speakerClass}">
                <div class="speaker-header">
                    <span class="speaker-icon">${parseInt(speakerNum) + 1}</span>
                    Speaker ${parseInt(speakerNum) + 1}
                </div>
                <div class="speaker-content">
                    ${wordsHTML}
                </div>
            </div>
        `;
    }).join('');
    
    container.innerHTML = segmentsHTML;
}

function setupAudioPlayer() {
    if (!currentAudio) return;
    
    currentAudio.addEventListener('timeupdate', () => {
        updateTranscriptHighlight(currentAudio.currentTime);
    });
}

function updateTranscriptHighlight(currentTime) {
    const words = document.querySelectorAll('.transcript-word');
    
    words.forEach(word => {
        const start = parseFloat(word.dataset.start);
        const end = parseFloat(word.dataset.end);
        
        word.classList.remove('active', 'played');
        
        if (currentTime >= start && currentTime <= end) {
            word.classList.add('active');
            word.scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
        } else if (currentTime > end) {
            word.classList.add('played');
        }
    });
}

function seekToTime(time) {
    if (currentAudio) {
        currentAudio.currentTime = time;
        if (currentAudio.paused) {
            currentAudio.play();
        }
    }
}

function toggleStats() {
    const stats = document.getElementById('transcript-stats');
    const button = document.getElementById('stats-toggle');
    
    if (stats.classList.contains('active')) {
        stats.classList.remove('active');
        button.innerHTML = '<i class="fas fa-chart-bar"></i> Stats';
    } else {
        stats.classList.add('active');
        button.innerHTML = '<i class="fas fa-eye-slash"></i> Hide';
    }
}

function closePodcastModal() {
    const modal = document.getElementById('podcast-modal');
    modal.classList.remove('active');
    document.body.style.overflow = '';
    
    if (currentAudio) {
        currentAudio.pause();
        currentAudio.currentTime = 0;
    }
    
    const stats = document.getElementById('transcript-stats');
    const button = document.getElementById('stats-toggle');
    stats.classList.remove('active');
    button.innerHTML = '<i class="fas fa-chart-bar"></i> Stats';
}

function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
}

async function viewFile(filePath, fileName) {
    currentFilePath = `${EXERCISES_PATH}${filePath}`;
    const ext = filePath.split('.').pop().toLowerCase();
    
    document.getElementById('viewer-title').textContent = fileName;
    const viewerContent = document.getElementById('viewer-content');
    const downloadBtn = document.getElementById('download-btn');
    
    downloadBtn.style.display = 'flex';
    downloadBtn.onclick = () => {
        const a = document.createElement('a');
        a.href = currentFilePath;
        a.download = fileName;
        a.click();
    };
    
    viewerContent.innerHTML = '<div class="loading"><div class="spinner"></div><p>Loading file...</p></div>';
    
    try {
        if (ext === 'pdf') {
            await renderPDF(currentFilePath);
        } else if (['jpg', 'jpeg', 'png', 'gif', 'svg'].includes(ext)) {
            renderImage(currentFilePath, fileName);
        } else if (ext === 'md') {
            await renderMarkdown(currentFilePath);
        } else {
            const response = await fetch(currentFilePath);
            const content = await response.text();
            viewerContent.innerHTML = `<pre style="white-space: pre-wrap; font-family: inherit; background: white; padding: 20px; border-radius: 10px;">${content}</pre>`;
        }
        
        document.getElementById('file-viewer').classList.add('active');
        document.body.style.overflow = 'hidden';
    } catch (error) {
        console.error('Error loading file:', error);
        viewerContent.innerHTML = '<p style="text-align: center; color: #e74c3c; padding: 40px;">Error loading file. Please check if the file exists.</p>';
    }
}

async function renderPDF(url) {
    const viewerContent = document.getElementById('viewer-content');
    viewerContent.innerHTML = `
        <div class="pdf-container">
            <div class="pdf-controls">
                <button onclick="changePDFPage(-1)" id="pdf-prev">Previous</button>
                <span><span id="pdf-page-num">1</span> / <span id="pdf-page-count">-</span></span>
                <button onclick="changePDFPage(1)" id="pdf-next">Next</button>
            </div>
            <canvas id="pdf-canvas"></canvas>
        </div>
    `;
    
    const loadingTask = pdfjsLib.getDocument(url);
    currentPdfDoc = await loadingTask.promise;
    document.getElementById('pdf-page-count').textContent = currentPdfDoc.numPages;
    currentPageNum = 1;
    renderPDFPage(currentPageNum);
}

async function renderPDFPage(num) {
    const page = await currentPdfDoc.getPage(num);
    const canvas = document.getElementById('pdf-canvas');
    const ctx = canvas.getContext('2d');
    
    const viewport = page.getViewport({ scale: 1.5 });
    canvas.height = viewport.height;
    canvas.width = viewport.width;
    
    await page.render({
        canvasContext: ctx,
        viewport: viewport
    }).promise;
    
    document.getElementById('pdf-page-num').textContent = num;
    document.getElementById('pdf-prev').disabled = num <= 1;
    document.getElementById('pdf-next').disabled = num >= currentPdfDoc.numPages;
}

function changePDFPage(delta) {
    currentPageNum += delta;
    renderPDFPage(currentPageNum);
}

function renderImage(url, alt) {
    const viewerContent = document.getElementById('viewer-content');
    viewerContent.innerHTML = `
        <div class="image-container">
            <img src="${url}" alt="${alt}" />
        </div>
    `;
}

async function renderMarkdown(url) {
    const response = await fetch(url);
    const content = await response.text();
    const viewerContent = document.getElementById('viewer-content');
    
    // Get the base path of the markdown file
    const basePath = url.substring(0, url.lastIndexOf('/') + 1);
    
    marked.setOptions({
        breaks: true,
        gfm: true
    });
    
    const htmlContent = marked.parse(content);
    viewerContent.innerHTML = `<div class="markdown-content">${htmlContent}</div>`;
    
    // Fix relative image paths
    const images = viewerContent.querySelectorAll('.markdown-content img');
    images.forEach(img => {
        const src = img.getAttribute('src');
        // Only fix relative paths (not absolute URLs or data URIs)
        if (src && !src.startsWith('http://') && !src.startsWith('https://') && !src.startsWith('data:') && !src.startsWith('/')) {
            img.setAttribute('src', basePath + src);
        }
    });
    
    mermaid.initialize({ 
        startOnLoad: false,
        theme: 'default',
        securityLevel: 'loose',
        fontFamily: 'Segoe UI, sans-serif',
        er: {
            useMaxWidth: true
        }
    });
    
    const mermaidBlocks = viewerContent.querySelectorAll('pre code.language-mermaid');
    
    for (let i = 0; i < mermaidBlocks.length; i++) {
        const block = mermaidBlocks[i];
        const mermaidCode = block.textContent;
        const pre = block.parentElement;
        
        const mermaidDiv = document.createElement('div');
        mermaidDiv.className = 'mermaid-diagram';
        const uniqueId = `mermaid-${Date.now()}-${i}`;
        mermaidDiv.id = uniqueId;
        
        pre.replaceWith(mermaidDiv);
        
        try {
            const { svg } = await mermaid.render(uniqueId + '-svg', mermaidCode);
            mermaidDiv.innerHTML = svg;
        } catch (error) {
            console.error('Mermaid rendering error:', error);
            mermaidDiv.innerHTML = `<pre style="color: #e74c3c; background: #fee; padding: 15px; border-radius: 8px;">Error rendering diagram: ${error.message}\n\nDiagram code:\n${mermaidCode}</pre>`;
        }
    }
}

function closeViewer() {
    document.getElementById('file-viewer').classList.remove('active');
    document.body.style.overflow = '';
    currentPdfDoc = null;
    currentPageNum = 1;
}

document.getElementById('podcast-modal').addEventListener('click', (e) => {
    if (e.target.classList.contains('modal-overlay')) {
        closePodcastModal();
    }
});

document.getElementById('file-viewer').addEventListener('click', (e) => {
    if (e.target.classList.contains('file-viewer')) {
        closeViewer();
    }
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        if (document.getElementById('podcast-modal').classList.contains('active')) {
            closePodcastModal();
        } else if (document.getElementById('file-viewer').classList.contains('active')) {
            closeViewer();
        }
    }
});

document.addEventListener('DOMContentLoaded', function() {
    loadPodcasts();
});