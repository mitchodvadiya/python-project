import ffmpeg

input_file = r"D:\python programming\python_project\bhajan.mp4"
output_file = 'convert.mp3'

ffmpeg.input(input_file).output(output_file, format='mp3', acodec='libmp3lame').run()

print("Audio saved as MP3!")

                                            