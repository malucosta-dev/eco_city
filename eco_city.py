import datetime

dados_cadastrais = {
}

def cadastrar(estacao: str, codigo: str, bairro: str, volume: float):
    erro = False #Sempre que acontecer um erro, a variável "erro" é alterada para True, permitindo que todas as mensagens de erro aconteçam

    for i in dados_cadastrais.keys(): #checando se alguma key já foi cadastrada
        if i == estacao:
            print(f"{estacao} já cadastrada! Por favor, insira outro nome.")
            return 0 #Caso já tenha um cadastro de mesmo nome, o return impede que ele seja modificado posteriormente
    
    if len(codigo) != 5: #Verificando regras de negócio
        erro = True 
        print("Código inválido. É preciso, exatamente, 5 números.")

    if codigo.isnumeric() == False: #Verificando se input é um número
        erro = True
        print("Código inválido. Por favor, digite um número.")

    if codigo == "":
        erro = True
        print("Código inválido. Por favor, digite um número.")

    if type(bairro) != str:  #Verificando se input é uma str
        erro = True
        print("Bairro inválido. Por favor, digite uma palavra.")

    if bairro == "":
            erro = True
            print("Bairro inválido. Por favor, digite um bairro.")

    try:
        volume = float(volume)
        if volume < 0: #Verificando se o input é negativo
            erro = True
            print("Volume inválido. Por favor, digite uma número maior que zero.")
        if volume > 400: #Verificando limite de volume de descarte
            erro = True
            print(f"Limite de volume de descarte atingido, valor máximo permitido: 300kg.")
    except ValueError:
        erro = True
        print("Volume inválido. Por favor, digite uma número inteiro ou decimal.")

    erro = verificar_volume(volume)

    if erro == True:
        return 0

    dados_cadastrais[estacao] = {}
    dados_cadastrais[estacao]['codigo'] = codigo
    dados_cadastrais[estacao]['bairro'] = bairro
    dados_cadastrais[estacao]['volume'] = volume
    dados_cadastrais[estacao]['cacambas'] = {}
    for i in range(4):
        dados_cadastrais[estacao]['cacambas'][f'{i + 1}'] = {}
        dados_cadastrais[estacao]['cacambas'][f'{i + 1}']['capacidade'] = 100
        dados_cadastrais[estacao]['cacambas'][f'{i + 1}']['volume_cacamba'] = 0
        dados_cadastrais[estacao]['cacambas'][f'{i + 1}']['temperatura'] = 0
        dados_cadastrais[estacao]['cacambas'][f'{i + 1}']['porcentagem'] = dados_cadastrais[estacao]['cacambas'][f'{i + 1}']['capacidade']*(dados_cadastrais[estacao]['cacambas'][f'{i + 1}']['volume_cacamba'])/100
    dados_cadastrais[estacao]['cacambas']['1']['volume_cacamba'] = volume 
    dados_cadastrais[estacao]['historico'] = {}

    return 1 #Toda função retorna 1. Isso acontece para verificar se a função ocorreu ou não. Se não retornar 1, isso significa que a função não chegou ao final

def verificar_todas_estacoes():
    if len(dados_cadastrais) == 0:
        print("Nenhuma estação cadastrada")
    for i in dados_cadastrais.keys():
        print(f"{i}:")
        print(f"    -Código: {dados_cadastrais[i]['codigo']}")
        print(f"    -Bairro: {dados_cadastrais[i]['bairro']}")
        print(f"    -Volume total: {dados_cadastrais[i]['volume']}kg\n")
        for j in range(4):
            print(f"    -Caçamba {j + 1}:")
            print(f"        .Capacidade máxima: {dados_cadastrais[i]['cacambas'][f'{j + 1}']['capacidade']}kg:")
            print(f"        .Volume atual: {dados_cadastrais[i]['cacambas'][f'{j + 1}']['volume_cacamba']}kg:")
            print(f"        .Temperatura: {dados_cadastrais[i]['cacambas'][f'{j + 1}']['temperatura']}º\n:")
            print(f"        .Porcentagem: {dados_cadastrais[i]['cacambas'][f'{j+1}']['volume_cacamba'] / (dados_cadastrais[i]['cacambas'][f'{j + 1}']['capacidade']) * 100} %:")

    return 1

