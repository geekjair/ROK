# -*- encoding=utf8 -*-
__author__ = "thou"

import logging

from airtest.core.android.adb import ADB
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.javacap import Javacap
from airtest.core.android import Android, adb
from airtest.utils.logger import get_logger
from airtest.aircv.aircv import *

DEBUG = True
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
import matplotlib.pyplot as plt

# ret = find_all(Template(r"tpl1610026421082.png", record_pos=(-0.429, 0.195), resolution=(2280, 1080)))
# print(ret)
# exists(Template(r"tpl1610026442515.png", record_pos=(-0.431, 0.118), resolution=(2280, 1080)))

# ret = find_all(Template(r"tpl1610026478715.png", record_pos=(-0.429, 0.194), resolution=(2280, 1080)))
# print(ret)
# ret = find_all(Template(r"tpl1610026507266.png", record_pos=(-0.431, 0.118), resolution=(2280, 1080)))
# print(ret)

# exists(Template(r"tpl1610026732683.png", record_pos=(0.437, 0.203), resolution=(2280, 1080)))
# exists(Template(r"tpl1610026787532.png", record_pos=(0.226, 0.116), resolution=(2280, 1080)))
# exists(Template(r"tpl1610026804600.png", record_pos=(-0.228, 0.008), resolution=(2280, 1080)))

# exists(Template(r"tpl1610026898988.png", record_pos=(-0.299, -0.085), resolution=(2280, 1080)))

# exists(Template(r"tpl1610026942386.png", record_pos=(-0.03, -0.032), resolution=(2280, 1080)))
# exists(Template(r"tpl1610030834716.png", record_pos=(0.326, -0.168), resolution=(2280, 1080)))
# exists(Template(r"tpl1610030868810.png", record_pos=(0.132, 0.004), resolution=(2280, 1080)))
# exists(Template(r"tpl1610030984989.png", record_pos=(0.134, 0.005), resolution=(2280, 1080)))
# exists(Template(r"tpl1610031036905.png", record_pos=(0.115, 0.207), resolution=(2280, 1080)))
#

# while True:
#     ret = find_all(Template(r"tpl1610029582301.png", record_pos=(0.436, 0.086), resolution=(2280, 1080)))
#     print(ret)
#     if ret != None:
#         x,y=ret[0]['result']
#         print('click')
#         touch([x,y])
# #         dev.touch([1085,485])
#     sleep(0.5)

#         dev.touch(ret[0]['result'])


# {'id': 0, 'width': 1080, 'height': 2280, 'xdpi': 403.41, 'ydpi': 402.17, 'size': 6.27, 'density': 3.0, 'fps': 60.0, 'secure': True, 'rotation': 90, 'orientation': 1.0, 'physical_width': 1080, 'physical_height': 2280}
# print(dev.get_display_info())
# dev.pinch(steps=50)
# dev.pinch(steps=50)
# pos = loop_find(Template(r"tpl1610026942386.png", record_pos=(-0.03, -0.032), resolution=(2280, 1080)))
# print(pos)
# dev.touch(pos)
# pos = loop_find(Template(r"tpl1610026478715.png", record_pos=(-0.429, 0.194), resolution=(2280, 1080)))


# dev.touch(pos)
# start_app(ROK_PACKAGE_NAME)

# for i in range(4):
#     st=time.time()
#     ret = Template('1610092262498_26.jpg').match_in(dev.snapshot())
#     print(ret)
#     print('time cost: %s' % ((time.time() - st)))
#     ST.CVSTRATEGY.pop(0)


# 野蛮人 564 955 r=30
# 农田 855  955
# 木材 1145 955
# 石头 1430 955
# 金币 1720 955

# r=dev.get_current_resolution()
# r = dev.start_app_timing(ROK_PACKAGE_NAME, 'com.harry.engine.MainActivity')
# print(r)
# while True:
#     r = dev.get_top_activity()
#     print(r)
#     sleep(1)
#
# snapshot()
# for i in range(100000):
#     dev.swipe((w/2,h/2), (w/2-500,h/2), steps=1)
#     sleep(0.1)


# for i in range(10000):
#     switch_role()
#     print(i)
# pos = loop_find(Template('%s/home-tower.png'))
# dev.touch(pos)
# print('%d -> %s' %(i, pos))

