"""
Criar uma função que categorize o desempenho  das estações de descarte com um filtro que retorne apenas as estações correspondentes à categoria selecionada.
As categorias acompanharão o volume de descarte feito por estação. Quanto maior o volume de descarte, maior é o índice de desempenho.
de 0 a 25%= Regular
de 26% a 50%= Bom
de 51% a 75%= Muito bom
de 76% a 100%= Ótimo

        indicador = dados_cadastrais[estacao]['volume']
       
        if indicador >=0 and indicador <30:
            desempenho= "Regular"
        elif indicador >30 and indicador <=60:
            desempenho= "Bom"
        elif indicador >60 and indicador <= 90:
            desempenho= "Muito bom"
        else:
            print(f"Volume de descarte inválido.")
            return 0

"""
