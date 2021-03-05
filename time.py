import time
t1=time.time()
def numbers(max):
    for x in range(0,max):
        print(x)
t2=time.time()

numbers(1000)
print('all time %s' %(t2-t1))