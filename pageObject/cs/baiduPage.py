from poium import Page, Element, Elements


# 继承Page类
class BaiDuPage(Page):

    # timeout:元素超时时间，默认是10
    # describe：描述，增加元素定义的可读性
    shu_ru = Element(id_="kw", describe="输入操作")
    cha_xun = Element(id_="su")

    # 可以定位一组元素
    # batch_shuru = Elements(class_name='class', timeout=5)

    # 还支持其他的定位方式
