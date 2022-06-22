# Importing the module(s)
from tqdm import tqdm
import time
from pytube import YouTube

# ================
# Status of downloads from tqdm library
#for x in tqdm(range(1000)):
#	time.sleep(0.01)
# ================

# ================
# Artifact destination
SAVE_PATH = "/users/khanson/Downloads/"
'''
# Prompting user for Youtube Video link
  youtube_url = input("Please enter youtube link ")
'''
# Link(s) of the video to be downloaded
# link = "https://www.youtube.com/watch?v=dbsYBv1tt78"
# ================

def download_video(url):
	# Instantiates the YouTube Object
	try:
		yt = YouTube(url)
		print(yt.title)
		print(yt.author)
	except:
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
	except:
		print("Error creating StreamQuery Object..")

	# Prompt user for video download request
	try: 
		print("Select the Video Stream you want to download: ")
		video_stream_num = int(input("Enter the Stream number: "))
		print("===============")
		print("Starting Download of Video File...")
		
		# Start downloading video with given format to given output
		video_stream[video_stream_num].download(output_path=SAVE_PATH)
		print("Downloaded Successfully!")
	
	except:
		print("Failure during download of video stream..")

	# Prompt user for audio download request
	try:
		print("The video file is completed, we need the audio\n"
			  "file to layer them together after the fact")
		print("Select the Audio Stream you want to download: ")

		# Apply audio filters to StreamQuery Object 
		audio_stream = my_stream.filter(adaptive=True,is_dash=True,audio_stream=True)
		
		# Creates audio list to better read selection(s)
		audio_stream_list = list(enumerate(audio_stream))
		for i in audio_stream_list:
			print(i)
	except:
		print("There is a failure retrieving the audio streams list...")
		
	try:	
		audio_stream_num = int(input("Enter the Stream number: "))
		print("===============")
		print("Starting Download of Audio File...")
		
		# Start downloading audio with given format to given output
		audio_stream[audio_stream_num].download(output_path=SAVE_PATH)
		print("Downloaded Successfully!")
	except:
		print("Failure during download of audio stream..")



if __name__ == "__main__":
	print("Enter the URL of the video:  ")
	url = input()
	download_video(url)