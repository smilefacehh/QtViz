# -*- coding:utf-8 -*-
# adb工具方法

import os
import re

def adb_connected(ip):
    """测试设备是否通过adb连接上了

    Returns:
        True连接状态
    """
    ret = os.popen('adb devices').read()
    return True if ip in ret else False


def adb_connect(ip):
    """通过adb连接设备
    
    Returns:
        True连接成功
    """
    ret = os.popen('adb connect %s' % ip).read()
    if 'already connected to' in ret:
        return True
    return False


def adb_disconnect(ip):
    """释放adb连接
    """
    os.popen('adb disconnect %s' % ip)


def adb_login():
    """adb登录"""
    ret = os.popen('adb shell').read()
    if 'error' in ret:
        return False
    return True


def adb_pull(from_path, to_path):
    """通过adb拉取文件

    Args:
        from_path: 机器人路径
        to_path: 本地路径

    Returns:
        True拉取成功
    """
    ret = os.popen('adb devices').read()
    match_obj = re.match(r'.*\d+\.\d+\.\d+\.\d+:\d+.*', ret)
    if not match_obj:
        return False

    ret = os.popen('adb pull %s %s' % (from_path, to_path))
    if 'error' in ret:
        return False

    return True


def adb_push(from_path, to_path):
    """通过adb推送文件

    Args:
        from_path: 本地路径
        to_path: 机器人路径

    Returns:
        True推送成功
    """
    ret = os.popen('adb devices').read()
    match_obj = re.match(r'.*\d+\.\d+\.\d+\.\d+:\d+.*', ret)
    if not match_obj:
        return False

    ret = os.popen('adb push %s %s' % (from_path, to_path))
    if 'error' in ret:
        return False

    return True