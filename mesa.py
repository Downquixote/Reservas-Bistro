class Cadastro:
    def __init__(self, nome, mesa):
        self.nome = nome
        self.mesa = mesa

ListaNome = list()
ListaMesa = list()
saida = False

while saida == False:
    print("-" * 80)
    print("{:^80}".format("CADASTRO DE MESAS - BISTRÔ'S VINSMOKE"))
    print("-" * 80)

    NomeCliente = Cadastro(nome="", mesa="")
    NomeCliente.nome = str(input("Nome: ")).upper().strip()
    ListaNome.append(NomeCliente.nome)

    NumeroMesa = Cadastro(nome="", mesa="")
    NumeroMesa.mesa = int(input("Nº Mesa: "))

    if NumeroMesa.mesa > 20:
        print("Nosso bistrô tem apenas 20 mesas para reservas.")
        ListaNome.pop()
    elif NumeroMesa.mesa not in ListaMesa:
        ListaMesa.append(NumeroMesa.mesa)
        ListaMesa.sort()
        print("Mesa reservada com sucesso.")
    else:
        print("Esta Mesa já foi reservada por outro cliente.")
        ListaNome.pop()
    try:
        visualizar = int(input("Para visualizar mesas preenchidas digite 1, se não, digite qualquer número: "))
        if visualizar == 1:
            print("-" * 80)
            print("Mesas reservadas:")
            for v in range(len(ListaMesa)):
                print(ListaMesa[v], end=" ")
            print("\n")
    except:
        print("Preste mais atenção.")
        try:
            saida = int(input("Se deseja sair digite 1, se não, digite qualquer número: "))
            if saida == 1:
                saida = True
            else:
                saida = False
                continue
        except:
            print("Preste mais atenção.")
        else:
            continue
    else:
        try:
            saida = int(input("Se deseja sair digite 1, se não, digite qualquer número: "))
            if saida == 1:
                saida = True
            else:
                saida = False
                continue
        except:
            print("Preste mais atenção.")
        else:
            continue

print("-" * 80)
print("Obrigado por utilizar nosso sistema de reserva de mesas.")
