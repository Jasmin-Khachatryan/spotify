document.addEventListener('DOMContentLoaded', function () {
    const addToPlaylistBtn = document.getElementById('addToPlaylistBtn');

    if (addToPlaylistBtn) {
        addToPlaylistBtn.addEventListener('click', function () {
            addToPlaylistHandler();
        });
    }
});

function addToPlaylistHandler() {
    // Extract information about the song from the DOM
    const songTitle = document.querySelector('.artist__info__name').innerText;
    const songId = /* You need to get the song ID, possibly from a data attribute or another way */;

    // Send a request to the server to add the song to the playlist
    addToPlaylistRequest(songId, songTitle);
}

function addToPlaylistRequest(songId, songTitle) {
    fetch('/api/playlists/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token for Django
        },
        body: JSON.stringify({
            songId: songId,
            songTitle: songTitle,
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to add the song to the playlist');
        }
        // Optionally update the UI to reflect the success
        console.log('Song added to the playlist successfully');
    })
    .catch(error => {
        console.error('Error adding the song to the playlist:', error);
    });
}

// Function to get CSRF token from cookies (for Django)
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
