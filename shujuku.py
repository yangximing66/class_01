# -*- coding: utf-8 -*-
# @Time      :2019/7/16 0016 18:14
# @Author    :lebo_ximing
# @Email     :1228902900@qq.com
# @File      : manage.py.py

from pymysql import*

connect= connect(host="127.0.0.1", port=3306, database="test", user="root", password="123456", charset="utf8")

 # 通过cursor创建游标
cursor = connect.cursor()
  # 创建sql 语句
sql = "select * from ximing"
  # 执行sql语句
cursor.execute(sql)
  # 获取所有记录列表
results = cursor.fetchone()
print(results)
# for data in results:      # 打印结果      print(data)
# except  Exception :print("查询失败")
