#!/usr/bin/env python3

from download import download_playlist

if __name__ == '__main__':
   link = input("Enter youtube video url: ")
   download_playlist(link)
