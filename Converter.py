import sys
import subprocess

def convert(filename: str, new_format: str):
    subprocess.run(["ffmpeg", "-i", filename, (filename + "_converted." + new_format)])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Converter.py <input file> <output format>")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
