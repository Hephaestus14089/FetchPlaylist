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

def download_playlist(link):
   playlistObj = get_playlist(link)
   try:
      playlistTitle = playlistObj.title
      print(f'Playlist found: "{playlistTitle}"')
   except:
      print("Error: Unable to find playlist\t:(")
      return None

   videoObjList = get_videos(playlistObj)
   for videoObj in videoObjList:
      print(f'Downloading "{videoObj.title}"...')
      download_video(videoObj)
