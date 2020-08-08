import csv
import datetime as dt

def strToDate(strDate):
    time = dt.datetime.strptime(strDate, '%Y/%m/%d')
    start = dt.date(time.year, 1, 1)
    date = dt.date(time.year, time.month, time.day)
    return (date - start).days + 1

def read():
    f = open('./data/data.csv', encoding='shift_jis')
    reader = csv.reader(f)
    reader = [row for row in reader][6:]
    data = list(map(lambda x: [strToDate(x[0]), float(x[1]), float(x[4]), int(x[7]), x[10]==0], reader))
    return data

print(read()[365:370])