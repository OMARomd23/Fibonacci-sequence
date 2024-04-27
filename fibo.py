a = 0
b = 1
c=0
n=0
def fibo(k):
    global a
    global b
    global c
    print(c+2,"#  ",a+b)
    b= a+b
    a =b-a
    c+=1
    if c == k:
        exit()
    fibo(k)
k=int(input("Enter a number: "))
print(c,"#  ",a)
print(c+1,"#  ",b)
fibo(k)
