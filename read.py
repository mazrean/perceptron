import csv
import datetime as dt
import plot

def strToDate(strDate):
    time = dt.datetime.strptime(strDate, '%Y/%m/%d')
    start = dt.date(time.year, 1, 1)
    date = dt.date(time.year, time.month, time.day)
    return (date - start).days + 1

def read():
    f = open('./data/data.csv', encoding='shift_jis')
    reader = csv.reader(f)
    reader = [row for row in reader][5:]
    data = list(map(lambda x: [strToDate(x[0]), float(x[5]), float(x[8]), float(x[11]), x[1]=='0'], reader))
    return data

data = read()
print(data[0:5])
red = list(filter(lambda x: x[4], data))
blue = list(filter(lambda x: not x[4], data))
plot.plot(list(map(lambda x: x[1], red)), list(map(lambda x: x[2], red)), list(map(lambda x: x[3], red)), list(map(lambda x: x[1], blue)), list(map(lambda x: x[2], blue)), list(map(lambda x: x[3], blue)))