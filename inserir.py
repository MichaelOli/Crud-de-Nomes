nomes =[]
while True:
    # Solicita o nome da tarefa
    print(f'{'='*20} Adicionando Nomes a Lista {'='*20}')
    add_nome = input(
        'Informe o nome de uma tarefa ou aperte "enter" para exibir a lista: ')

    # Verifica se o usuário inseriu uma tarefa ou deseja exibir a lista
    if add_nome:
       nomes.append(add_nome)
    else:
        break

for nome in nomes:
    print(nome)