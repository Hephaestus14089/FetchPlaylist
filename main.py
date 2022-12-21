#!/usr/bin/env python3

from pytube import YouTube

def download(link):
   ytObj = YouTube(link)
   ytObj = ytObj.streams.get_highest_resolution()

   try:
      ytObj.download()
   except:
      print("An error occurred")

   print("Download completed successfully")

link = input("Enter youtube video url: ")
download(link)
