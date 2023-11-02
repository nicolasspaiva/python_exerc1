teams = {}
done = False



#Listar times
def prin_teams():
    print("Times Listados : ")
    for i , team in enumerate(teams.values()):
        print(f"{i+1}.{team['name']}({len(team['players'])}) jogadores")

# Lista jogadores de um time
def print_teams_players(team):
    print(f"Jogadores do {team['name']}")
    for i, player in enumerate(team['players']):
        print(f'{i+1}. {player}')



while not done :
    #Opções no programa
    print("O que vc deseja fazer  ?")
    print("1. Adicionar um time ")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adcionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    choice = input(">")
    if choice == "1":
       team_name = input("Digite o nome do time\n")
       teams[team_name] = {'name': team_name, 'players': []}
       print("Time Adicionado")
    elif choice == '2':
        prin_teams()
        team_num= int(input("Digite o número time que deseja remover \n"))
        if team_num<= len(teams):
            team_name = list(teams.keys())[team_num -1]
            del teams[team_name]
            print("Time removido")
        else:
            print("Número de time inválido")
    elif choice == '3':
        prin_teams()
    elif choice == '4':
        prin_teams()
        team_num = int(input("Informe o número do time que deseja adicionar o jogador \n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            player_name = input("Informe o nome do jogador: ")
            teams[team_name]['players'].append(player_name)
            print('Jogador adicionado no time')
        else:
            print("Número do time esta invalido")
    elif choice == '5':
        prin_teams()
        team_num = int(input("Informe o número do time que deseja remover o jogador \n"))
        if team_num <=len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_teams_players(teams[team_name])
            player_num= int(input(" Digite o número do jogador que deseja remover\n"))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num-1]
                print("Jogador removido")
            else:
                print("Jogador inválido")
        pass
    elif choice == '6':
        prin_teams()       
        team_num = int(input("Informe o número do time que deseja listar o jogador \n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_teams_players(teams[team_name])
        else:
            print("Numero do time inválido")
            
    elif choice == '7':
        done = True
    else:
     print('Opção invalida')