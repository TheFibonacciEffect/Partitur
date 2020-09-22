# Partitur
A program to extract Sheet music from an .mp3 or .wav file
You can find the newest version in the "unstable" branch and the newest tested version in the "developement" branch.

Install [Python 3.8.3](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64-webinstall.exe) (this is the Windows Webbased installer, for others click [here](https://www.python.org/downloads/release/python-383/), don't forget to add python to PATH ;D

Download and Extract the files from this Directory into a new directory named ``Partitur``

Open your commandline of choice (for example powershell)

``cd [your path, where you extracted the files]``

Install the requirenments
``pip install -r requirenments.txt``

or if you want to keep a clean workspace, run the folowing commands to create a virtual environment:

``pip -m venv .music``

execute the batch/ps/cmdlet/script found in ``.\.music\Scripts\`` (whatever suits you)

``pip -r install requirenments.txt``

## How to run the programm

to run the programm just type ``python run.py`` into your commandline

## This is what it does so far


A sound file is read, here an `a` note played by a piano

![a raw a note played by a piano](/images/piano_a.png)

its fourrier transform extracts frequencies and marks the most important peaks, here one can see the 440Hz of an `a` and its overtone an octave higher

![transform](/images/transformed.png)

This will output `[ [0, 12] ]` which means that the first played note is 0 halftone steps away from the pure `a` and the second played note is 12 halftone steps away from the "a" which is an entire octave. This means that the second played note is an `a'` and indeed it is, since `a'` is the overtone of the `a`.

You can also give it an entire file and it will tell you the names of the notes played. This currently only works reliantly with single note melody (no triads) and works a little unreliably when multiple notes are played at the same time and it should detect how many are played and extract all notes which are played at the same time. For example when I play 6 it dosn't give back all the right notes but only 4 and maybe even wrong ones if the instrument isn't tuned correctly.
