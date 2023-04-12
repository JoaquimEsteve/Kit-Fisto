print("Digite o número.")
a=float(input())
print("Qual a operação desejada?")
c=input()

c=c.lower()

print("Digite um segundo número.")
b=float(input())
print("Resultado:")

if c=="*":
    print(a*b)

elif c=="/":
    print(a/b)

elif c=="+":
    print(a+b)

elif c=="-":
    print(a-b)

elif c=="potência":
    print(a**b)

elif c=="raiz quadrada":
    print(a**0.5)

elif c=="1/x":
    print(1/a)
   