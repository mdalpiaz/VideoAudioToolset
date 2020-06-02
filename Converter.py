import sys
import subprocess

if len(sys.argv) != 3:
    print("Usage: python Converter.py <input file> <output format>")
    sys.exit(1)

# constant filename
INPUTFILE = sys.argv[1]

# call ffmpeg
subprocess.run(["ffmpeg", "-i", INPUTFILE, (INPUTFILE + "_converted." + sys.argv[2])])
