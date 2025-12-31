num=3
factorial=1
if num<0:
    print("The factorial does not for neagative numners")
else:
    for i in range(1,num+1):
        factorial=factorial*i

print(f"The factorial number{num}is :",factorial)