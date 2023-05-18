import os
class Config(object):
    PROXY_ENABLE = True
    PROXYS = ['sock5h://username:password@ipaddress:1080',''] # blank one at end for not proxying connection. i.e. it will randomly go direct