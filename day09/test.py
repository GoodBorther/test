#!/usr/bin/python3
class Dict(dict):
    def __init__(self,**kw):
        super().init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Dict' object has no attribute %s'" % key)
    def __setattr__(self,key,value):
        self[key] = value

