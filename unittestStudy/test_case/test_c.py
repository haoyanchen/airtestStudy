import unittest

from ddt import data, unpack, ddt, file_data

from test_case.c import C

# 测试类需要ddt装饰
@ddt
class TestC(unittest.TestCase):

    # 断言参数
    def dy(self, cs):
        c1 = C()
        c1.c(cs)

    # 列表
    @data(["case1", "1"], ["case2", "a"], ["case3", "b"])
    @unpack
    def test_sz(self, case, cs):
        self.dy(cs)
        self.assertEqual(cs, "1")

    # 元组
    @data(("case1", "1"), ("case2", "a"), ("case3", "b"))
    @unpack
    def test_a(self, case, cs):
        self.dy(cs)
        self.assertEqual(cs, "a")

    # 字典
    # 注意：这里传入的是cs
    @data({"cs": "1"}, {"cs": "a"}, {"cs": "b"})
    @unpack
    def test_b(self, cs):
        self.dy(cs)
        self.assertEqual(cs, "b")

    # 参数化读取JSON文件(这里是有.就文件找不到，不知道是不是这个路径是相对于本文件，而不是相对于根目录的)
    # @file_data('ddt_data_file.json')：文件和.py在同一个目录下就行，要不要指定路径
    @file_data('../data_file/ddt_data_file.json')
    def test_c(self, cs):
        self.dy(cs)
        self.assertEqual(cs, "c")

    # 参数化读取yaml文件
    @file_data('../data_file/ddt_data_file.yaml')
    def test_d(self, case):
        cs = case[0]["cs"]
        self.dy(cs)
        self.assertEqual(cs, "d")


if __name__ == '__main__':
    # 2：输入更详细的日志
    unittest.main(verbosity=2)
