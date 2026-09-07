''''
Autor do projeto: Wendel Spargoli Bernardo da Silva (Matrícula: 2025b011434)

Parte 2 do Mini-trabalho refatoração do código para POO

criação de um sistema de cadastro de jogos
'''

# Classe jogos (superclasse)
class Jogo:
    def __init__(self, nome, tempo_jogo, preco):
        self.nome = nome;
        self.tempo_jogo = tempo_jogo;
        self.__preco = preco; # preço marcado como privado para evitar alterações indesejadas

    def get_preco(self): # Método para leitura de dado privado
        return self.__preco

    def set__preco(self, novo_preco): #Método para alteração do preço do jogo
        self.__preco = novo_preco

    def __str__(self): # Função para formatar a estring a ser usada
            return f"{self.nome} - {self.tempo_jogo}hrs médias de jogo - R${self.get_preco()}." #O valor do print troca a vírgula pelo ponto. Quero colocar para que o valor do jogo saia com a vírgula no terminal.

# Subclasse para identificação de jogos digitais
class jogo_digital(Jogo):
    def __init__(self, nome, tempo_jogo, preco, tamanho, loja):
        super().__init__(nome, tempo_jogo, preco);
        self.tamanho = tamanho
        self.loja = loja
        super().set__preco()

    def __str__(self): # formatação da estring, puxando dados da mãe
        return f"{super(). __str__()} - {self.tamanho}Gb - comprado no {self.loja}."

# Subclasse para identificação de jogos físicos
class jogo_fisico(Jogo):
    def __init__(self, nome, tempo_jogo, preco, formato, plataforma):
        super().__init__(nome, tempo_jogo, preco);
        self.formato = formato
        self.plataforma = plataforma
        super().set__preco()

    def __str__(self): # formatação da estring, puxando dados da mãe
        return f"{super(). __str__()} - {self.formato} - para ser jogado no {self.plataforma}."

# Lista de jogos
Jogos = [] # Lista em aberto para o cadastro

# Criação de Menu
def exibir_menu():
    print ("\nBem-vindo(a) à sua lista de jogos! O que você quer fazer hoje? \n 1 - Listar jogos \n 2 - Cadastrar jogos \n 3 - Buscar jogo \n 4 - Alterar jogo \n 5 - Remover jogo \n 6 - Jogo mais caro \n 0 - Sair");

# 1 - Listagem de Jogos
def listar_tudo():
    if not Jogos: # A negativa foi colocada fora do laço. Se estivesse dentro do laço e não tivesse jogo na lista, o código não iria rodar.
        print("\nNão há jogos cadastrados no momento!\n");
    else:
        for jogo in Jogos:
            print(jogo);

# 2 - Cadastro de jogos
def cadastro_jogo():
    print("\nBem-vindo(a) ao cadastro de jogos! \nPor favor, insira as seguintes informações:\n");
    nome = input("Digite o nome do jogo: ").strip(); #Utilização do "strip()" para eliminar os espaços do início e fim
    tempo_jogo = input("Digite o tempo médio de jogo (em horas): ").strip();
    preco = float(input("Digite o valor do jogo (em reais): ").strip().replace(",",".")); # Utilizei a IA para me ajudar a entender como substituir a vírgula pelo ponto, caso o usuário escreva o valor com vírgula e o código precise ler. É umportante ressaltar que o tratamento do texo deve vir antes da conversão para "float", porque, se não for, o código dá erro.

    print("\nEscolha a categoria que a qual seu jogo pertence: \n1 - Jogo digital \n2 - Jogo físico"); #Definindo em qual subclasse o jogo cadastrado irá adentrar
    categoria = input("\nInforme o número desejado: ").strip();
    if categoria in ["01", "1"]: # Entendi uma nova forma para escrever duas ou mais opções a serem aceitas no input sem precisar repetir "categoria ==".

        ''''

        Fazer a validação do código - o tamanho e a loja ainda aceitam respostas incorretas

        '''

        tamanho = float(input("\nInforme o tamanho aproximado do jogo: ").strip().replace(",","."));
        loja = input("\nInforme a loja de compra do jogo: ").strip();

        #Descobri que o métido "append" só permite apenas um argumento
        #Criação do objeto na suclasse
        novo_jogo_dig = jogo_digital(nome, tempo_jogo, preco, tamanho, loja);

        #Ordem de cadastro
        Jogos.append(novo_jogo_dig);
        print(f"\nO jogo {nome} foi cadastrado com sucesso!");

    elif categoria in ["02", "2"]:
        formato = input("\nInforme o formato da mídia física do jogo: ").strip();
        plataforma = input("\nInforme a plataforma em que o jogo será jogado: ").strip();

        #Criação da subclasse
        novo_jogo_fis = jogo_fisico(nome, tempo_jogo, preco, formato, plataforma);

        #Odem de cadastro
        Jogos.append(novo_jogo_fis);
        print(f"\nO jogo {nome} foi cadastrado com sucesso!");

# 3 - Buscar jogo
def buscar_jogo():
    #Termo de busca para identificar o jogo
    termo_busca = input("\nInforme o nome do jogo: ").strip();
    for jogo in Jogos:
        if jogo.nome.lower() == termo_busca.lower(): #Colocando a comparação dos nomes em minúsculo para evitar erros na diferenciação das letras
            print(f"Encontrei o jogo informado com os seguintes dados:\n{jogo}\n");
            return
    print("\nO jogo informado não foi encontrado. Certifique-se de digitar o nome corretamente ou proceda com o cadastro do jogo.");
    
# 4 - Alterar jogo
def alterar_jogo():
    #Aviso de limitação
    print("\nPor motivos de limitação de funcionários, no momento as modificações de dados só estão disponíveis para dados primários: nome, tempo de jogo e preço.");
    #Termo de busca para buscar o jogo
    termo_busca = input("\nInforme o nome do jogo que você queira alterar: ").strip();
    
    for jogo in Jogos:
        if jogo.nome.lower() == termo_busca.lower():
            print("\nQual informação você deseja alterar? \n1- nome \n2 - tempo de jogo \n3 - preço");
            opcao = input("\nInforme o número devido para alteração: "). strip();
            if opcao in ["01", "1"]:
                jogo.nome = input("\nInsira o novo nome do jogo: ").strip();
            elif opcao in ["02", "2"]:
                jogo.tempo_jogo = input("\nInsira o novo tempo médio de jogo: ").strip();
            elif opcao in ["03", "3"]:
                novo_valor = float(input("\nInforme o novo valor a ser atribuído ao jogo").strip().replace(",","."));
                jogo.set_preco(novo_valor); #Premissão para alteração do novo valor do jogo.
            else:
                print("\nOpção incorreta. Por favor, insira um número válido");
            

# 5 - Remover Jogo

# 6 - Jogo mais caro

# Menu principal
def principal():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma das opções informadas: ").strip();
        if opcao in ["01", "1"]:
            listar_tudo();
        elif opcao in ["02", "2"]:
            cadastro_jogo();
        elif opcao in ["03", "3"]:
            buscar_jogo();
        elif opcao in ["04", "4"]:
            alterar_jogo();

principal()
