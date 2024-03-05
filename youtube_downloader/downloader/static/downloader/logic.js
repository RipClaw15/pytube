document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#mp3-btn').addEventListener('click', () => load_mp3_url());
    document.querySelector('#mp4-btn').addEventListener('click', () => load_mp4_url());
    document.querySelector('#playlist-btn').addEventListener('click', () => load_playlist_url());
    document.querySelector('#channel-btn').addEventListener('click', () => load_channel_url());
})

function load_mp3_url()
{
    document.querySelector('#mp4').style.display = 'none';
    document.querySelector('#playlist').style.display = 'none';
    document.querySelector('#channel').style.display = 'none';
    document.querySelector('#mp3').style.display = 'block';
}

function load_mp4_url()
{
    document.querySelector('#mp3').style.display = 'none';
    document.querySelector('#playlist').style.display = 'none';
    document.querySelector('#channel').style.display = 'none';
    document.querySelector('#mp4').style.display = 'block';
}

function load_playlist_url()
{
    document.querySelector('#mp3').style.display = 'none';
    document.querySelector('#mp4').style.display = 'none';
    document.querySelector('#channel').style.display = 'none';
    document.querySelector('#playlist').style.display = 'block';
}

function load_channel_url()
{
    document.querySelector('#mp3').style.display = 'none';
    document.querySelector('#mp4').style.display = 'none';
    document.querySelector('#playlist').style.display = 'none';
    document.querySelector('#channel').style.display = 'block';
}