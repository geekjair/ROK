import random
import re

import cv2
import matplotlib.pyplot as plt
import numpy as np
from airtest.core.android import Android

from aip import AipOcr
from airtest.core.api import sleep
from airtest.core.cv import Template

config = {
    'appId': '23519624',
    'apiKey': 'TKy0zut7HeB3Hnj1ivyBDiwe',
    'secretKey': 'KPCGygIFChQGTEOWUOD6iBvPK4f0YGPS'
}

client = AipOcr(**config)

def img_to_str(image):
    if isinstance(image, str):
        with open(image, 'rb') as fp:
            image = fp.read()
    elif not isinstance(image, bytes):
        return

    result = client.basicGeneral(image)
    # print(result)
    # {'words_result': [{'words': '109382'}], 'log_id': 1347901057883176960, 'words_result_num': 1}
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])
from airtest.core.settings import Settings as ST


# ST.CVSTRATEGY = ["surf", "tpl"]
dev=Android()
while True:

    s = dev.snapshot()
    # pos = Template('../item/jin-sum.png').match_in(s)

    # info = dev.get_display_info()
    # x = int(info['width'] / 2)
    # y = int(info['height'] / 2)
    # dx = random.randint(-500, 500)
    # dy = random.randint(-500, 500)
    # # print('%d,%d %d,%d' % (x, y, x + dx, y + dy))
    # dev.swipe([x, y], [x + dx, y + dy])

    pos = Template('../item/res-sum.png').match_in(s)
    if pos:
        plt.text(pos[0], pos[1], 'x')
        s=s[pos[1] - 25:pos[1] + 150,
        pos[0] + 300:pos[0] + 550]
        # s =s[pos[1]:,pos[0]:]
        # s = s[pos[1]-25:pos[1]+25, pos[0]+300:pos[0]+550]
        # s = s[pos[1]-25:pos[1]+15, pos[0]+60:pos[0]+130]
        # s = s[pos[1] - 30:pos[1] + 30, pos[0] - 320:pos[0] - 100]
        # s = s[15:65, 530:850]
        plt.imshow(s)
        plt.show()

        result = img_to_str(np.array(cv2.imencode('.jpg', s)[1]).tobytes())

        print(result)

        # print(img_to_str(np.array(cv2.imencode('.jpg', s)[1]).tobytes()))
        # print(pos)
    break
    sleep(1)

