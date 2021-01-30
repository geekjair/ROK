from airtest.cli.parser import cli_setup
from airtest.core.android import Android
from airtest.core.api import sleep, keyevent, auto_setup
from airtest.core.cv import Template
from settings import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "android://127.0.0.1:5037/%s" % (VM if DEBUG else WIRE_VIVO),
    ])

dev = Android()

def home():
    """
    返回家
    :return: None
    """
    while True:
        pos = Template(r"../item/home-tower.png").match_in(dev.snapshot())
        if pos is not None:
            dev.touch(pos)
            sleep(1)
            break

        pos = Template(r"../item/home-map.png").match_in(dev.snapshot())
        if pos is not None:
            dev.touch(pos)
            sleep(1)
            dev.touch(pos)
            sleep(1)
            break

        keyevent('BACK')

def scout():
    home()
    info = dev.get_display_info()
    w=info['width']
    h=info['height']
    while True:
        dev.touch([int(w/2), int(h/2)])
        sleep(1)
        pos = Template("../item/scout.png").match_in(dev.snapshot())
        if pos:
            dev.touch(pos)
            sleep(1)

        pos = Template("../item/scout-manage-string.png").match_in(dev.snapshot())
        if pos:
            flag = False
            while True:

                pos = Template("../item/explore-string.png").match_in(dev.snapshot())
                if pos:
                    dev.touch(pos)
                    sleep(1)


                pos = Template("../item/send-string.png").match_in(dev.snapshot())
                if pos:
                    if not flag:
                        flag = True
                        screen = dev.snapshot()
                        pos = Template("../item/sleep.png").match_in(screen) \
                              or Template("../item/station.png").match_in(screen) \
                              or Template("../item/go-back.png").match_in(screen)

                        if pos:
                            dev.touch(pos)
                            sleep(1)
                    else:
                        dev.touch(pos)
                        sleep(1)
                        break

                sleep(1)
                print("循环监听《探索》按钮中....")

        dev.touch(Template("../item/home-tower.png").match_in(dev.snapshot()))
        sleep(1)

scout()