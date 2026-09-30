import datetime

dados_cadastrais = {
}

def cadastrar(estacao: str, codigo: str, bairro: str, volume: float):
    erro = 1 #Sempre que acontecer um erro, a variável "erro" é alterada para True, permitindo que todas as mensagens de erro aconteçam

    for i in dados_cadastrais.keys(): #checando se alguma key já foi cadastrada
        if i == estacao:
            print(f"{estacao} já cadastrada! Por favor, insira outro nome.")
            return 0 #Caso já tenha um cadastro de mesmo nome, o return impede que ele seja modificado posteriormente
    
    if len(codigo) != 5: #Verificando regras de negócio
        erro = 0 
        print("Código inválido. É preciso, exatamente, 5 números.")

    if codigo.isnumeric() == False: #Verificando se input é um número
        erro = 0
        print("Código inválido. Por favor, digite um número.")

    if codigo == "":
        erro = 0
        print("Código inválido. Por favor, digite um número.")

    if type(bairro) != str:  #Verificando se input é uma str
        erro = 0
        print("Bairro inválido. Por favor, digite uma palavra.")

    if bairro == "":
            erro = 0
            print("Bairro inválido. Por favor, digite um bairro.")

    try:
        volume = float(volume)
        if volume < 0: #Verificando se o input é negativo
            erro = 0
            print("Volume inválido. Por favor, digite uma número maior que zero.")
    except ValueError:
        erro = 0
        print("Volume inválido. Por favor, digite uma número inteiro ou decimal.")

    if erro == 0:
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
    dados_cadastrais[estacao]['cacambas']['1']['volume_cacamba'] = volume
    dados_cadastrais[estacao]['historico'] = {}

    if verificar_volume(estacao, "1") == 0:
        print("Volume de descarte excedido. Estação não cadastrada.")
        del dados_cadastrais[estacao]
        return 0

    return 1 #Toda função retorna 1. Isso acontece para verificar se a função ocorreu ou não. Se não retornar 1, isso significa que a função não chegou ao final

def verificar_todas_estacoes(): #Adicionar exemplos
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
            print(f"        .Temperatura: {dados_cadastrais[i]['cacambas'][f'{j + 1}']['temperatura']}º")
            verificar_volume(i, f'{j+1}')
    return 1

def verificar_estacao_especifica(estacao:str):
    try:
        dados_cadastrais[estacao] #Checa se a estação existe

        print(f"{estacao}:")
        print(f"    -Código: {dados_cadastrais[estacao]['codigo']}")
        print(f"    -Bairro: {dados_cadastrais[estacao]['bairro']}")
        print(f"    -Volume total: {dados_cadastrais[estacao]['volume']}\n") #testar
        for j in range(4):
            print(f"    -Caçamba {j + 1}:")
            print(f"        .Capacidade máxima: {dados_cadastrais[estacao]['cacambas'][f'{j + 1}']['capacidade']}kg:")
            print(f"        .Volume atual: {dados_cadastrais[estacao]['cacambas'][f'{j + 1}']['volume_cacamba']}kg:")
            print(f"        .Temperatura: {dados_cadastrais[estacao]['cacambas'][f'{j + 1}']['temperatura']}º:")
            verificar_volume(estacao, f'{j+1}')
    except KeyError:
        print("Estação inválida. Tente novamente.")
    return 1

def creditos_carbono(estacao: str): #testar
    try:
        if dados_cadastrais[estacao]['volume'] <= 150:
            print(f'Desempenho ecológico da {estacao}: Baixo impacto')
        elif dados_cadastrais[estacao]['volume'] > 150 and dados_cadastrais[estacao]['volume'] <= 360:
            print(f'Desempenho ecológico da {estacao}: Sustentabilidade moderada')
        else:
            print(f'Desempenho ecológico da {estacao}: Polo verde avançado')
    except KeyError: #Pega erros de Keys inválidas ou, no nosso caso, se ela existe ou não
        print("Estação inválida. Tente novamente.")
    return 1

#====================
#Catarina
def historico_dia(estacao: str, dia:str, mes:str): #Fazer case
    if estacao not in dados_cadastrais:
        print("Estação não cadastrada!")
        return 0

    if dia.isnumeric() == False:
        print("Dia inválido! Digite um número.")
        return 0

    if mes.isnumeric() == False:
        print("Mês inválido! Digite um número.")
        return 0

    if f'{dia}/{mes}' not in dados_cadastrais[estacao]['historico'].keys():
        print(f"Nenhum dado encontrado para o dia {dia}/{mes}.")
        return 0

    print(f"Histórico do dia {dia}/{mes} da estação {estacao}")
    for hora, descarte in dados_cadastrais[estacao]['historico'][f'{dia}/{mes}'].items():
        print(f"{hora[0:5]}: {descarte}")

    return 1

