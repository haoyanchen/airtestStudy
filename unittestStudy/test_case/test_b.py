import unittest

from parameterized import parameterized

from test_case.b import B


class TestB(unittest.TestCase):

    # 断言参数
    def b(self, cs):
        b1 = B()
        b1.b(cs)

    # 通过parameterized实现参数化
    # 通过@parameterized.expand装饰测试用例test_dy
    @parameterized.expand([
        ("case1", "1"),
        ("case2", "a"),
        ("case3", "b"),
    ])
    # 这里要name参数(name对应元组中第一列数据，如case1,用于定义测试用例名称，如test_dy_0_case1)
    def test_dy(self, name, cs):
        self.b(cs)
        self.assertEqual(cs, "b")


if __name__ == '__main__':
    # 2：输入更详细的日志
    unittest.main(verbosity=2)
