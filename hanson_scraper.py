# Importing the module(s)
from tqdm import tqdm
from time import sleep
from pytube import YouTube
import ffmpeg
import os

# ================
# Status of downloads from tqdm library
#for x in tqdm(range(1000)):
#	time.sleep(0.01)
# ================

# ================
# Artifact destination
SAVE_PATH = "/users/khanson/Downloads/"

# Link(s) of the video to be downloaded
# link = "https://www.youtube.com/watch?v=dbsYBv1tt78"
# ================
def download_streams(url):
	# Instantiates the YouTube Object
	try:
		yt = YouTube(url)
		print(yt.title)
		print(yt.author)
	except IOError:
		print("Connection Error..")
	# Creates StreamQuery Object and prints to screen
	try: 
		my_stream = yt.streams
		# Apply video filters to StreamQuery Object 
		video_stream = my_stream.filter(adaptive=True,is_dash=True)
		# Creates list to better read selection(s)
		video_stream_list = list(enumerate(video_stream))
		for i in video_stream_list:
			print(i)
	except IOError:
		print("Error creating StreamQuery Object..")
	# Prompt user for video download request
	try: 
		video_stream_num = int(input("Select the Video Stream you want to download: "))
		print("===============")
		print("Starting Download of Video File...")
		# Start downloading video with given format to given output
		v = video_stream[video_stream_num].download(SAVE_PATH,"video.mp4")
		print("Downloaded Successfully!")
	except IOError:
		print("Failure during download of video stream..")
	# Prompt user for audio download request
	try:
		print("=")
		print("=")
		print("=")
		print("=")
		print("The video file is completed, we still need the audio\n"
			  "file as a seperate layer so that quality was not\n"
			  "sacrificed on download. We'll do that now..")
		print("=")
		print("=")
		print("=")
		print("=")
		input("Press Enter to continue...")
		my_audio_stream = yt.streams
		# Apply audio filters to StreamQuery Object 
		audio_stream = my_audio_stream.filter(only_audio=True)
		# Creates audio list to better read selection(s)
		audio_stream_list = list(enumerate(audio_stream))
		for i in audio_stream_list:
			print(i) 
	except IOError:
		print("There is a failure retrieving the audio streams list...")
	# Prompt user for Audio input
	try:	
		audio_stream_num = int(input("Select the Audio Stream you want to download:  "))
		print("===============")
		print("Starting Download of Audio File...")
		# Start downloading audio with given format to given output
		a = audio_stream[audio_stream_num].download(SAVE_PATH, "audio.mp4")
		print("Downloaded Successfully!")
	except IOError:
		print("Failure during download of audio stream..")
		print("=")
		print("=")
		print("=")
		print("=")
		print("Both Audio and Video files have been downloaded.\n"
			  "At this point they need to be post-processed back\n"
			  "into a single artifact.")
		print("=")
		print("=")
		print("=")
		print("=")
		input("Press Enter to continue...")
	
	
	
	# Merges audio and video downloads 
	try:
		# Join files w/ FFmpeg and python-FFmpeg
		v = ffmpeg.input(os.path.join(SAVE_PATH, 'video.mp4' )) # video only
		a = ffmpeg.input(os.path.join(SAVE_PATH, 'audio.mp4')) # audio only
		final_artifact = ffmpeg.concat(v, a, v=1, a=1).output(os.path.join(SAVE_PATH,'r.mp4')).run()
		print(final_artifact)
	except IOError:
		print("Failure while trying to parse files together...")


if __name__ == "__main__":
	
	print("Enter the URL of the video:  ")
	url = input()
	download_streams(url)