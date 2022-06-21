import ffmpeg 

video_stream = input(' Please enter the name of the VIDEO file here..')
audio_stream = input(' Please enter the name of the AUDIO file here..')

ffmpeg.output(audio_stream, video_stream, 'out.mp4')