# crack_geetest_vcode()
# frame = jcap.get_frame_from_stream()
# img = plt.imread(BytesIO(frame), "jpg")
# # img = img[200:, 730:1810]
# plt.imshow(img)
# plt.text(110, 1500, '①')
# plt.show()
# img = imread('vcode.png')
# img = np.array(cv2.imencode('.png', img)[1]).tobytes()
# print(img)

# s=time.time()
# r=get_vcode_click_pos('okiyar', 'okiyar', img)
# print(r)
# print(time.time()-s)

# # mark_point(img, (200, 200), circle=True, color=1000, radius=50)
# mask_image(img, [200,200,200,200], color=(0, 0, 255), linewidth=20)
# # img = crop_image(img, [50,50,300,300])
# show(img)
# dev.pinch(steps=100)

# ret = find_all(Template(r"%s/target.png"))
# screen = dev.snapshot()
# plt.imshow(screen)
# n = 1
# for info in ret:
#     print(info)
#
#     x, y = info['result']
#     plt.text(x, y, '%s' % n)
#     n += 1
# plt.show()

# dev.pinch(steps=100)
# dev.start_recording()
# sleep(1)
# # for i in range(10):
# #     import random
# #     x,y=random.randint(100, 200),random.randint(100, 200)
# #     print(x,y)
# #     dev.swipe((w,h), (x,y))
# dev.stop_recording()
# farm()

# dev.keyevent('BACK')
# home()
# while True:
#     pos = loop_find(Template(r'%s/help.png'))
#     if pos:
#         print(pos)
#         dev.touch(pos)
#     sleep(0.5)
# start_app(ROK_PACKAGE_NAME)

# while True:
#     snapshot(quality=99)
#     sleep(1)
# exists(Template(r"tpl1610017921954.png", record_pos=(-0.429, 0.194), resolution=(2280, 1080)))

# ('com.lilithgames.rok.offical.cn', 'com.harry.engine.MainActivity', '7504')
# print(dev.get_top_activity())
# {'id': 0, 'width': 1080, 'height': 2280, 'xdpi': 403.41, 'ydpi': 402.17, 'size': 6.27, 'density': 3.0, 'fps': 60.0, 'secure': True, 'rotation': 270, 'orientation': 3.0, 'physical_width': 1080, 'physical_height': 2280}
# print(dev.get_display_info())

# print(jcap.get_ready())

# while True:
# pass_geetest_vcode()


# while True:
#     snapshot()

# screen=dev.adb.snapshot()
# with open('xxx.png','wb') as f:
#     f.write(screen)

# with open(image_path, "rb") as file:
#     jpg_bin = file.read()
#     image = cv2.imdecode(np.asarray(bytearray(jpg_bin), dtype='uint8'), cv2.IMREAD_COLOR)
#
#     with open(tmp_image_path, 'wb') as tmp_file:
#         tmp_jpg_bin = np.array(cv2.imencode('.jpg', image)[1]).tobytes()
#         tmp_file.write(tmp_jpg_bin)

# dev = Android()
#
# while False:
#     # 找《搜索》小图标
#     pos = Template(r"item/search.png").match_in(dev.snapshot())
#     print('查找:{pos}'.join(pos))
#     if pos is None:
#         home()
#         pos = Template(r'item/home-map.png').match_in(dev.snapshot())
#         print('home map:{pos}'.join(pos))
#         if pos:
#             dev.touch(pos)
#         continue
#     else:
#         dev.touch(pos)
#
#     import random as r
#
#     r = r.randint(1, 3)
#     if r == 1:
#         pos = Template(r"item/farm-string.png")
#
#         print('农田')
#         print(pos)
#         if pos:
#             dev.touch(pos)
#     elif r == 2:
#         pos = loop_find(
#             Template(r"%s/wood-string.png" % ITEM_PATH, record_pos=(-0.003, 0.286), resolution=(2560, 1600)))
#         print('木材')
#         print(pos)
#         if pos:
#             dev.touch(pos)
#     else:
#         pos = loop_find(
#             Template(r"%s/stone-string.png" % ITEM_PATH, record_pos=(0.148, 0.284), resolution=(2560, 1600)))
#         print('石头')
#         print(pos)
#         if pos:
#             dev.touch(pos)
#
#     sleep(3)
#     pos = loop_find(
#         Template(r"%s/search-string.png" % ITEM_PATH, record_pos=(0.001, 0.13), resolution=(2560, 1600)))
#     print('搜索')
#     print(pos)
#     if pos:
#         dev.touch(pos)
#
#     if r == 1:
#         pos = loop_find(Template(r"%s/farm.png" % ITEM_PATH))
#         print('农田2')
#         print(pos)
#         if pos:
#             print(pos)
#             dev.touch(pos)
#     elif r == 2:
#         pos = loop_find(Template(r"%s/wood.png" % ITEM_PATH))
#         print('木材2')
#         print(pos)
#         if pos:
#             print(pos)
#             dev.touch(pos)
#     else:
#         pos = loop_find(Template(r"%s/stone.png" % ITEM_PATH))
#         print('石头3')
#         print(pos)
#         if pos:
#             print(pos)
#             dev.touch(pos)
#
#     pos = loop_find(Template(r'%s/gather-string.png' % ITEM_PATH))
#     print('采集')
#     print(pos)
#     if pos:
#         print(pos)
#         dev.touch(pos)
#         sleep(3)
#
#     result = find_all(Template(r'%s/create-troop-string.png' % ITEM_PATH))
#     if result is not None:
#         print('创建部队')
#         print(pos)
#         dev.touch(result[0]['result'])
#         pos = loop_find(Template(r'%s/march-string.png' % ITEM_PATH))
#         print('行军')
#         print(pos)
#         if pos:
#             dev.touch(pos)
#             sleep(3)
#     else:
#         result = find_all(Template(r'%s/march-string.png' % ITEM_PATH))
#         print('行军2')
#         print(pos)
#         if result is not None:
#             dev.touch((500, 500))
#             break

