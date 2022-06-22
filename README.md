██╗  ██╗ █████╗ ███╗   ██╗███████╗ ██████╗ ███╗   ██╗    
██║  ██║██╔══██╗████╗  ██║██╔════╝██╔═══██╗████╗  ██║    
███████║███████║██╔██╗ ██║███████╗██║   ██║██╔██╗ ██║    
██╔══██║██╔══██║██║╚██╗██║╚════██║██║   ██║██║╚██╗██║    
██║  ██║██║  ██║██║ ╚████║███████║╚██████╔╝██║ ╚████║    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝    
                                                         
██████╗ ███████╗ █████╗ ██████╗ ███╗   ███╗███████╗      
██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝      
██████╔╝█████╗  ███████║██║  ██║██╔████╔██║█████╗        
██╔══██╗██╔══╝  ██╔══██║██║  ██║██║╚██╔╝██║██╔══╝        
██║  ██║███████╗██║  ██║██████╔╝██║ ╚═╝ ██║███████╗      
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚══════╝      
                                                         
# Youtube-scraper 
I wanted something that would inclusively download, parse, and
spit out a final artifact from YouTube. There are a lot of random libraries out there that have small bits of functionality, but this app only requests the url of the video you want and then displays options for the individual streams. 

Originally, you could download progressive streams that had both audio and video encoded together. This is still a possibility, however, your downloads are limited to 720p with the inclusion of Dynamic Adaptive Streaming over HTTP (DASH). 1080p and above requires that you use the adaptive streaming over the progressive type, and download the audio and video codecs seperately. This allows you to bypass the bandwidth limitations.

After both codec files are downloaded, I utilized ffmpeg-python to post process the files, and concatenate them back together. This results in the final artifact in .mp4 format that can be dynamically reshaped to fit various screen resolutions as well as exceeds the 720 restriction.

## Resource(s)
### Pytube Library
[https://pytube.io/en/latest/index.html]
### ffmpeg-python
[https://github.com/kkroening/ffmpeg-python]

## Future Ideas: 
1. Progress bar for the ffmpeg piece
2. Include place to change save location
3. Change font/color theme
4. Menu selection for video properties
5. Look into decreasing the length of video encoding
