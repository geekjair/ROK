import random

import cv2
import matplotlib.pyplot as plt
import numpy as np
from airtest.core.android import Android

from aip import AipOcr
from airtest.core.cv import Template

from testcase.testhome import *


def farm():
    img_list = ("farm-string.png", "wood-string.png", "stone-string.png")
    while True:
        pos = Template("../item/search.png").match_in(dev.snapshot())
        if pos:
            dev.touch(pos)

        pos = Template("../item/search-string.png").match_in(dev.snapshot())
        if pos:
            pos = Template("../jia.png").match_in(dev.snapshot())
            if pos:
                for i in range(6):
                    dev.touch(pos)
                    sleep(0.2)

            pos = Template('../item/' + img_list[random.randint(0, len(img_list) - 1)]).match_in(dev.snapshot())
            if pos:
                dev.touch(pos)
                sleep(1)

            while True:
                pos = Template('../item/search-string.png').match_in(dev.snapshot())
                if pos is None:
                    break
                else:
                    dev.touch(pos)
                    sleep(1)

                pos = Template("../jian.png").match_in(dev.snapshot())
                if pos:
                    dev.touch(pos)

            flag = False
            while True:
                info = dev.get_display_info()
                w = info['width']
                h = info['height']
                dev.touch([int(w / 2), int(h / 2)])
                plt.imshow(dev.snapshot())
                plt.text(int(w / 2), int(h / 2), 'x')
                plt.show()

                pos = Template('../item/gather-string.png').match_in(dev.snapshot())
                if pos:
                    dev.touch(pos)
                    break

                pos = Template('../attack.png').match_in(dev.snapshot())
                if pos:
                    flag = True
                    break

            if flag:
                break

            while True:
                pos = Template('../item/create-troop-string.png').match_in(dev.snapshot())
                if pos:
                    dev.touch(pos)
                    break

                pos = Template('../item/march-string.png').match_in(dev.snapshot())
                if pos:
                    dev.touch([500,500])
                    return

            while True:
                pos = Template('../item/march-string.png').match_in(dev.snapshot())
                if pos:
                    dev.touch(pos)
                    break


farm()


