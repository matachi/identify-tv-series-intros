import csv
import os

"""Functions for saving and retrieving timepoints of the files' intros' start and end."""

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
SKIPINTRO_DIR = os.path.join(CURRENT_DIR, '.skipintro')
TIMEPOINTS_FILE = os.path.join(SKIPINTRO_DIR, 'timepoints.csv')


def append(filename, start, end):
    """Store when a file's intro starts and ends.

    Args:
        filename: The file's  name.
        start: When the intro starts.
        end: When the intro ends.
    """
    if not os.path.exists(SKIPINTRO_DIR):
        os.makedirs(SKIPINTRO_DIR)

    with open(TIMEPOINTS_FILE, 'ab') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([filename, start, end])


def retrieve():
    """Retrieve a list of all timepoints.

    Returns:
        A list looking like:
            [{'filename': 'video1.mp4', 'start': 1010, 'end': 1250}, ...]
    """
    if not os.path.exists(TIMEPOINTS_FILE):
        return

    with open(TIMEPOINTS_FILE, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file)
        return [{'filename': row[0], 'start': row[1], 'end': row[2]} for row in csv_reader]


def clear():
    """Remove all timepoints from the storage."""
    if not os.path.exists(TIMEPOINTS_FILE):
        return

    with open(TIMEPOINTS_FILE, 'wb') as _:
        pass
