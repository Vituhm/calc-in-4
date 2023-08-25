n1=(int(input("Informe um número: ")))
n2=(int(input("Informe um número: ")))

print("Escolha a operação a ser realizada: ")
print("1 = Adição (+)")
print("2 = Subtração (-)")

op=(int(input("Opção: ")))

if op == 1:
    print("Resultado: ", n1, "+", n2, "=", n1 + n2)
if op == 2:
    print("Resultado: ", n1, "-", n2, "=", n1 - n2)