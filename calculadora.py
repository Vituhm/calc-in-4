n1=(int(input("Informe um número: ")))
n2=(int(input("Informe um número: ")))

print("Escolha a operação a ser realizada: ")
print("1 = Adição (+)")
print("2 = Subtração (-)")
print("3 = Multiplicação (*)")

op=(int(input("Opção: ")))

if op == 1:
    print("Resultado: ", n1, "+", n2, "=", n1 + n2)
elif op == 2:
    print("Resultado: ", n1, "-", n2, "=", n1 - n2)
elif op == 3:
    print("Resultado: ", n1, "*", n2, "=", n1 * n2)
elif op == 4:
    if n2 == 0:
        print("Não é possível dividir por Zero.")
    else:
        print("Resultado: ", n1, "/", n2, "=", n1 / n2)
else:
    print("Opção inválida")