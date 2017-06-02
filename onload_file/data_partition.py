# -*- coding: UTF-8 -*-
import csv
import numpy as np
import pandas as pd
# csvfile = file('Atest_1.csv', 'wb')
# writer = csv.writer(csvfile)
# writer.writerows(data)
while True:
    num=0
    with open('train.txt') as f:
        while True:
            if num%500==0:
                csvfile = file(str(num/500+1)+'.csv', 'wb')

            file1=f.readline()

            writer = csv.writer(csvfile)
            writer.writerow([file1])
            print('num=%s'% num)
            num=num+1
            if num%500==0:
                csvfile.close()
            if num==10000:
                break
        f.close()
        break