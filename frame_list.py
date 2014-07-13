from tempfile import NamedTemporaryFile
import cv2
import pHash


class FrameList(dict):
    """A list of frames, mapping the indices to their hashes.

    Usage examples:
        >> v = Video('~/video.mp4')
        >> f = v.frames
        >> len(f)     # Number of frames
        30153
        >> f[100]     # Get the hash of frame 100
        17574810791425954274
        >> f[30000]   # Get the hash of frame 30000
        1385074781582455747
        >> f.save(10) # Save frame 10 as a JPG image
    """

    def __init__(self, video):
        """
        Args:
            video: An instance of a Video.
        """
        self.video = video
        self.__len = -1
        super(dict, self).__init__()

    def __len__(self):
        if self.__len == -1:
            video = cv2.VideoCapture(self.video.filename)
            # Cache the length
            self.__len = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
        return self.__len

    def __getitem__(self, frame_number):
        if type(frame_number) is slice:
            return [(frame, self[frame]) for frame in range(
                frame_number.start,
                frame_number.stop,
                frame_number.step if frame_number.step else 10
            )]

        if frame_number in self:
            return self.get(frame_number)

        video = cv2.VideoCapture(self.video.filename)
        video.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frame_number)

        success, frame = video.read()

        temporary_image_file = NamedTemporaryFile(suffix='.jpg')
        cv2.imwrite(temporary_image_file.name, frame)
        frame_hash = pHash.imagehash(temporary_image_file.name)

        self[frame_number] = frame_hash
        return frame_hash

    def save(self, frame_number):
        """Save a frame as a JPG image.

        Args:
            frame_number: The frame to save.
        """
        video = cv2.VideoCapture(self.video.filename)
        video.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frame_number)
        success, frame = video.read()
        cv2.imwrite('%s - %d.jpg' % (self.video.filename, frame_number), frame)

