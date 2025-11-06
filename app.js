// Configuration
const PODCASTS_PATH = 'podcasts/';
const EXERCISES_PATH = '';

// State Management
const state = {
    currentSection: 'classes',
    currentAudio: null,
    currentPodcastData: {},
    currentPdfDoc: null,
    currentPageNum: 1,
    currentFilePath: '',
    selectedClass: null
};

// PDF.js Configuration
if (typeof pdfjsLib !== 'undefined') {
    pdfjsLib.GlobalWorkerOptions.workerSrc = 
        'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
}

// Data
const PODCAST_FILES = [
    { name: 'm101.mp3', title: 'Module 101' },
    { name: 'm102ch1-3.mp3', title: 'Module 102 Chapitre 1-3' },
    { name: 'm103ch1-2.mp3', title: 'Module 103 Chapitre 1-2' },
];

const EXERCISE_STRUCTURE = [
    {
        id: 'c14',
        class: 'Classe 14',
        instructor: 'Abderahman Salhi',
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
            },
            {
                name: 'TD5',
                files: [
                    { name: 'PDF', path: 'c14/TD/5/original/output.pdf', isAnswer: false },
                    { name: 'Answers', path: 'c14/TD/5/answers/answers.md', isAnswer: true }
                ]
            },
            {
                name: 'TD6',
                files: [
                    { name: 'PDF', path: 'c14/TD/6/original/tableaux.pdf', isAnswer: false },
                    { name: 'Answers', path: 'c14/TD/6/answers/answers.md', isAnswer: true }
                ]
            }
        ]
    },
    {
        id: 'c12',
        class: 'Classe 12',
        instructor: 'Abdelkarim Kherimiche',
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
                    { name: 'Enonce', path: 'c12/TD/4/original/Ex4-enonce.jpg', isAnswer: false },
                    { name: 'Exercice', path: 'c12/TD/4/original/Ex4-questions.jpg', isAnswer: false },
                    { name: 'Answers', path: 'c12/TD/4/answers/answers.md', isAnswer: true }
                ]
            },
            {
                name: 'TD5',
                files: [
                    { name: 'PDF', path: 'c12/TD/5/original/LDD.pdf', isAnswer: false },
                    { name: 'EX2', path: 'c12/TD/5/answers/ex2.md', isAnswer: true },
                    { name: 'EX3', path: 'c12/TD/5/answers/ex3.md', isAnswer: true }
                ]
            }
        ]
    }
];

// Utility Functions
function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
}

function getFileIcon(path) {
    const ext = path.split('.').pop().toLowerCase();
    if (ext === 'pdf') return 'fa-file-pdf';
    if (['jpg', 'jpeg', 'png', 'gif', 'svg'].includes(ext)) return 'fa-file-image';
    if (ext === 'md') return 'fa-file-alt';
    return 'fa-file';
}

// Custom Modal
class Modal {
    constructor() {
        this.overlay = document.getElementById('customModal');
        this.title = document.getElementById('modalTitle');
        this.body = document.getElementById('modalBody');
        this.actions = document.getElementById('modalActions');
        this.closeBtn = this.overlay.querySelector('.modal-close');
        
        this.closeBtn.addEventListener('click', () => this.close());
        this.overlay.addEventListener('click', (e) => {
            if (e.target === this.overlay) this.close();
        });
    }

    show(title, content, buttons = []) {
        this.title.textContent = title;
        this.body.innerHTML = content;
        
        this.actions.innerHTML = buttons.map(btn => `
            <button class="btn ${btn.primary ? 'btn-primary' : 'btn-secondary'}" 
                    data-action="${btn.action}">
                ${btn.text}
            </button>
        `).join('');
        
        this.actions.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                const button = buttons.find(b => b.action === action);
                if (button && button.callback) button.callback();
                this.close();
            });
        });
        
        this.overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    close() {
        this.overlay.classList.remove('active');
        document.body.style.overflow = '';
    }
}

const modal = new Modal();

// Navigation
function initNavigation() {
    const navItems = document.querySelectorAll('.nav-item:not([href])');
    
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const section = item.dataset.section;
            showSection(section);
        });
    });
}

function showSection(sectionName) {
    state.currentSection = sectionName;
    
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.toggle('active', item.dataset.section === sectionName);
    });
    
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.toggle('active', section.id === sectionName);
    });
    
    if (sectionName === 'podcasts' && !document.querySelector('.podcast-container').hasChildNodes()) {
        loadPodcasts();
    }
}

