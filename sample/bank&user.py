# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:28:53 2018

@author: Administrator
"""
class Bank(object):
    
    # 存储所有开户信息
    __userInfo = []
    
    # 用户开户
    def resigterUser(self):
        return 
    # 获取所有开户信息
    def getUserInfo(self):
        return self.__usersInfo
    
    def getUserCount(self):
        return len(self.__userInfo)
    
class User(object):
    
    # 卡号
    __bankCardNumber = ""
    # 密码
    __password = ""
    # 用户名
    __userName = ""
    # 余额
    __balance = 0
    
    def __init__(self, cardNumber, password, userName, balance):
        self.__bankCardNumber = cardNumber
        self.__password = password
        self.__userName = userName
        self.__balance = balance
        
    def queryMoney(self, cardNumber, password, money):
        if self.__bankCardNumber == cardNumber and self.__password == password:
            if money <= 0 :
                return "取的钱数不能为负"
            elif money > self.__balance:
                return "您的余额不足, 余额为：" + str(self.__balance)
            else:
                self.__balance -= money
                print("取钱成功！")
                return self.__balance
    
    def getBankCardNumber(self):
        return self.__bankCardNumber
    
    def getPassword(self):
        return self.__password
    
    def getUserName(self):
        return self.__userName
    
    def getBalance(self):
        return self.__balance

user1 = User("1234", "123", "geyang", 1000)
print(user1.getBalance())
balance = user1.queryMoney("1234", "123", -50)