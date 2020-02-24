import youtube_dl
import os

def downloadMP3(url,dest):
    dwdl_opts = {
        'format' : 'bestaudio/best',
        'outtmpl' : dest+"/%(title)s.%(ext)s",
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '320'
        }],
    }

    with youtube_dl.YoutubeDL(dwdl_opts) as ydl:
        ydl.download([url])
        print()

def downloadMP4(url,dest):
    dwdl_opts = {
        'outtmpl' : dest+"/%(title)s.%(ext)s",
    }

    with youtube_dl.YoutubeDL(dwdl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=HJjdahujoMk"
    location = r"C:\Users\9380-85615SG\Desktop\StudyMaterials\Programming\Python\test"
    downloadMP3(url,location)

