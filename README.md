# mp3chaps

Commandline utility for adding chapter marks to mp3 files similar to ``mp4chaps`` utility.

Many pocast apps on Android and iOS support chapter markers in both mp4 (aac) and mp3 files.

This utilizes the excellent `eyeD3 <https://github.com/nicfit/eyeD3>`_ tagging module to read and write chapter frames and title subframes.

Note: This project is a fork of [mp3chapters](https://github.com/dskrad/mp3chaps) from [dskrad](https://github.com/dskrad), however, I changed the behavior a bit for me.

# Usage

Just clone this project:

```bash
git clone https://github.com/lesthack/mp3chaps
cd mp3chaps
sudo -H pip install -r requirements.txt
```

So, now you can use as follow:

### List chapters of mp3 file

```bash
python mp3chaps.py -l /path/to/mp3file.mp3
```

### Add chaperts to mp3 file

Note: You need a chapters (txt) file with the next format:

```
00:00:00.000 Introduction
00:02:00.000 Chapter Title
00:42:24.123 Chapter Title
```

So

```bash
python mp3chaps.py -i /path/to/mp3file.mp3 -c /path/to/chaptersfile.txt
```

