
fibo_dic = {}
def fibo(n):

    if n in fibo_dic:
        return fibo_dic[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibo(n - 1) + fibo(n - 2)


    fibo_dic[n] = value
    return value


for i in range(1, 100):
    print(i, ": ", fibo(i))
