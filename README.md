# Partitur
 A program to extract Sheet music from an .mp3 or .wav file
 in case it doesnt work, install the requirenments using 
``pip install -r requirenments.txt``


or if you want to keep a clean workspace, run the folowing commands to create a virtual environment:

``pip -m venv music``

execute the batch/ps/cmdlet/script found in ``.\music\Scripts\`` (whatever suits you)

``pip -r install requirenments.txt``

## This is what it does so far


A sound file is read, here an "a" note played by a piano

![a raw a note played by a piano](/images/piano_a.png)

its fourrier transform extracts frequencies and marks the most important peaks, here one can see the 440Hz of an "a" and its overtone an octave higher

![transform](/images/transformed.png)
