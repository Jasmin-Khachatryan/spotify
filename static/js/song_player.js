
    function iframeToggle() {
        document.getElementById('ytbPlayerCont').classList.toggle('hidden');
    };


    var player;
    var pauseButton = document.getElementById("pauseicon");
    var playButton = document.getElementById("playicon");
    pauseButton.classList.toggle("hidden");
    document.getElementById("progressBar").value = 0;
    var progressBar = document.getElementById("progressBar");


    var dur;

    // this function gets called when API is ready to use
    function onYouTubePlayerAPIReady() {
        // create the global player from the specific iframe (#video)
        player = new YT.Player('video', {
            events: {
                // call this function when player is ready to use
                'onReady': onPlayerReady,
                'onStateChange': onPlayerStateChange
            }
        });
    }

    function str_pad_left(string, pad, length) {
        return (new Array(length + 1).join(pad) + Math.round(string)).slice(-length);
    }


    var iframe = document.getElementById("video");



    function playSong(id, playlistId, liked=false) {
        if (liked){
            iframe.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&controls=0&disablekb=1&enablejsapi=1&iv_load_policy=3&vq=medium`;
            play();
        } else{
        iframe.src = `https://www.youtube-nocookie.com/embed/?listType=playlist&list=${playlistId}&index=${id}&autoplay=1&controls=0&disablekb=1&enablejsapi=1&iv_load_policy=3&vq=medium`;
        play();
        }
    };

    function nextSong(){
        player.nextVideo();
        play();
    }


    function play() {
        if (pauseButton.classList.contains("hidden")) {
            playButton.classList.toggle("hidden");
            pauseButton.classList.toggle("hidden");
        };
        player.playVideo();
    };

    function pause() {
        if (playButton.classList.contains("hidden")) {
            pauseButton.classList.toggle("hidden");
            playButton.classList.toggle("hidden");
        };
        player.pauseVideo();
    };


    function infoUpdate() {
      try{
        dur = player.getDuration();
        let minutes = Math.floor(dur / 60);
        let seconds = dur - minutes * 60;
        let finalTime = str_pad_left(minutes, '0', 2) + ':' + str_pad_left(seconds, '0', 2);
        document.getElementById("duration").innerHTML = finalTime;
        var nowPlaying = player.getVideoData();
        // console.log(nowPlaying, 'hey')
        document.getElementById('songName').innerHTML = nowPlaying['title'];
        document.getElementById('channel').innerHTML = nowPlaying['author'];
      }
      catch{
          console.log('error!')
          document.getElementById('songName').innerHTML='Heer Ranjha'
          document.getElementById('channel').innerHTML='BB Ki Vines'
      }
    };


    function onPlayerReady(event) {
        playButton.addEventListener("click", play);
        pauseButton.addEventListener("click", pause);
        setVolume();
        onPlayerStateChange(event);
    }


    function goToStart() {
        player.seekTo(0);
        progressBar.value = 0;
        player.previousVideo();
        play();
    }


    function setVolume() {
        let v = Math.floor(document.getElementById("volumeBar").value / 5);
        player.setVolume(v);
        vol_ico = document.getElementById('vol-icon');
        if (v == 0) {
            vol_ico.src = 'https://cdn.discordapp.com/attachments/768083738848133130/773923517091676190/v0.png';
        }
        else if (v < 33) {
            vol_ico.src = 'https://cdn.discordapp.com/attachments/768083738848133130/773921824635093013/v1.png';
        }
        else if (v < 66) {
            vol_ico.src = 'https://cdn.discordapp.com/attachments/768083738848133130/773921822492065843/v2.png';
        }
        else {
            vol_ico.src = 'https://cdn.discordapp.com/attachments/768083738848133130/773921819879014421/v3.png';
        }

    }

progressBar.addEventListener('input', function () {
    var seek = progressBar.value;
    finalSeek = (seek * dur) / 100;
    player.seekTo(finalSeek);
    play()
})

    function onPlayerStateChange(event) {
        console.log('this');
        mytimer = setInterval(function () {
            infoUpdate();

            dur = player.getDuration();
            var playerCurrentTime = player.getCurrentTime();
            var playerTimeDifference = (playerCurrentTime / dur) * 100;
            progressBar.value = playerTimeDifference;
            let minutes = Math.floor(playerCurrentTime / 60);
            let seconds = playerCurrentTime - (minutes * 60);
            let currentDur = str_pad_left(minutes, '0', 2) + ':' + str_pad_left(seconds, '0', 2);
            document.getElementById("currentDur").innerHTML = currentDur;
        }, 1000);



        iframe.addEventListener("DOMAttrModified", function(event) {
            if (event.attrName == "src") {
            console.log('this');
            }
        });
        if (event.data == YT.PlayerState.PLAYING) {
            progressBar.addEventListener('input', function () {
                var seek = progressBar.value;
                finalSeek = (seek * dur) / 100;
                player.seekTo(finalSeek);
            });



            mytimer = setInterval(function () {
                infoUpdate();
                dur = player.getDuration();
                var playerCurrentTime = player.getCurrentTime();
                var playerTimeDifference = (playerCurrentTime / dur) * 100;
                progressBar.value = playerTimeDifference;
                let minutes = Math.floor(playerCurrentTime / 60);
                let seconds = playerCurrentTime - (minutes * 60);
                let currentDur = str_pad_left(minutes, '0', 2) + ':' + str_pad_left(seconds, '0', 2);
                document.getElementById("currentDur").innerHTML = currentDur;
            }, 1000);
        }
    }




    // Inject YouTube API script
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/player_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);


    $(document).on('click', '#like-form', function(e){
      e.preventDefault();
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0');
        var yyyy = today.getFullYear();
        today = dd + '/' + mm + '/' + yyyy;
      console.log('that',{
          'title':$("#songName").text(),
          'channel': $("#channel"),
          'date': today,
          'duration': $("#duration").text(),
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        })



        var youtube_video_id = player.getVideoData()['video_id'];
      $.ajax({
        type:'POST',
        url:window.location.pathname,
        data:{
          'title':$("#songName").text(),
          'songid':youtube_video_id,
          'channel': $("#channel").text(),
          'date': today,
          'duration': $("#duration").text(),
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },

      })

    });