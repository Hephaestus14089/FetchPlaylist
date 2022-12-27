from pytube import contrib
from pytube import YouTube
from pytube.cli import on_progress

def get_playlist(link):
   return contrib.playlist.Playlist(link)

def get_videoObj_list(playlistObj):
   videoUrlList = playlistObj.video_urls
   videoObjList = []
   for videoUrl in videoUrlList:
      videoObjList.append(YouTube(videoUrl, on_progress_callback=on_progress))
   return videoObjList

def download_video(videoObj):
   stream = videoObj.streams.get_highest_resolution()
   try:
      stream.download()
      print("Done.")
   except:
      print("Unknown error while downloading video")

def download_playlist(link):
   playlistObj = get_playlist(link)
   try:
      playlistTitle = playlistObj.title
      print(f'Playlist found: "{playlistTitle}"')
   except:
      print("Error: Unable to find playlist\t:(")
      return None

   videoObjList = get_videoObj_list(playlistObj)
   for videoObj in videoObjList:
      print(f'Downloading "{videoObj.title}"...')
      download_video(videoObj)
