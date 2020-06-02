# VideoAudioToolset
Some Python 3 Scripts for converting and generally working with video/audio files.  
It requires FFmpeg and FFprobe in the same directory for it to work.

## Converter
Usage:  
`python Converter.py <input file> <output format>`  
Requires:  
FFmpeg

## Compressor
Usage:  
`python Compressor.py <input file> [<crf=26>]`  
Requires:  
FFmpeg

## Splitter
Usage:  
`python Splitter.py <input file>`  
Requires:  
FFmpeg  
FFprobe
