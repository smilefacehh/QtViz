# -*- coding:utf-8 -*-

class ConnectInfo:
    """网络、adb连接信息
    
    Attributes:
        lan_ip_mac_list: 局域网设备列表
        host_ip_mac: 本机ip
        net_connected: 与客户端建立网络连接
        adb_connected: 与客户端建立adb连接
        connected_client_info: 连接的客户端设备信息
        net_ping: 与客户端网络延迟
    """

    def __init__(self) -> None:
        self.lan_ip_mac_list = list()
        self.host_ip_mac = IpMac()
        self.net_connected = False
        self.adb_connected = False
        self.connected_client_info = None
        self.net_ping = 0


class IpMac:
    """IP信息"""
    ip = ""
    mac = ""


class ClientInfo:
    """客户端信息
    
    客户端: 机器人、PC。

    Attributes:
        name: 客户端名字
        ip_mac: ip + mac
    """
    def __init__(self, name, ip_mac) -> None:
        self.name = name
        self.ip_mac = ip_mac

    def __str__(self) -> str:
        return "name:{0}, ip:{1}, mac:{2}".format(self.name, self.ip_mac.ip, self.ip_mac.mac)