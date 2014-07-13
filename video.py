from frame_list import FrameList


class Video:
    """Encapsulates a video and its frames."""

    def __init__(self, filename):
        """
        Args:
            filename: The video's filename.
        """
        self.filename = filename
        self.frames = FrameList(self)
        self.__start = 0

    def __len__(self):
        """
        Returns:
            The video file's number of frames.
        """
        return len(self.frames)


class IdenticalFrameFinder:
    """A class for finding frames in two videos that result in the same hash."""

    FPS = 24
    INTERVAL = 15*FPS

    def __init__(self, video1, video2):
        """
        Args:
            video1: An instance of Video.
            video2: An instance of Video.
        """
        self.video1 = {'video': video1, 'identical': -1}
        self.video2 = {'video': video2, 'identical': -1}

    def find(self):
        """Run the finder.

        Returns:
            A tuple of frame numbers from the two videos that share hash value.
        """
        # TODO Fix this method.
        for video1_slice in self.__list_of_frame_slices(self.video1['video']):
            video1_hash_set = self.video1['video'].frames[video1_slice]
            for video2_slice in self.__list_of_frame_slices(self.video2['video']):
                video2_hash_set = self.video1['video'].frames[video2_slice]
                frame1, frame2 = self.__get_identical_frame_from_hash_sets(video1_hash_set, video2_hash_set)
                return frame1, frame2
        return -1, -1

    @staticmethod
    def __list_of_frame_slices(video):
        """Get a list of slices of frames that should be checked.

        Args:
            video: An instance of Video.
        Returns:
            A list of slices.
        """
        return [
            slice(
                start,
                start + IdenticalFrameFinder.INTERVAL + 10,
                10
            ) for start in range(
                0,
                int(0.3 * len(video)),
                IdenticalFrameFinder.INTERVAL*2
            )
        ]

    @staticmethod
    def __get_identical_frame_from_hash_sets(hash_set1, hash_set2):
        """Compare two lists of hashes and find similar hashes.

        Args:
            hash_set1: A list of tuples of the frame number and hash, for example:
                [(100, 2932982313), (110, 3493429832)]
            hash_set2: The same as hash_set1.
        Returns:
            A tuple of frame numbers whose hashes are more or less the same.
        """
        for hash1 in hash_set1:
            for hash2 in hash_set2:
                if abs(hash1[1] - hash2[1]) < 1e15:
                    return hash1[0], hash2[0]
        return -1, -1