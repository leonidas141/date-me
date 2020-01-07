#!/usr/bin/python3
# coding: utf-8

'''
@Author  : Wang Siqiang
@Contact : wang_siqiang@163.com
@File    : ${NAME}.py
@Time    : ${DATE} ${TIME}
'''
import heapq
import numpy as np
import random
"""

rules

    1. 男女各100人；

    2. 编号为1~100，但他们不知道数字最大的是100，最小的是1；

    3. 编号贴在背后，自己只能看见别人的编号；
        每个 person 可以观测对方的数值，观测可以加噪声

    4. 大家可以说任何话，但不能把对方的编号告诉对方。
        每个 person 无法直接获得自己的数值，但是隐含了可以估计

    5. 实验要求：大家去找一个异性配对，只要两人加起来的数字越大，得到的奖品越高，奖金归他们所有；

    6. 配对时间有限，设定4轮，固定后不可更改。

p.s.：

    1. 每人一轮可以选10个，此处首先为随机抽取

    2. 每人可以知道自己被谁选择，以及该人是否可选这一情况。作为记忆，整场留存。

"""



class person(object):
    value = 0
    education = 0
    wealth = 0
    age = 0
    weights = np.array([1.0,1.0,1.0,1.0])
    number = 0
    idealSelect = -1
    estimation = 0
    followers = []
    occupied = False
    selection = []
    mate = -1
    def __init__(self,number):
        self.value = self.calculate
        self.number = number

    def calculate(self, another):
        parameter = np.array([another.value, 
                              another.education,
                              another.wealth,
                              another.age])
        return np.dot(parameter,self.weights)

    def estimate(self):
        try:
            tire = heapq.nlargest(3, self.followers[-1])
            self.estimation = tire/len(tire)
        except Exception:
            if len(self.followers)>0:
                self.estimation = max(self.followers[-1])
            else:
                self.estimation = -1

    def select(self, anothers, maxSelect):
        score = self.calculate(anothers)
        print(score)


class woman(person):
    height = 1.6
    weights = np.ones(6)

class man(person):
    height = 1.7
    weights = np.ones(5)

class test(object):
    men = []
    women = []

    def __init__(self, times=4, num=100, maxSelect=3,maxCheck=10):
        for i in range(num):
            self.num = num
            self.men.append(man(i))
            self.women.append(woman(i))
            self.men[i].value = i
            self.women[i].value = i
            self.times = times
            self.maxCheck = maxCheck
            self.maxSelect = maxSelect
    
    def update(self):
        for man in self.men:
            if man.occupied is True:
                continue
            follower = []
            for select in man.selection:
                if man.number in self.women[select].selection and self.women[select].occupied is False:
                    man.mate = select
                    man.occupied = True
                    self.women[select].mate = man.number
                    self.women[select].occupied = True
        for woman in self.women:
            if woman.occupied is True:
                continue
            for select in woman.selection:
                if woman.number in self.men[select].selection and self.men[select].occupied is False:
                    woman.mate = select
                    woman.occupied = True
                    self.men[select].mate = woman.number
                    self.men[select].occupied = True

    def select(self, me, gender):
        """
        strategy 1:     max n
        strategy 2:     nearest n
        strategy 2.1:   nearest & bigger n
        """
        # strategy 1
        backList = []
        selection = []
        # while len(backList) <= self.maxSelect
        for _ in range(self.maxCheck):
            j = random.randint(0,self.num-1)
            if gender == 'female':
                if self.women[j].occupied is False:
                    backList.append(j)
            elif gender == 'male':
                if self.men[j].occupied is False:
                    backList.append(j)
            else:
                print('wrong gender', gender)
                exit(-1)
        try:
            selection = heapq.nlargest(self.maxSelect, backList)
        except Exception as e:
            selection = backList
        return selection

    def run(self):
        for it in range(self.times):
            print('round ',it)
            for man in self.men:
                man.selection = self.select(man, 'female')
            for woman in self.women:
                woman.selection = self.select(woman, 'male')
            self.update()
            for i in range(self.num):
                self.men[i].estimate()
                self.women[i].estimate()
        for i in range(self.num):
            if self.men[i].occupied is True:
                print(self.men[i].value, self.women[self.men[i].mate].value, sep=',', end=',')
                print(self.men[i].value + self.women[self.men[i].mate].value)
                # print(self.men[i].estimation)
                print('',end='')
            else:
                continue
                print(self.men[i].value)

if __name__ == "__main__":
    Test = test(times=5,maxSelect=2)
    Test.run()

