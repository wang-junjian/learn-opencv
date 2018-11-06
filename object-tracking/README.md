# 目标追踪 Object Tracking

## object_tracker.py
```bash
usage: object_tracker.py [-h] [-v VIDEO]
                         [-t {BOOSTING,MIL,KCF,TLD,MEDIANFLOW,GOTURN,MOSSE,CSRT}]

optional arguments:
  -h, --help            show this help message and exit
  -v VIDEO, --video VIDEO
                        video file path. default open camera.
  -t {BOOSTING,MIL,KCF,TLD,MEDIANFLOW,GOTURN,MOSSE,CSRT}, --tracker {BOOSTING,MIL,KCF,TLD,MEDIANFLOW,GOTURN,MOSSE,CSRT}
                        tracker type. default CSRT
```
## 视频文件
* [百米赛跑](hundred-meters-race.mov)

## 快照
![](hundred-meters-race.gif)

## 参考资料
* [深度学习和目标跟踪](https://zhuanlan.zhihu.com/DCF-tracking)
* [计算机视觉中，目前有哪些经典的目标跟踪算法？](https://www.zhihu.com/question/26493945)
* [VOT2018：SiamNet大崛起](https://zhuanlan.zhihu.com/p/46669238)
* [DaSiamRPN - Distractor-aware Siamese Networks for Visual Object Tracking (ECCV2018)](https://github.com/foolwood/DaSiamRPN)
* [ECCV视觉目标跟踪之DaSiamRPN](https://zhuanlan.zhihu.com/p/42546692)
* [OpenCV Object Tracking](https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/)
* [用OpenCV实现八种不同的目标跟踪算法](https://www.jqr.com/article/000383)
* [GOTURN : Deep Learning based Object Tracking](https://www.learnopencv.com/goturn-deep-learning-based-object-tracking/)
* [opencv2/core/version.hpp](https://github.com/opencv/opencv/blob/master/modules/core/include/opencv2/core/version.hpp)
* [cv::MultiTracker Class Reference](https://docs.opencv.org/trunk/d8/d77/classcv_1_1MultiTracker.html)
* [How to Detect and Track Object With OpenCV](https://www.intorobotics.com/how-to-detect-and-track-object-with-opencv/)
* [Object Tracking using OpenCV (C++/Python)](https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/3/)
* [SiameseFC和CFNet细节笔记](https://blog.csdn.net/fzp95/article/details/81867190)
* [用OpenCV实现八种不同的目标跟踪算法](https://www.jqr.com/article/000383)
* [Make Animated GIFs from Movies in Mac OS X with Drag & Drop Ease](http://osxdaily.com/2016/04/08/make-animated-gif-from-movie-mac-os-x-drop-to-gif/)
