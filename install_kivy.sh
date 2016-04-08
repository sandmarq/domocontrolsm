#!/bin/sh
sudo apt-get update
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev pkg-config libgl1-mesa-dev libgles2-mesa-dev python-setuptools libgstreamer1.0-dev git-core gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-{omx,alsa} python-dev cython
sudo apt-get install python3-setuptools python3-dev
sudo pip install git+https://github.com/kivy/kivy.git@master
sudo pip3 install git+https://github.com/kivy/kivy.git@master
