# importing the module(s)
from pytube import YouTube

# artifact destination
SAVE_PATH = "/users/khanson/Downloads/"

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=dbsYBv1tt78"

# object instantiation
try:
	yt = YouTube(link)
	print(yt.title)
except:
	print("Connection Error..")

# print streams
print(yt.streams.filter(adaptive=True))

# allows user selection
stream_selection = input("Select the itag of the video stream you'd like to download: ")

# initiates the downloads
try: 
	stream = yt.streams.get_by_itag(stream_selection)
	stream.download(output_path=SAVE_PATH)
except: 
	print(" Error with downloading the video file ")

try:
	audio_stream = yt.streams.filter(only_audio=True)
	audio_stream.download(output_path=SAVE_PATH)
except:
	print(" Error with downloading the audio file ")


print("The Download for " + yt.title + " has completed successfully! ") 

'''
# Highest Quality will give best video
myHDStream = yt.streams.first()

# Lowest Quality will give best audio
myAudioStream = yt.streams.last()

print(myHDStream, myAudioStream)

myHDStream.download(SAVE_PATH)

myAudioStream.download(SAVE_PATH)
'''