import sys
import subprocess

def split(filename: str):
    # get number of audio tracks
    num_of_streams = int(subprocess.check_output(["ffprobe", filename, "-show_entries", "format=nb_streams", "-v", "0", "-of", "compact=p=0:nk=1", "-select_streams", "a"], universal_newlines=True))

    # call ffmpeg to extract video
    subprocess.run(["ffmpeg", "-i", filename, "-an", "-vcodec", "copy", "-map", "0:0", (filename + "_video.mp4")])

    # call ffmpeg to extract audio (let's say, we have 4 of those)
    for i in range(1, num_of_streams):
        subprocess.run(["ffmpeg", "-i", filename, "-acodec", "copy", "-vn", "-map", ("0:" + str(i)), (filename + "_track" + str(i) + ".aac")])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Splitter.py <input file>")
        sys.exit(1)
    split(sys.argv[1])
