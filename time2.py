import time
print(time.asctime())
#print(time.localtime())
t=time.localtime()
year=t[0]
month=t[1]
print(year)
print(month)

for x in range(1,10):
    print(x)
    time.sleep(1)