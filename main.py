from pytube import YouTube
import os

def checkLocation(save_dest):
    if os.path.isdir(save_dest):
        print("Valid Location. Download gonna starts soon!!")
    else:
        print("Invalid Location.Creating new directory!!")
        os.makedirs(save_dest)

def download(url,dest):
    print("Downloading....")
    YouTube(url).streams.first().download(dest)


if __name__ == '__main__':

    vdo_url = input("Enter the video url to download ")
    save_dest = input("Enter the location to save : ")

    checkLocation(save_dest)
    download(vdo_url,save_dest)

    print('The video has been downloaded to the '+save_dest)