import ffmpeg

input_file = r"D:\python programming\python_project\bhajan.mp4"
output_file = 'convert.mp3'

ffmpeg.run( ffmpeg.input(input_file).output(output_file))

print("Audio saved as MP3!")


                                            
