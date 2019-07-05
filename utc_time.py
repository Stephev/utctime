#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/7/2 0002 
# @Author  : Stephev
# @Site    : 
# @File    : utc_time.py
# @Software:

import csv
from datetime import datetime, timedelta
from pprint import pprint
import os

path = 'C:\\Users\\Administrator\\Desktop\\袋鼠云\\车满满慢日志\\'

for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    rows = []
    f = open(file_path)
    f_csv = csv.DictReader(f)

    for row in f_csv:
            a = row['start_time']
            b = row['check_time']
            date = datetime.strptime(a.split('+')[0], '%Y-%m-%dT%H:%M:%S')+ timedelta(hours=8)
            date1 = datetime.strptime(b.split('+')[0], '%Y-%m-%dT%H:%M:%S') + timedelta(hours=8)
            row['start_time'] = date.strftime('%Y-%m-%d %H:%M:%S')
            row['check_time'] = date1.strftime('%Y-%m-%d %H:%M:%S')
            rows.append(row)

    pprint(rows)
    headers = ['user_id','instance_name','host_address','db_name','sql_text','query_times','lock_times','parse_row_counts','return_row_counts','start_time','check_time']
    with open(file_path,'w',newline="\n") as e:
        e_csv = csv.DictWriter(e, headers)
        e_csv.writeheader()
        e_csv.writerows(rows)
