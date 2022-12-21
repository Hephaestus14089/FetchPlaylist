from pytube import contrib

def get_playlist(link):
   return contrib.playlist.Playlist(link)

def get_videos(playlistObj):
    return playlistObj.videos

def download_video(videoObj):
    videoObj.streams.get_highest_resolution()
    try:
        videoObj.download()
        print("Done.")
    except:
        print("Unknown error while downloading video")

def download_playlist():
    playlistObj = get_playlist(link)
    videoObjList = get_videos(playlistObj)

    print("Videos in playlist are: ")
    for i in range(3):
        videoObj = videoObjList[i]
        print(f"Downloading {videoObj.title} ...")
        download_video(videoObj)

if __name__=='__main__':
    # link = input("Enter youtube video url: ")
    link = "https://www.youtube.com/watch?v=NzLMzbR2JJw&list=PLWvnUfModHP_99Pr-xBNKDZUcJFm7H9m8"
