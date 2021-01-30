import time

import cv2
from airtest.core.android.adb import ADB
from airtest.core.android.minicap import Minicap

adb = ADB(
    # serialno='emulator-5554',
    # adb_path=None,
    # server_addr=None,
    # display_id=None,
    # input_event=None
)

devices_list = adb.devices()
adb.serialno = devices_list[0][0]

mcap=Minicap(adb)

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

# lena = mpimg.imread('lena.png') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
# lena.shape #(512, 512, 3)


for frame in mcap.get_stream():
    st=time.time()
    nparr = np.frombuffer(frame, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(len(img))
    print(time.time()-st)

    time.sleep(1)
    # plt.imshow(img)  # 显示图片
    # plt.axis('off')
    # plt.show()

from airtest import aircv
