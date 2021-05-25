import time
import unittest

# 测试用例目录
from TestRunner.HTMLTestRunner import HTMLTestRunner

test_dir = './test_case'
# 测试用例目录、匹配以test开头的多个文件、还有一个参数是top_level_dir=None：测试模块的顶层目录，若没有则默认是None
suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    # 获取当前日期时间
    now_time = time.strftime("%Y-%m-%d %H-%M-%S")
    # 生成HTML格式报告(对字节写)
    fp = open('./test_report/' + now_time + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title="测试报告（自定义）", description="描述内容（自定义）")
    runner.run(suits)
    fp.close()