def verificar_estacao_especifica(estacao:str):
    try:
        dados_cadastrais[estacao] #Checa se a estação existe

        print(f"{estacao}:")
        print(f"    -Código: {dados_cadastrais[estacao]['codigo']}")
        print(f"    -Bairro: {dados_cadastrais[estacao]['bairro']}")
        print(f"    -Volume inicial: {dados_cadastrais[estacao]['volume']}\n")
        for j in range(4):
            print(f"    -Caçamba {j + 1}:")
            print(f"        .Capacidade máxima: {dados_cadastrais[estacao]['cacambas'][f'{j + 1}']['capacidade']}kg:")
            print(f"        .Volume atual: {dados_cadastrais[estacao]['cacambas'][f'{j + 1}']['volume_cacamba']}kg:")
            print(f"        .Temperatura: {dados_cadastrais[estacao]['cacambas'][f'{j + 1}']['temperatura']}º\n:")
            print(f"        .Porcentagem: {dados_cadastrais[estacao]['cacambas'][f'{j+1}']['volume_cacamba'] / (dados_cadastrais[estacao]['cacambas'][f'{j + 1}']['capacidade']) * 100} %:")
    except KeyError:
        print("Estação inválida. Tente novamente.")
    return 1

def creditos_carbono(estacao: str):
    try:
        if dados_cadastrais[estacao]['volume'] <= 50:
            print(f'Desempenho ecológico da {estacao}: Baixo impacto')
        elif dados_cadastrais[estacao]['volume'] > 50 and dados_cadastrais[estacao]['volume'] <= 100:
            print(f'Desempenho ecológico da {estacao}: Sustentabilidade moderada')
        else:
            print(f'Desempenho ecológico da {estacao}: Polo verde avançado')
    except KeyError: #Pega erros de Keys inválidas ou, no nosso caso, se ela existe ou não
        print("Estação inválida. Tente novamente.")
    return 1

#====================
#Catarina
def historico_dia(estacao: str):
    
    return 1

def historico_mes():
    
    return 1

def porcentagem_cacamba(estacao:str):
    try:
        if estacao not in dados_cadastrais[estacao]['cacambas']:
            for cacamba ,dicionario in dados_cadastrais[estacao]['cacambas'].items():
                volume_ocu = dicionario ['volume_cacamba']
                porcentagem = (dicionario ['volume_cacamba'] / 100 ) * 100
                print(f"Cacamba {cacamba}: {porcentagem}% cheia")
    except KeyError:
        print('Estação não cadastrada! Escolha outra estação')
    print(dados_cadastrais)
    return 1

    # escolher a estação
    # enumerar a caçamba
    # ver qual é o valume ocupado de cada caçamba por descarte
    # e calcular a porcentagem da caçamba utilizando a capacidade máx 100
 
