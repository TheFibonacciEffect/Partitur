# Partitur
 A program to extract Sheet music from an .mp3 or .wav file
 in case it doesnt work, install the requirenments using 
``pip -r install requirenments.txt``


or if you want to keep a clean workspace, run the folowing commands to create a virtual environment:

``pip -m venv music``

execute the batch/ps/cmdlet/script found in ``.\music\Scripts\`` (whatever suits you)

``pip -r install requirenments.txt``

## This is what it does so far


You have an osszilation, some file that osszilates (obtained from a wav file using the Extractor)

![a raw tone](/images/osszilation.png)

...and you can extract it's frequecies using the Transformator (here 50 Hz and 80 Hz)
![its fourrier transform extracts frequencies](/images/fourrier.png)

