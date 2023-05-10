import datetime

a = datetime.datetime.now()

# b = datetime.datetime.strptime("2001년 2월 12일 0요일", "%Y년 %m월 %d일 %B요일")

c = datetime.date(2001, 2, 12)

str_datetime = '2021-04-08 21:31:48'
currdate = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

print(a.strftime("%Y %m %d %H %M %S %B %A"))

print(a.strftime("%Y-%m-%d"))

# print(b)

print(c)

print(a)