// js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // Function to show/hide forms based on selected radio buttons
    function toggleForms() {
        const mp3Form = document.getElementById('mp3-form');
        const mp4Form = document.getElementById('mp4-form');
        const playlistMp3Form = document.getElementById('playlist-mp3-form');
        const playlistMp4Form = document.getElementById('playlist-mp4-form');
        const channelMp3Form = document.getElementById('channel-mp3-form');
        const channelMp4Form = document.getElementById('channel-mp4-form');

        const mp3Btn = document.getElementById('mp3-btn');
        const mp4Btn = document.getElementById('mp4-btn');
        const singleBtn = document.getElementById('single-btn');
        const playlistBtn = document.getElementById('playlist-btn');
        const channelBtn = document.getElementById('channel-btn');

        mp3Form.classList.add('hidden');
        mp4Form.classList.add('hidden');
        playlistMp3Form.classList.add('hidden');
        playlistMp4Form.classList.add('hidden');
        channelMp3Form.classList.add('hidden');
        channelMp4Form.classList.add('hidden');

        if (mp3Btn.checked) {
            if (singleBtn.checked) {
                mp3Form.classList.remove('hidden');
            } else if (playlistBtn.checked) {
                playlistMp3Form.classList.remove('hidden');
            } else if (channelBtn.checked) {
                channelMp3Form.classList.remove('hidden');
            }
        } else if (mp4Btn.checked) {
            if (singleBtn.checked) {
                mp4Form.classList.remove('hidden');
            } else if (playlistBtn.checked) {
                playlistMp4Form.classList.remove('hidden');
            } else if (channelBtn.checked) {
                channelMp4Form.classList.remove('hidden');
            }
        }
    }

    // Add event listeners to radio buttons
    const radioBtns = document.querySelectorAll('input[type="radio"]');
    radioBtns.forEach(btn => {
        btn.addEventListener('change', toggleForms);
    });

    // Initial call to set initial form visibility
    toggleForms();
});
