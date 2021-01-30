from airtest.core.android import Android
from airtest.core.api import sleep, keyevent
from airtest.core.cv import Template


dev = Android()

def home():
    """
    返回家
    :return: None
    """
    while True:
        pos = Template(r"item/home-tower.png").match_in(dev.snapshot())
        if pos is not None:
            dev.touch(pos)
            sleep(1)
            break

        pos = Template(r"item/home-map.png").match_in(dev.snapshot())
        if pos is not None:
            dev.touch(pos)
            sleep(1)
            dev.touch(pos)
            sleep(1)
            break

        keyevent('BACK')