// Class Selection
function initClassSelection() {
    const classCards = document.querySelectorAll('.class-card');
    
    classCards.forEach(card => {
        card.addEventListener('click', () => {
            const classId = card.dataset.class;
            selectClass(classId);
        });
    });
}

function selectClass(classId) {
    state.selectedClass = classId;
    const classData = EXERCISE_STRUCTURE.find(c => c.id === classId);
    
    if (!classData) return;
    
    showSection('exercises');
    loadExercises(classData);
}

// Podcasts
function loadPodcasts() {
    const container = document.querySelector('.podcast-container');
    
    if (PODCAST_FILES.length === 0) {
        container.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">No podcasts available.</p>';
        return;
    }
    
    container.innerHTML = PODCAST_FILES.map(podcast => `
        <div class="podcast-item" data-file="${podcast.name}">
            <div class="podcast-icon">
                <i class="fas fa-podcast"></i>
            </div>
            <div class="podcast-info">
                <div class="podcast-title">${podcast.title}</div>
                <div class="podcast-meta">
                    <span><i class="fas fa-file-audio"></i> MP3</span>
                    <span><i class="fas fa-clock"></i> Click to play</span>
                </div>
            </div>
            <button class="play-btn">
                <i class="fas fa-play"></i>
            </button>
        </div>
    `).join('');
    
    container.querySelectorAll('.podcast-item').forEach(item => {
        item.addEventListener('click', () => {
            const fileName = item.dataset.file;
            const podcast = PODCAST_FILES.find(p => p.name === fileName);
            openPodcastPlayer(fileName, podcast.title);
        });
    });
}

// Podcast Player
async function openPodcastPlayer(fileName, title) {
    const modal = document.getElementById('playerModal');
    const audio = document.getElementById('audioPlayer');
    const audioUrl = `${PODCASTS_PATH}${fileName}`;
    const transcriptUrl = `${PODCASTS_PATH}${fileName.replace(/\.[^/.]+$/, '')}.json`;
    
    document.getElementById('playerTitle').textContent = title;
    document.getElementById('playerMeta').textContent = 'Loading...';
    
    audio.src = audioUrl;
    state.currentAudio = audio;
    
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    
    setupAudioControls();
    await loadTranscript(transcriptUrl);
    
    audio.addEventListener('loadedmetadata', () => {
        document.getElementById('playerMeta').textContent = 
            `Duration: ${formatTime(audio.duration)}`;
    });
}

function setupAudioControls() {
    const audio = state.currentAudio;
    const playPauseBtn = document.getElementById('playPause');
    const downloadBtn = document.getElementById('downloadAudio');
    const progressTrack = document.querySelector('.progress-track');
    const progressFill = document.querySelector('.progress-fill');
    const currentTimeEl = document.getElementById('currentTime');
    const durationEl = document.getElementById('duration');
    
    playPauseBtn.addEventListener('click', () => {
        if (audio.paused) {
            audio.play();
            playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
        } else {
            audio.pause();
            playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
        }
    });
    
    downloadBtn.addEventListener('click', () => {
        const a = document.createElement('a');
        a.href = audio.src;
        a.download = audio.src.split('/').pop();
        a.click();
    });
    
    audio.addEventListener('timeupdate', () => {
        const progress = (audio.currentTime / audio.duration) * 100;
        progressFill.style.width = `${progress}%`;
        currentTimeEl.textContent = formatTime(audio.currentTime);
        updateTranscriptHighlight(audio.currentTime);
    });
    
    audio.addEventListener('loadedmetadata', () => {
        durationEl.textContent = formatTime(audio.duration);
    });
    
    progressTrack.addEventListener('click', (e) => {
        const rect = progressTrack.getBoundingClientRect();
        const pos = (e.clientX - rect.left) / rect.width;
        audio.currentTime = pos * audio.duration;
    });
}

async function loadTranscript(transcriptUrl) {
    const container = document.getElementById('transcriptContent');
    
    try {
        const response = await fetch(transcriptUrl);
        if (!response.ok) {
            container.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">No transcript available.</p>';
            return;
        }
        
        const data = await response.json();
        state.currentPodcastData = data;
        
        document.getElementById('statLanguage').textContent = 
            `${data.language_code || 'Unknown'} (${(data.language_probability * 100 || 0).toFixed(1)}%)`;
        document.getElementById('statConfidence').textContent = 
            `${(data.language_probability * 100 || 0).toFixed(1)}%`;
        
        renderTranscript(data.words || []);
    } catch (error) {
        console.error('Error loading transcript:', error);
        container.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Error loading transcript.</p>';
    }
}

