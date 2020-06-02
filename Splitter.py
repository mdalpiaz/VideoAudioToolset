import sys
import subprocess

if len(sys.argv) != 2:
    print("Usage: python Splitter.py <input file>")
    sys.exit(1)

# constant filename
INPUTFILE = sys.argv[1]

# get number of audio tracks
num_of_streams = int(subprocess.check_output(["ffprobe", INPUTFILE, "-show_entries", "format=nb_streams", "-v", "0", "-of", "compact=p=0:nk=1", "-select_streams", "a"], universal_newlines=True))

# call ffmpeg to extract video
subprocess.run(["ffmpeg", "-i", INPUTFILE, "-an", "-vcodec", "copy", "-map", "0:0", (INPUTFILE + "_video.mp4")])

# call ffmpeg to extract audio (let's say, we have 4 of those)
for i in range(1, num_of_streams):
    subprocess.run(["ffmpeg", "-i", INPUTFILE, "-acodec", "copy", "-vn", "-map", ("0:" + str(i)), (INPUTFILE + "_track" + str(i) + ".aac")])
