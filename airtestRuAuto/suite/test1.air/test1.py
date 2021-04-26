from airtest.core.api import *
from airtest.cli.parser import cli_setup
# 连接设备
# connect_device("Android://127.0.0.1:5037/FIFIMFFEPVAIWCU8")

if not cli_setup():
    auto_setup(__file__, logdir='./suite/test1.air/log')

print("cs1-----")
touch(Template(r"tpl1616502023840.png", record_pos=(0.402, 0.979), resolution=(1080, 2280)))
sleep(4)



