print("Digite o número.")
a=float(input())
print("Qual a operação desejada?")
c=input()

c=c.lower()

if c=="ao quadrado":
    print(a**2)
    quit()

if c=="raiz quadrada":
    print(a**0.5)
    quit()

if c=="1/x":
    print(1/a)
    quit()

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