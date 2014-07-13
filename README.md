# Identify TV series intros

Author: Daniel "MaTachi" Jonsson  
License: [MIT License](LICENSE.md)

A program that's supposed to identify when the intro sequences of downloaded TV series episodes start and end. The
start and end timepoints of the episodes' intros are then saved in `.skipintro/timepoints.csv`.

Not completely implemented yet.

## Set up

Setup instructions for Ubuntu: 

    sudo apt-get install python-opencv
    sudo apt-get install python-dev libphash0-dev # Required to install py-phash
    virtualenv --system-site-packages -p /usr/bin/python2 env
    source env/bin/activate
    pip install git+https://github.com/polachok/py-phash.git

## Run

    ./main.py
