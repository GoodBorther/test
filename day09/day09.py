#!/usr/bin/python3
#-*- conding: utf-8 -*-
class ListMetaclass(type): ## 定义元类需要从type类型派生
    def __new__(cls,name,bases,attrs): ## __new__需要接收的四个参数：1.准备创建的类的对象；2.类的名字；3.类继承的父类集合；4.类的方法集合
        attrs['add'] = lambda self,value: self.append(value) ##定义了一个列表的add方法，使用匿名函数定义，返回list.append(值)
        return type.__new__(cls,name,bases,attrs) ##返回当前方法
class MyList(list,metaclass=ListMetaclass):
    pass
L = MyList()
L.add(1)
print (L)
