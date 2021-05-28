import unittest
from time import sleep

from selenium import webdriver

from cs.baiduPage import BaiDuPage


class ChaXun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_1(self):
        bd = BaiDuPage(self.driver)
        bd.get("https://www.baidu.com")
        bd.shu_ru.send_keys("haha")
        bd.cha_xun.click()
        sleep(3)
        # 这里我不懂：为啥我前面的例子加()没事，这里加了就报错：'str' object is not callable
        self.assertEqual(bd.get_title, "haha_百度搜索")

    @classmethod
    def tearDown(cls):
        # cls.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
