from airtest.core.api import *
from airtest.cli.parser import cli_setup
# 连接设备
# connect_device("Android://127.0.0.1:5037/FIFIMFFEPVAIWCU8")

if not cli_setup():
    auto_setup(__file__, logdir='./suite/test2.air/log')

print("cs2-----")
touch(Template(r"tpl1616507525961.png", record_pos=(-0.196, -0.108), resolution=(2280, 1080)))

