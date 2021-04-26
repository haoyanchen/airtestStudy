# import os
#
# f = 'test1.air'
# root_dir = 'C:\\Users\\Administrator\\Desktop\\airtestRuAuto\\suite'
# script = os.path.join(root_dir, f)
# print(script)
#
# log = os.path.join(root_dir, 'log' + '\\' + f.replace('.air', ''))
# print(log)
# log_1 = script + '\\' + 'log'
# print(log_1)


#图片列表函数
def picList(id):
    if id == 1:
        a = [1, 2, 3, 4, 5]
    else:
        pass
        return None
    return aa(a)

#遍历识别方法
def aa(a):
    for i in a:
        if i < 6:
            print(i)
            a.remove(i)
            print(a)
            return aa(a)
        else:
            pass
picList(2)