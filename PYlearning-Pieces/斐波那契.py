import sys
def fib(n):
    a,b,count=0,1,0
    while True:
        if count<=n:
            yield a #
            a,b=b,a+b
            count+=1
        else:
            return
f=fib(10)
while True:
    try:
        print(next(f),end=' ')
    except StopIteration:
        print('\nThe interation has stopped.')
        sys.exit()
