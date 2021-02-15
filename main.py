import ffmpeg
import os
def conv():
    playlist = input('Please paste the full path to the .m3u8 file: ')
    out = input('output filename (without the .mp3): ')
    (
        ffmpeg
        .input(playlist)
        .output(out+'.mp3')
        .run()
    )
count = 0
os.system('cls')
while True:
    conv()
    os.system('cls')
    def increase():
        global count
        count += 1
    increase()
    if count != 0:
        print(count, 'file(s) done')
        print("input the next file, if you're done press CTRL + C")
        print(' ')
