#Leonardo Lino Guedes

#Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
#linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
#operações que serão realizadas entre dois conjuntos de dados.
#O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
#seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
#operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:

#Método correto para se abrir um conjunto em python
conjunto1 = set()
conjunto2 = set()
conjunto3 = set()

#Nomes que serão atribuidos as operações
nomeOp = ['União', 'Interceção', 'Difrença', 'Cartesiano']

#entrada do arquivo para ser lido e configurado para separar linha por linha, transformando em um arquivo em python e adiciona o leitor de caracter especial
with open("entrada3.txt", "r", encoding="utf-8") as arquivio:
    entrada = arquivio.readlines()

#recebe o número indicado no arquivo txt do tanto de operações presentes nele
numOp = int(entrada[0].strip())
linha = 1

#loop para ler todas as operações que tem dentro do arquivo txt lido
for cont in range(numOp):

    #recebe o número referente ao indice da letra da operação
    op = entrada[linha].strip()

    #Define o conjunto de acordo com a variável "linha" que sera sempre a primeira e segunda linha de baixo da letra da operação e faz uma separação toda vez que aparece uma ", " na linha
    conjunto1 =  set(entrada[linha+1].strip().split(", "))
    conjunto2 =  set(entrada[linha+2].strip().split(", "))

    #faz com que sempre pule para a proxima linha certa de operação a ser realizada (de 3 em 3)
    linha += 3

    #Possibilidades de respostas entre União, Interceção, Diferença, Produto Cartesiano
    if op == 'U':
        #Modifica o conjunto 3 para um conjunto de União
        conjunto3 = conjunto1 | conjunto2
        print(f"{nomeOp[0]}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {conjunto3} \n")

    elif op == 'I':
        #Modifica o conjunto 3 para um conjunto de Interceção
        conjunto3 = conjunto1 & conjunto2
        print(f"{nomeOp[1]}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {conjunto3}\n")

    elif op == 'D':
        #Modifica o conjunto 3 para um conjunto de Diferença
        conjunto3 = conjunto1 - conjunto2
        print(f"{nomeOp[2]}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {conjunto3}\n")

    elif op == 'C':
        #Modifica o conjunto 3 para um conjunto de Produto Cartesiano
        conjunto3 = conjunto1 ^ conjunto2
        print(f"{nomeOp[3]}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {conjunto3}\n")