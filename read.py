import csv
from datetime import datetime as dt

def strToDate(strDate):
    time = dt.strptime(strDate, '%Y/%m/%d')
    date = dt.date(time)
    return date

def read():
    f = open('./data/data.csv', encoding='shift_jis')
    reader = csv.reader(f)
    reader = [row for row in reader][6:]
    data = list(map(lambda x: [strToDate(x[0]), float(x[1]), float(x[4]), int(x[7]), x[10]==0], reader))
    return data

print(read()[0:5])