function renderTranscript(words) {
    const container = document.getElementById('transcriptContent');
    
    if (!words || words.length === 0) {
        container.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">No transcript data available.</p>';
        return;
    }
    
    const speakers = {};
    let currentSpeaker = null;
    let currentSegment = [];
    
    words.forEach(word => {
        if (word.type === 'spacing') {
            if (currentSegment.length > 0) currentSegment.push(word);
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
    
    container.innerHTML = allSegments.map(({ speakerId, segment }) => {
        const speakerNum = speakerId.replace('speaker_', '');
        const wordsHTML = segment.map(word => {
            if (word.type === 'spacing') {
                return word.text || ' ';
            }
            return `<span class="transcript-word" data-start="${word.start}" data-end="${word.end}">${word.text}</span>`;
        }).join('');
        
        return `
            <div class="speaker-segment">
                <div class="speaker-header">
                    <span class="speaker-icon">${parseInt(speakerNum) + 1}</span>
                    Speaker ${parseInt(speakerNum) + 1}
                </div>
                <div class="speaker-content">${wordsHTML}</div>
            </div>
        `;
    }).join('');
    
    container.querySelectorAll('.transcript-word').forEach(word => {
        word.addEventListener('click', () => {
            const time = parseFloat(word.dataset.start);
            if (state.currentAudio) {
                state.currentAudio.currentTime = time;
                if (state.currentAudio.paused) state.currentAudio.play();
            }
        });
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
            word.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else if (currentTime > end) {
            word.classList.add('played');
        }
    });
}

function closePodcastPlayer() {
    const modal = document.getElementById('playerModal');
    modal.classList.remove('active');
    document.body.style.overflow = '';
    
    if (state.currentAudio) {
        state.currentAudio.pause();
        state.currentAudio.currentTime = 0;
    }
    
    const playPauseBtn = document.getElementById('playPause');
    playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
}

// Exercises
function loadExercises(classData) {
    const container = document.querySelector('.exercise-container');
    
    const totalFiles = classData.exercises.reduce((sum, ex) => sum + ex.files.length, 0);
    
    container.innerHTML = `
        <div class="exercise-group open">
            <div class="group-header">
                <div class="group-title">
                    <i class="fas fa-chevron-right chevron-icon"></i>
                    <i class="fas fa-graduation-cap"></i>
                    <h3>${classData.class} - ${classData.instructor}</h3>
                </div>
                <span class="group-count">${totalFiles} files</span>
            </div>
            <div class="group-content">
                ${classData.exercises.map(td => `
                    <div class="td-item">
                        <div class="td-header">
                            <div class="td-name">
                                <i class="fas fa-chevron-right chevron-icon"></i>
                                <span>${td.name}</span>
                            </div>
                            <span class="group-count">${td.files.length} files</span>
                        </div>
                        <div class="td-files">
                            ${td.files.map(file => `
                                <div class="file-link ${file.isAnswer ? 'answer' : ''}" 
                                     data-path="${file.path}">
                                    <i class="fas ${getFileIcon(file.path)}"></i>
                                    <span>${file.name}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
    
    container.querySelectorAll('.group-header').forEach(header => {
        header.addEventListener('click', () => {
            header.parentElement.classList.toggle('open');
        });
    });
    
    container.querySelectorAll('.td-header').forEach(header => {
        header.addEventListener('click', () => {
            header.parentElement.classList.toggle('open');
        });
    });
    
    container.querySelectorAll('.file-link').forEach(link => {
        link.addEventListener('click', () => {
            const path = link.dataset.path;
            const name = link.querySelector('span').textContent;
            viewFile(path, name);
        });
    });
}

// File Viewer
async function viewFile(filePath, fileName) {
    state.currentFilePath = `${EXERCISES_PATH}${filePath}`;
    const ext = filePath.split('.').pop().toLowerCase();
    
    document.getElementById('viewerTitle').textContent = fileName;
    const viewerContent = document.getElementById('viewerContent');
    const downloadBtn = document.getElementById('viewerDownload');
    
    downloadBtn.onclick = () => {
        const a = document.createElement('a');
        a.href = state.currentFilePath;
        a.download = fileName;
        a.click();
    };
    
    viewerContent.innerHTML = '<div class="loading-spinner"><div class="spinner"></div><p>Loading file...</p></div>';
    
    try {
        if (ext === 'pdf') {
            await renderPDF(state.currentFilePath);
        } else if (['jpg', 'jpeg', 'png', 'gif', 'svg'].includes(ext)) {
            renderImage(state.currentFilePath, fileName);
        } else if (ext === 'md') {
            await renderMarkdown(state.currentFilePath);
        } else {
            const response = await fetch(state.currentFilePath);
            const content = await response.text();
            viewerContent.innerHTML = `<pre style="white-space: pre-wrap; background: var(--surface-light); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">${content}</pre>`;
        }
        
        document.getElementById('viewerModal').classList.add('active');
        document.body.style.overflow = 'hidden';
    } catch (error) {
        console.error('Error loading file:', error);
        viewerContent.innerHTML = '<p style="text-align: center; color: var(--text-secondary); padding: 3rem;">Error loading file.</p>';
    }
}

async function renderPDF(url) {
    const viewerContent = document.getElementById('viewerContent');
    viewerContent.innerHTML = `
        <div class="pdf-container">
            <div class="pdf-controls">
                <button id="pdf-prev">Previous</button>
                <span><span id="pdf-page-num">1</span> / <span id="pdf-page-count">-</span></span>
                <button id="pdf-next">Next</button>
            </div>
            <canvas id="pdf-canvas"></canvas>
        </div>
    `;
    
    const loadingTask = pdfjsLib.getDocument(url);
    state.currentPdfDoc = await loadingTask.promise;
    document.getElementById('pdf-page-count').textContent = state.currentPdfDoc.numPages;
    state.currentPageNum = 1;
    await renderPDFPage(1);
    
    document.getElementById('pdf-prev').addEventListener('click', () => {
        if (state.currentPageNum > 1) {
            state.currentPageNum--;
            renderPDFPage(state.currentPageNum);
        }
    });
    
    document.getElementById('pdf-next').addEventListener('click', () => {
        if (state.currentPageNum < state.currentPdfDoc.numPages) {
            state.currentPageNum++;
            renderPDFPage(state.currentPageNum);
        }
    });
}

async function renderPDFPage(num) {
    const page = await state.currentPdfDoc.getPage(num);
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
    document.getElementById('pdf-next').disabled = num >= state.currentPdfDoc.numPages;
}

function renderImage(url, alt) {
    const viewerContent = document.getElementById('viewerContent');
    viewerContent.innerHTML = `
        <div class="image-container">
            <img src="${url}" alt="${alt}" />
        </div>
    `;
}

async function renderMarkdown(url) {
    const response = await fetch(url);
    const content = await response.text();
    const viewerContent = document.getElementById('viewerContent');
    const basePath = url.substring(0, url.lastIndexOf('/') + 1);
    
    marked.setOptions({
        breaks: true,
        gfm: true
    });
    
    const htmlContent = marked.parse(content);
    viewerContent.innerHTML = `<div class="markdown-content">${htmlContent}</div>`;
    
    const images = viewerContent.querySelectorAll('.markdown-content img');
    images.forEach(img => {
        const src = img.getAttribute('src');
        if (src && !src.startsWith('http://') && !src.startsWith('https://') && 
            !src.startsWith('data:') && !src.startsWith('/')) {
            img.setAttribute('src', basePath + src);
        }
    });
    
    if (typeof mermaid !== 'undefined') {
        mermaid.initialize({ 
            startOnLoad: false,
            theme: 'dark',
            securityLevel: 'loose'
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
                mermaidDiv.innerHTML = `<pre style="color: var(--error);">Error rendering diagram</pre>`;
            }
        }
    }
}

function closeViewer() {
    document.getElementById('viewerModal').classList.remove('active');
    document.body.style.overflow = '';
    state.currentPdfDoc = null;
    state.currentPageNum = 1;
}

// Event Listeners
document.getElementById('playerClose')?.addEventListener('click', closePodcastPlayer);
document.getElementById('viewerClose')?.addEventListener('click', closeViewer);

document.getElementById('statsToggle')?.addEventListener('click', () => {
    const stats = document.getElementById('transcriptStats');
    stats.classList.toggle('active');
});

document.getElementById('playerModal')?.addEventListener('click', (e) => {
    if (e.target.id === 'playerModal') closePodcastPlayer();
});

document.getElementById('viewerModal')?.addEventListener('click', (e) => {
    if (e.target.id === 'viewerModal') closeViewer();
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        if (document.getElementById('playerModal')?.classList.contains('active')) {
            closePodcastPlayer();
        } else if (document.getElementById('viewerModal')?.classList.contains('active')) {
            closeViewer();
        }
    }
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initClassSelection();
});