import sys
import subprocess
from Converter import convert
from Splitter import split

if len(sys.argv) != 2:
    print("Usage: python VideoPreparer.py <input file>")
    sys.exit(1)

filename = sys.argv[1]

split(filename)
convert(filename + "_track1.aac", "m4a")
convert(filename + "_track2.aac", "m4a")
convert(filename + "_track3.aac", "m4a")
convert(filename + "_track4.aac", "m4a")
