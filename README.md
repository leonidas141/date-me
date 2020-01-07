# Date Me

[TOC]

## English Version

### Purpose

This is a social experiment program to test and evaluate the game named *The Pairing Game*.

### Parameters

- num:L, L women and L men in one simulation
- times:N, Simulation runs for N rounds
- maxSelect:M, Each person can express himself or herself for M time in a round
- maxCheck:K, Each person can check K person in one round

### Usage

Use `python` to run this program.

``` bash
python date.py
```

### TODO

1. Add different selection method
   1. bigest one
   2. nearest to self estimation
   3. bigger and nearest to self estimation
2. Research the influence of who express first
3. Add more parameter like education, salary, age, height, etc.

## 中文版

### 目的

本程序用于模拟*配对游戏*。

### 参数

- 人数：L，每次仿真中包含男女各L人；
- 次数：N，每次仿真中进行N轮选择；
- 最大选择数：M，每轮中每个人最多向M个人表白；
- 最大查看数：K，每轮每个人最多获取K个人的信息。

### Usage

使用`python`运行本程序

``` bash
python date.py
```

### 下一步

1. 加入不同的选择方法
   1. 得分最高
   2. 离自己估计值最近
   3. 大于自己且离自己最近
2. 研究男女先表白之间的区别
3. 加入更多参数，例如教育、薪资、年龄、身高等等
