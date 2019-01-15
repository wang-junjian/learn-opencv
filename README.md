# Learn OpenCV

## Install OpenCV4 on CentOS7
* 安装CMake新版本
```bash
wget https://github.com/Kitware/CMake/releases/download/v3.13.3/cmake-3.13.3.tar.gz
cd cmake-3.13.3/
./bootstrap
make
make install

sudo nano ~/.bashrc
export CMAKE_ROOT=/usr/local/bin/
```

* 安装OpenCV4
```bash
wget https://github.com/opencv/opencv/archive/4.0.0.zip
unzip 4.0.0.zip
cd opencv-4.0.0/
mkdir build
cd build/
cmake -D CMAKE_BUILD_TYPE=DEBUG -D CMAKE_INSTALL_PREFIX=/usr/local ..
make
make install
sudo ldconfig

cd /usr/lib/python3.6/site-packages
ln -s /usr/local/python/cv2/python-3.6/cv2.cpython-36m-x86_64-linux-gnu.so cv2.so
```

* 测试OpenCV
```bash
cd
git clone https://github.com/opencv/opencv_extra.git
export OPENCV_TEST_DATA_PATH=~/dev/opencv-4.0.0/opencv_extra/testdata
cd $OPENCV_TEST_DATA_PATH
./opencv_test_photo
```

## 参考资料
* [How to install OpenCV 4 on Ubuntu](https://www.pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/)
* [How to Install OpenCV on CentOS 7](https://www.vultr.com/docs/how-to-install-opencv-on-centos-7)
* [Installing CMake](https://cmake.org/install/)
* [OpenCV 4.0](https://opencv.org/opencv-4-0-0.html)
* [Install OpenCV 4 on CentOS 7 (C++ and Python)](https://www.learnopencv.com/install-opencv-4-on-centos-7/)

* [目标追踪](object-tracking/)
