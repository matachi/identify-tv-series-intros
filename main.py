#!/usr/bin/env python2
from video import Video, IdenticalFrameFinder


def main():
    video1 = Video('video1.mp4')
    video2 = Video('video2.mp4')
    identical_frame_finder = IdenticalFrameFinder(video1, video2)
    print(identical_frame_finder.find())
    # TODO Very lacking implementation.


if __name__ == '__main__':
    main()