def historico_mes(estacao: str, mes:str): #Fazer case 
    if estacao not in dados_cadastrais:
        print("Estação não cadastrada!")
        return 0

    if mes.isnumeric() == False:
        print("Mês inválido! Digite um número.")
        return 0


    print(f"Histórico do mês {mes} da estação {estacao}")
    for diames in dados_cadastrais[estacao]['historico'].keys():

        dia, mes_historico = diames.split("/")

        if mes_historico == mes:
            for hora, descarte in dados_cadastrais[estacao]['historico'][diames].items():
                print(f"Dia {dia} às {hora[0:5]}: {descarte}")
        else:
            print(f"Nenhum histórico para o mês {mes}.")
            return 0

    return 1

def historico_ultimos_10(estacao: str):
    if estacao not in dados_cadastrais:
        print("Estação não cadastrada!")
        return 0

    if len(dados_cadastrais[estacao]['historico']) == 0:
        print("Nenhum descarte feito")
        return 0

    print(f"Histórico dos últimos 10 dias da estação {estacao}")
    for dia in list(dados_cadastrais[estacao]['historico'].keys())[-10:]:
        for hora, descarte in dados_cadastrais[estacao]['historico'][dia].items():
            print(f"{dia}: {descarte} às {hora[0:5]}")

    return 1

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
        if verificar_volume(estacao, cacamba) == 0:
            dados_cadastrais[estacao]['volume'] = dados_cadastrais[estacao]['volume'] - descarte
            dados_cadastrais[estacao]['cacambas'][cacamba]['volume_cacamba'] = dados_cadastrais[estacao]['cacambas'][cacamba]['volume_cacamba'] - descarte
            print(f'Descarte de {descarte}kg não autorizado. Por favor, refaça o descarte.')
            return  0
        dados_cadastrais[estacao]['cacambas'][cacamba]['temperatura'] = dados_cadastrais[estacao]['cacambas'][cacamba]['volume_cacamba'] * 40 / 100
        if (f'{data_hora.day}/{data_hora.month}') not in dados_cadastrais[estacao]['historico']:   #checando se dia já foi cadastrado no histórico
            dados_cadastrais[estacao]['historico'][f'{data_hora.day}/{data_hora.month}'] = {}    #Se a checagem não for feita, o dicionário sempre vai sobrescrever
        dados_cadastrais[estacao]['historico'][f'{data_hora.day}/{data_hora.month}'][f'{data_hora.time()}'] = f'{descarte}kg na caçamba {cacamba}'
    except KeyError:
        print('Estação não cadastrada! Escolha outra estação')

    return 1

#====================
#Luiza

def calcular_porcentagem(estacao:str, cacamba:str):
        
        capacidade = dados_cadastrais[estacao]['cacambas'][cacamba]['capacidade']
        volume_cacamba = dados_cadastrais[estacao]['cacambas'][cacamba]['volume_cacamba']

        porcentagem = volume_cacamba/capacidade*100
    
        return porcentagem 

def verificar_volume(estacao:str, cacamba:str):
    try:

        porcentagem = calcular_porcentagem(estacao, cacamba)

        if porcentagem == 0:
            pass 
        elif porcentagem >=1 and porcentagem <31:
            print(f"Volume de ocupação da caçamba {cacamba}: Baixo")
        elif porcentagem >=30 and porcentagem <61:
            print(f"Volume de ocupação da caçamba {cacamba}: Moderado")
        elif porcentagem >=60 and porcentagem <91:
            print(f"Volume de ocupação da caçamba {cacamba}: Alto")
        else:
            print(f"Atenção: Volume da caçamba {cacamba} perigosamente alto.")
            return 0
        
    except KeyError:
        print("Estação ou caçamba inválida! Tente novamente.")
        return 0 
    
    return 1

def indicador_desempenho(desempenho:str): #Filtra estações por categoria de desempenho
    try: 

        reg=[]
        bom=[]
        mt_bom=[]

        for estacao in dados_cadastrais.keys():
            indicador = dados_cadastrais[estacao]['volume']

            if indicador >=0 and indicador <121:
                reg.append(estacao)
            elif indicador >=120 and indicador <241:
                bom.append(estacao)
            elif indicador >=241 and indicador <361:
                mt_bom.append(estacao)

        if desempenho == "1":
            print(f"Regular: {reg}")
        elif desempenho == "2":
            print(f"Bom: {bom}")
        elif desempenho == "3":
            print(f"Muito bom: {mt_bom}")
        else:
            print("Categoria inválida!")
        
        return 1

    except KeyError:
        print("Estação inválida! Tente novamente.")
        return 0 

