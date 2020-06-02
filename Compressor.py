import sys
import subprocess

if len(sys.argv) == 2:
    CRF = "26"
elif len(sys.argv) == 3:
    CRF = sys.argv[2]
else:
    print("Usage: python Compressor.py <input file> [<crf=26>]")
    sys.exit(1)

# constant filename
INPUTFILE = sys.argv[1]

# call ffmpeg
subprocess.run(["ffmpeg", "-i", INPUTFILE, "-acodec", "copy", "-vcodec", "libx264", "-crf", CRF, (INPUTFILE + "_compressed.mp4")])
