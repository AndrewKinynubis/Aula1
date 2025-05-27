#Delta
#Entrada
a = float(input("a =  "))
b = float(input("b =  "))
c = float(input("c =  "))

#Processamento:
Delta = b**2 - 4*a*c
Value = Delta

#Saída
#Valor de Delta
if Delta > 0: 
    print("A equação tem duas raízes reais")
elif Delta == 0:
    print("A equação tem uma raiz real")
else:
    print("A equação não possui raízes reais")

print(Value)