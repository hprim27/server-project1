// Music notes animation for the main portfolio
function initMusicNotesAnimation() {
    const heroVisual = document.querySelector('.hero-visual');
    if (!heroVisual) return;
    
    const musicNotesContainer = document.createElement('div');
    musicNotesContainer.className = 'music-notes-container';
    
    const notes = ['♪', '♫', '♬', '♩', '♪', '♫'];
    
    notes.forEach((note, index) => {
        const musicNote = document.createElement('div');
        musicNote.className = 'music-note';
        musicNote.textContent = note;
        musicNote.style.animationDelay = `${index * 0.01}s`;
        
        // Position each note horizontally across the screen
        const screenWidth = window.innerWidth;
        const noteWidth = 60; // Approximate width of each note
        const spacing = (screenWidth - noteWidth) / (notes.length - 1);
        const xPos = index * spacing;
        
        musicNote.style.left = `${xPos}px`;
        
        musicNotesContainer.appendChild(musicNote);
    });
    
    heroVisual.appendChild(musicNotesContainer);
    
    // Remove the container after animation completes
    setTimeout(() => {
        if (musicNotesContainer.parentNode) {
            musicNotesContainer.remove();
        }
    }, 6000);
}

// Initialize everything when the page loads
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎵 Harrison Prim Portfolio loaded with musical inspiration! 🎵');
    
    // Only call the functions that exist
    initMusicNotesAnimation();
});
