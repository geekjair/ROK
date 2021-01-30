# -*- encoding=utf8 -*-
__author__ = "thou"

import logging
from io import BytesIO

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.javacap import Javacap
from airtest.core.android import Android
from airtest.utils.logger import get_logger
from airtest.aircv.aircv import *

import requests
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from airtest.aircv.aircv import *

DEBUG = False
VIVO_X21 = '4beda60'
VM = 'emulator-5554'
WIRE_VIVO = '192.168.1.101:5555'
BASE_DIR = os.path.dirname(__file__)
ROK_PACKAGE_NAME = 'com.lilithgames.rok.offical.cn'
logger = get_logger("airtest")
logger.setLevel(logging.INFO)

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "android://127.0.0.1:5037/%s" % (VM if DEBUG else WIRE_VIVO),
    ])

dev = Android()
jcap = Javacap(dev.adb)

w = 1080
h = 2280

# 1610031939987.jpg
img = plt.imread('log/1.jpg')
xs = int(w/7) - 20
xe = w
ys = int(h/3) - 30
ye = 2*ys
print(xs)
print(xe)
print(ys)
print(ye)

img = img[xs:, ys:ye]
plt.imshow(img)
plt.show()