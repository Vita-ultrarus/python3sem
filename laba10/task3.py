import time, random
import threading

start = time.time()
def thread_job(a,b,c):
    k=sum(a)
    b[c]=k
    return

a=[2,5,89,0,9876,-98,998]
print(sum(a))
N=7
m=0
if N!=1:
    n=len(a)//N
else:
    n=len(a)-1
b=[0]*(N+1)
i=0
threads=[]
while n!=m:
    threads.append(threading.Thread(target=thread_job,args=(a[m:n],b,i)))
    i += 1
    m = n
    if n < len(a)-len(a)//N - 1:
        n += len(a) // N + 1
    else:
        n = len(a) - 1


v = [a[-1]]
threads.append(threading.Thread(target=thread_job, args=(v, b, i)))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
k=sum(b)
print(k)



print(time.time() - start)