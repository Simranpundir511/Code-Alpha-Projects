def fibonacci(n):
    print("This is a fibbonacci generator")
    a=0
    b=1
    if n==1:
      print(a)
    elif n==2:
      print(a,b)
    else:
       print(a,b,end=" ")
       for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
n=int(input("Enter the number of terms you want to print:"))
fibonacci(n)