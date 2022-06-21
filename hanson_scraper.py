# importing the module
from pytube import YouTube

# artifact destination
SAVE_PATH = "/users/khanson/Downloads/"

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=dbsYBv1tt78"

# exception handling
try:
	yt = YouTube(link)
	print(yt.title)
except:
	print("Connection Error..")

print(yt.streams.filter(adaptive=True))

stream_selection = input("Select the itag of the stream you'd like to download: ")

try: 
	stream = yt.streams.get_by_itag(stream_selection)
	stream.download
except:
	print(" Error with the downloading process ")

print("The Download for " + yt.title + " has completed successfully! ")