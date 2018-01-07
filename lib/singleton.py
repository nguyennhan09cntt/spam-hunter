#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Singleton in Python
# class Singleton(object):
#     def __new__(clsObj, *args, **kwargs):
#         tmpInstance = None
#         if not hasattr(clsObj, "_instanceDict"):
#             clsObj._instanceDict = {}
#             clsObj._instanceDict[str(hash(clsObj))] = super(Singleton, clsObj).__new__(clsObj, *args, **kwargs)
#             tmpInstance = clsObj._instanceDict[str(hash(clsObj))]
#             tmpInstance.singleton_init(*args, **kwargs)
#         elif not clsObj._instanceDict.has_key(str(hash(clsObj))):
#             clsObj._instanceDict[str(hash(clsObj))] = super(Singleton, clsObj).__new__(clsObj, *args, **kwargs)
#             tmpInstance = clsObj._instanceDict[str(hash(clsObj))]
#             tmpInstance.singleton_init(*args, **kwargs)
#         else:
#             tmpInstance = clsObj._instanceDict[str(hash(clsObj))]
#         return tmpInstance

#     def __init__(clsObj, *args, **kwargs):
#         pass    
    
#     def singleton_init(*args, **kwargs):
#     		raise NotImplementedError

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]