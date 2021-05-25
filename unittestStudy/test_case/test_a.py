import codecs
import csv
import unittest
from itertools import islice

from test_case.a import A


class TestA(unittest.TestCase):

    # def dy(self, cs):
    #     a1 = A()
    #     a1.a()
    #     self.assertEqual(cs, "a")
    #
    # def test_a(self):
    #     with codecs.open("./data_file/ceshi.csv", 'r', 'GBK') as f:
    #         data = csv.reader(f)
    #         # iislice(iterable, start, stop, step):
    #         # 返回从迭代器中的start位置，步长为step，直到stop位置的元素
    #         # 如果stop为None，则一直迭代到最后位置，step是步长
    #         # 这里是从第一行到最后一行
    #         for line in islice(data, 1, None):
    #             # 第二个竖行，也就是数据值那一列
    #             cs = line[1]
    #             self.dy(cs)

    # 断言参数
    def dy(self, cs):
        a1 = A()
        a1.a()
        self.assertEqual(cs, "a")

    @classmethod
    def setUp(cls):
        cls.test_data = []
        with codecs.open('./data_file/ceshi.csv', 'r', 'GBK') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                cls.test_data.append(line)

    def test_1(self):
        """用例1"""
        self.dy(self.test_data[0][1])

    def test_2(self):
        """用例2"""
        self.dy(self.test_data[1][1])

    def test_3(self):
        """用例3"""
        self.dy(self.test_data[2][1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
