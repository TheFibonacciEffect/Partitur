# Partitur
A program to extract Sheet music from an .mp3 or .wav file
You can find the newest version in the "unstable" branch and the newest tested version in the "developement" branch.

Install the requirenments using 
``pip install -r requirenments.txt``


or if you want to keep a clean workspace, run the folowing commands to create a virtual environment:

``pip -m venv .music``

execute the batch/ps/cmdlet/script found in ``.\music\Scripts\`` (whatever suits you)

``pip -r install requirenments.txt``

## This is what it does so far


A sound file is read, here an `a` note played by a piano

![a raw a note played by a piano](/images/piano_a.png)

its fourrier transform extracts frequencies and marks the most important peaks, here one can see the 440Hz of an `a` and its overtone an octave higher

![transform](/images/transformed.png)

This will output `[ [0, 12] ]` which means that the first played note is 0 halftone steps away from the pure `a` and the second played note is 12 halftone steps away from the "a" which is an entire octave. This means that the second played note is an `a'` and indeed it is, since `a'` is the overtone of the `a`.
