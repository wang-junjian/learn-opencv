import sys
import argparse
import cv2

from random import randint


MAJOR, MINOR, REVISION = cv2.__version__.split('.')
WINDOW_NAME = 'Object Tracking'


def run(video_file, tracker_type):
    video = cv2.VideoCapture(video_file)
    if not video.isOpened():
        sys.exit()

    colors = []
    tracker = None
    while True:
        ok, frame = video.read()
        if not ok:
            break

        if not video_file:
            frame = cv2.flip(frame, 1, 0)

        key_code = cv2.waitKey(1)
        if key_code == ord('q'):
            break
        elif key_code == ord(' '):
            bboxs = cv2.selectROIs(WINDOW_NAME, frame, showCrosshair=False)
            if len(bboxs):
                tracker, colors = get_multi_tracker(tracker_type, frame, bboxs)
            else:
                tracker = None

        if tracker:
            tracker_update(frame, tracker, colors)
        
        cv2.imshow(WINDOW_NAME, frame)


def tracker_update(frame, tracker, colors):
    ok, bboxs = tracker.update(frame)
    if ok:
        for i, bbox in enumerate(bboxs):
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, colors[i], 2, 1)


def get_multi_tracker(tracker_type, frame, bboxs):
    colors = []
    tracker = cv2.MultiTracker_create()
    for bbox in bboxs:
        tracker.add(get_tracker(tracker_type), frame, (bbox[0], bbox[1], bbox[2], bbox[3]))
        colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))

    return tracker, colors


def get_tracker(tracker_type):
    trackers = {
        'BOOSTING':     (cv2.TrackerBoosting_create(), 2), 
        'MIL':          (cv2.TrackerMIL_create(), 2), 
        'KCF':          (cv2.TrackerKCF_create(), 2), 
        'TLD':          (cv2.TrackerTLD_create(), 2), 
        'MEDIANFLOW':   (cv2.TrackerMedianFlow_create(), 2), 
        'GOTURN':       (cv2.TrackerGOTURN_create(), 2), 
        'MOSSE':        (cv2.TrackerMOSSE_create(), 4), 
        'CSRT':         (cv2.TrackerCSRT_create(), 4)
    } 

    if tracker_type not in trackers:
        return None

    tracker = trackers[tracker_type]
    tracker_min_minor = tracker[1]
    if int(MINOR) < tracker_min_minor:
        print("OpenCV version don't support")
        sys.exit()

    tracker = tracker[0]

    return tracker


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', type=str, help='video file path. default open camera.')
    parser.add_argument('-t', '--tracker', type=str, default='CSRT',
                                           choices=['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT'],
                                           help='tracker type. default CSRT')
    
    args = parser.parse_args()
    
    video_file = args.video
    if not video_file:
        video_file = 0

    tracker_type = args.tracker

    run(video_file, tracker_type)