def relatorio_porcentagem():

    if len(dados_cadastrais) == 0:
        print("Nenhuma estação cadastrada")

    for i in dados_cadastrais.keys(): #i é a estação, j é a caçamba
        print(f"{i}:")
        for j in range(4):
            porcentagem= calcular_porcentagem(i, f'{j+1}') #A porcentagem recebia estacao, cacamba e fazia o calculo uma vez só. AGr calcula de acordo com i e j
            print(f"    - Porcentagem de ocupação da caçamba {j + 1}: {porcentagem:.1f}%")
            verificar_volume(i, f'{j+1}')
    return 1

#====================

def main():
    while True:
        print("Sistema EcoCity:")
        resposta = input("O que você quer fazer?\n0. Parar\n1. Cadastrar estação\n2. Verificar dados\n3. Cadastrar descarte\nR: ")
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

                    resposta = input("O que quer verificar?\n0. Sair\n1. Dados de todas as estações\n2. Dados de uma estação específica\n3. Créditos de carbono de uma estação\n4. Históricos\n5. Estações por índice de desempenho\n6. Relatório de ocupação geral\nR: ") #Adicionei o filtro do índice -Malu
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
                            resposta = input('Qual histórico você quer verificar?\n0. Sair\n1. Histórico dos últimos 10 descartes\n2. Histórico de um dia específico\n3. Histórico de um mês específico\nR: ')
                            match resposta:
                                case '0':
                                    break

                                case '1':
                                    estacao = input('Qual estação você quer verificar?\nR: ')
                        
                                    if historico_ultimos_10(estacao) == 1:
                                        break
                                    if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                                        print("================")
                                        break

                                case '2':
                                    estacao = input('Qual estação você quer verificar?\nR: ')
                                    mes = input('Qual mês você quer verificar?\nR: ')
                                    dia = input('Qual dia você quer verificar?\nR: ')
                                    if historico_dia(estacao, dia, mes) == 1:
                                        break
                                    if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                                        print("================")
                                        break
                                    break

                                case '3':
                                    estacao = input('Qual estação você quer verificar?\nR: ')
                                    mes = input('Qual mês você quer verificar?\nR: ')
                                    if historico_mes(estacao, mes) == 1:
                                        break
                                    if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                                        print("================")
                                        break
                                
                        case "5":
                            print("Estações por índice de desempenho:")
                            resposta = input("Qual categoria você quer verificar?\n1.Regular\n2.Bom\n3.Muito bom\nR: ")
    
                            if indicador_desempenho(resposta)==1:
                                    break
                            if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                                    print("================")
                        
                        case "6":
                            relatorio_porcentagem()
                
            case "3":
                while True:
                    print("================")
                    print("Cadastrar descarte:")

                    estacao = input("Em qual estação será feito o descarte?\nR:")
                    cacamba = input("Em qual caçamba será feito o descarte?\nR:")
                    descarte = input("Qual o peso do material descartado?\nR:")

                    if fazer_descarte(estacao, cacamba, descarte) == 1:
                        print("Descarte feito com sucesso!\n================")
                        break
                    if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                        print("================")
                        break

            case "4":
                while True:
                    print("================")
                    print("Verificação de dados:")

                    resposta = input("O que quer verificar?\n0. Sair\n1. Histórico dos últimos 10 dias\n2. Histórico de um dia especifico\n3. Histórico de um mês específico\nR: ")
                    print("================")

                    match resposta:
                        case "0":
                            break
                        case "1":
                            estacao = input('Qual estação você quer verificar?\nR: ')
                            if historico_ultimos_10(estacao) == 1:
                                break
                            if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                                print("================")
                                break
                            
                        case "2":
                            estacao = input('Qual estação você quer verificar?\nR: ')
                            dia = input('Em qual dia aconteceu o descarte?\nR: ')
                            mes = input('Em qual mes aconteceu o descarte?\nR: ')

                            if historico_dia(estacao, dia, mes) == 1:
                                break
                            if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                                print("================")
                                break
                        case "3":
                            estacao = input('Qual estação você quer verificar?\nR: ')
                            mes = input('Em qual mês aconteceu o descarte?\nR: ')

                            if historico_mes(estacao, mes) == 1:
                                break
                            if input("Tentar novamente?\n1. Sim\n2. Não\nR: ") == "2":
                                print("================")
                                break

main()