#====================
#Lucas
def fazer_descarte(estacao: str, cacamba:str, descarte:float):
    try:
        descarte = float(descarte)
    except ValueError:
        print('Peso do material descartado inválido! Por favor, digite um número.')
        return 0

    if descarte < 0:
        print("Peso do material descartado inválido! Por favor, digite um número maior que 0.")
        return 0

    if type(estacao) != str or estacao == "":
        print('Estação inválida. Por favor, digite uma palavra.')
        return 0

    if not cacamba.isnumeric():
        print("Caçamba inválida! Por favor, digite um número")
        return 0

    if int(cacamba) > 4 or int(cacamba) < 0:
        print('Caçamba inválida. Existem apenas as caçambas 1, 2, 3 e 4.')
        return 0

    data_hora = datetime.datetime.now()

    try:
        dados_cadastrais[estacao]['volume'] = dados_cadastrais[estacao]['volume'] + descarte
        dados_cadastrais[estacao]['cacambas'][cacamba]['volume_cacamba'] = dados_cadastrais[estacao]['cacambas'][cacamba]['volume_cacamba'] + descarte
        dados_cadastrais[estacao]['cacambas'][cacamba]['temperatura'] = dados_cadastrais[estacao]['cacambas'][cacamba]['volume_cacamba'] * 40 / 100
        if (f'dia {data_hora.day}') not in dados_cadastrais[estacao]['historico']:   #checando se dia já foi cadastrado no histórico
            dados_cadastrais[estacao]['historico'][f'dia {data_hora.day}'] = {}    #Se a checagem não for feita, o dicionário sempre vai sobrescrever
        dados_cadastrais[estacao]['historico'][f'dia {data_hora.day}'][f'{data_hora.time()}'] = f'descartados {descarte}kg na caçamba {cacamba}'
    except KeyError:
        print('Estação não cadastrada! Escolha outra estação')

    print(dados_cadastrais)

    return 1

#====================
#Luiza
def volume_cacambas(estacao:str):
    try:
        if dados_cadastrais <= 30:
            print("Volume de ocupação da caçamba: Baixo")
        elif porcentagem_cacamba >30 and porcentagem_cacamba <=60:
            print("Volume de ocupação da caçamba: Moderado")
        elif porcentagem_cacamba >60 and porcentagem_cacamba <= 90:
            print("Volume de ocupação da caçamba: Alto")
        else:
            print(f"Atenção: Volume da caçamba perigosamente alto. Restringir descarte.")
    except KeyError:
        return 1

#====================

def main():
    while True:
        print("Sistema EcoCity:")
        resposta = input("O que você quer fazer?\n0. Sair\n1. Cadastrar estação\n2. Verificar dados\n3. Cadastrar descarte\nR: ")
        match resposta:
            case "0":
                return
            
            case "1":
                while True:
                    print("================")
                    print("Cadastro de estação:")

                    estacao = input("Nome da estação: ")
                    codigo = input("Código identificador: ")
                    bairro = input("Bairro correspondente: ")
                    volume = input("Volume de resíduos(kg): ")

                    if cadastrar(estacao, codigo, bairro, volume) == 1:
                        print("Estação cadastrada com sucesso!\n================")
                        break
                    if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                        print("================")
                        break

            case "2":
                while True:
                    print("================")
                    print("Verificação de dados:")

                    resposta = input("O que quer verificar?\n0. Sair\n1. Dados de todas as estações\n2. Dados de uma estação específica\n3. Créditos de carbono de uma estação\n4. Porcentagem\nR: ")
                    print("================")

                    match resposta:
                        case "0":
                            break
                        case "1":
                            verificar_todas_estacoes()
                        case "2":
                            estacao = input('Qual estação você quer verificar?\nR: ')

                            if verificar_estacao_especifica(estacao) == 1:
                                break
                            if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                                print("================")
                                break
                        case "3":
                            estacao = input('Qual estação você quer verificar?\nR: ')

                            if creditos_carbono(estacao) == 1:
                                break
                            if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                                print("================")
                                break
                        case "4":
                            estacao = input('Qual estação você quer verificar?\nR: ')

                            if porcentagem_cacamba(estacao) == 1:
                                break
                            if input("Tentar novamente? \n1. Sim\n2. Não\nR: ") == "2":
                                print("================")
                                break

            case "3":
                while True:
                    print("================")
                    print("Cadastrar descarte:")

                    estacao = input("Em qual estação será feito o descarte?\nR:")
                    cacamba = input("Em qual caçamba será feito o descarte?\nR:")
                    descarte = input("Qual o peso do material descartado?\nR:")

                    if fazer_descarte(estacao, cacamba, descarte) == 1:
                        print("Estação cadastrada com sucesso!\n================")
                        break
                    if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                        print("================")
                        break

main()