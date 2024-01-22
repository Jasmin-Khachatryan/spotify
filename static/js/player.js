<script>
    // Get references to HTML elements
    var audioPlayer = new Audio();  // Create an audio player object
    var playButton = document.querySelector('.fa-play-circle');
    var stopButton = document.querySelector('.fa-stop-circle');
    var nextButton = document.getElementById('next');
    var previousButton = document.getElementById('previous');
    var progressBar = document.getElementById('ProgressBar');
    var songName = document.getElementById('masterSongName');
    var gifImage = document.getElementById('gif');

    // Array of song information (replace with your actual song data)
    var songs = [
        { name: 'CNCO - Tan Facil', url: 'https://example.com/song1.mp3', img: 'https://iscale.iheart.com/catalog/artist/31116368' },
        // Add more songs as needed
    ];

    var currentSongIndex = 0;

    // Function to play the current song
    function playSong() {
        audioPlayer.src = songs[currentSongIndex].url;
        audioPlayer.play();
        playButton.classList.remove('fa-play-circle');
        playButton.classList.add('fa-pause-circle');
    }

    // Function to pause the current song
    function pauseSong() {
        audioPlayer.pause();
        playButton.classList.remove('fa-pause-circle');
        playButton.classList.add('fa-play-circle');
    }

    // Function to play the next song
    function nextSong() {
        currentSongIndex = (currentSongIndex + 1) % songs.length;
        updateSongInfo();
        playSong();
    }

    // Function to play the previous song
    function previousSong() {
        currentSongIndex = (currentSongIndex - 1 + songs.length) % songs.length;
        updateSongInfo();
        playSong();
    }

    // Function to update song information on the UI
    function updateSongInfo() {
        songName.textContent = songs[currentSongIndex].name;
        gifImage.src = songs[currentSongIndex].img;
    }

    // Event listener for play/pause button
    playButton.addEventListener('click', function () {
        if (audioPlayer.paused) {
            playSong();
        } else {
            pauseSong();
        }
    });

    // Event listener for stop button
    stopButton.addEventListener('click', function () {
        audioPlayer.pause();
        audioPlayer.currentTime = 0;
        playButton.classList.remove('fa-pause-circle');
        playButton.classList.add('fa-play-circle');
    });

    // Event listener for next button
    nextButton.addEventListener('click', function () {
        nextSong();
    });

    // Event listener for previous button
    previousButton.addEventListener('click', function () {
        previousSong();
    });

    // Event listener for progress bar
    progressBar.addEventListener('input', function () {
        var progress = progressBar.value / 100;
        audioPlayer.currentTime = audioPlayer.duration * progress;
    });

    // Event listener for updating progress bar as the song plays
    audioPlayer.addEventListener('timeupdate', function () {
        var progress = (audioPlayer.currentTime / audioPlayer.duration) * 100;
        progressBar.value = progress;
    });

    // Initial setup
    updateSongInfo();
</script>
