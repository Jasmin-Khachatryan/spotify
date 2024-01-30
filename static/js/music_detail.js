function addToPlaylist() {

    var songId = getSongId();

    // Send an AJAX request to your Django view
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/add_to_playlist/", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xhr.onload = function () {
        if (xhr.status === 200) {
            // Handle success, e.g., show a success message
            alert("Song added to playlist successfully!");
        } else {
            // Handle errors
            alert("Error adding song to playlist");
        }
    };

    xhr.send(JSON.stringify({ song_id: songId }));
}