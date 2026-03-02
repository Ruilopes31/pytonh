nume1= float(input("digite seu primeiro numero:"))
nume2= float(input("digite seu segundo numero:"))
operacao = input("escolha a operacao (+,-.*,/):")

if operacao == "+":
    resultado = nume1 + nume2
    print(f"resultado:{nume1}+{nume2} ={resultado}")

elif operacao == "-":
    resultado = nume1 - nume2
    print(f"resultado:{nume1}-{nume2} ={resultado}")

if operacao == "*":
    resultado = nume1 * nume2
    print(f"resultado:{nume1}*{nume2} ={resultado}")

if operacao == "/":
    if nume2 !=0:
        resultado = nume1 / nume2
        print(f"resultado:{nume1}/{nume2} ={resultado}")
    else:
        print("erro: nao é possivel  dividir por zero ")