# import matplotlib.pyplot as plt
# plt.imshow(dev.snapshot())
#
# pos=Template('item/test.png').match_in(dev.snapshot())
# if pos:
#     print('test1')
#     print(pos)
#     plt.text(pos[0], pos[1], 'X')
#
# pos=Template('item/test2.png').match_in(dev.snapshot())
# if pos:
#     print('test2')
#     print(pos)
#     plt.text(pos[0], pos[1], 'X')
#
#
# pos=Template('item/queue-logo.png').match_in(dev.snapshot())
# if pos:
#     print('queue')
#     print(pos)
#     plt.text(pos[0], pos[1], 'X')
#
# plt.show()

from aip import AipOcr

config = {
    'appId': '23519624',
    'apiKey': 'TKy0zut7HeB3Hnj1ivyBDiwe',
    'secretKey': 'KPCGygIFChQGTEOWUOD6iBvPK4f0YGPS'
}

client = AipOcr(**config)

# snapshot()
# def get_file_content(file):
#     with open(file, 'rb') as fp:
#         return fp.read()
#
#
# def img_to_str(image):
#     if isinstance(image, str):
#         image = get_file_content(image)
#     elif not isinstance(image, bytes):
#         return
#
#     result = client.basicGeneral(image)
#     print(result)
#     if 'words_result' in result:
#         return '\n'.join([w['words'] for w in result['words_result']])

# # {'words_result': [{'words': '447.1万'}], 'log_id': 1347874022066487296, 'words_result_num': 1}
# print(img_to_str('ocr3.png'))

# snapshot()
# 农田和木材 6|100800  5|756000
# 石头 6 5|567000
# 金币 6|33600 5|252000

st=time.time()
G.DEVICE.snapshot()
print(time.time()-st)
# s=dev.snapshot()
# pos = Template("item/sleep.png").match_in(s)
# print(pos)
# s=s[pos[1] - 30:pos[1] + 30, pos[0] - 330:pos[0] - 100]
# s=s[15:65, 530:850]
# plt.text(pos[0], pos[1], 'x')
# plt.imshow(s)
# plt.show()
# print()
# s = Android().snapshot()
# pos = Template('item/cpos-flag.png').match_in(s)
# if pos:
#     plt.text(pos[0], pos[1], 'x')
#     # s =s[pos[1]:,pos[0]:]
#     s = s[pos[1] - 30:pos[1] + 30, pos[0]-330:pos[0]-100]
#     plt.imshow(s)
#     plt.show()
from pynput.keyboard import *


# def press(key):
#     print("press: %s" % str(key))
#
#
# def release(key):
#     # print("release: %s" % str(key))
#     pass
#
#
# # with Listener(on_press=press, on_release=release) as listener:
# #     listener.join()
# #     print("lllll")
#
# for i in range(999999999):
#     with open('img/%d.png' % (i+1), 'wb') as f:
#         f.write(dev.adb.snapshot())
#     sleep(1)

# adb = ADB(serialno="emulator-5554")
# ret = adb.get_display_info()
# print(ret)
