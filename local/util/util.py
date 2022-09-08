# -*- coding:utf-8 -*-

def str2int(s):
    """字符串转int，失败返回None
    """
    for e in s:
        if e < '0' or e > '9':
            return None

    return int(s)