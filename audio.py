import youtube_dl
import os

def downloadMP3(url):
    dwdl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '320'
        }],
    }

    with youtube_dl.YoutubeDL(dwdl_opts) as ydl:
        ydl.download([url])

def downloadMP4(url):
    dwdl_opts = {}

    with youtube_dl.YoutubeDL(dwdl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    url = input('Enter the video url : ')
    #location = input('Enter the save destination : ')
    f = input('[v]ideo or [a]udio : ')

    if f == 'v':
        downloadMP4(url)
    elif f == 'a':
        downloadMP3(url)
    else:
        print("Invalid Choice!!")

