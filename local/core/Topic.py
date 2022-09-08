# -*- coding:utf-8 -*-
# 话题，Msg，Attr等结构体

class Attr:
    """某个topic中的一个字段
    
    Attributes:
        path: 字段路径
        type: 类型
        value: 值
        label: 展示标签
        name: 名字
        type_str: 类型的名字
    """

    def __init__(self, path, type, value, label) -> None:
        self.path = path
        self.type = type
        self.value = value
        self.label = label
        self.name = self.path.split(".")[-1]
        self.type_str = self.get_type_str(type)
    
    def get_type_str(self, type):
        type_str = ""
        if type == float:
            type_str = "float"
        elif type == int:
            type_str = "int"
            
        return type_str


class Topic:
    """一个topic，包含多个Attr
    
    Attributes:
        uri: 名字
        type: 类型
        attrs: 字段列表
    """
    
    def __init__(self, uri, type) -> None:
        self.uri = uri
        self.type = type
        self.attrs = list()

    def add(self, attr):
        self.attrs.append(attr)


class Msg:
    """消息实体
   
    Attributes:
        topic: 话题
        msg: 消息实体
    """ 
    def __init__(self, topic) -> None:
        self.topic = topic
        self.msg = None

    def callback(self, msg):
        self.msg = msg

    def attr(self, attr):
        """获取属性的值，赋值给attr
        
        Args:
            attr: Attr结构体
        """
        data = self.msg

        if data is not None:
            attr_list = attr.path.split('.')
            for a in attr_list:
                data = getattr(data, a)
            attr.value = data