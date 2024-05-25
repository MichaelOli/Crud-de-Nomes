#pesquisa baseada na variavel do arquivo inserir.py
from  inserir.py import nome
pesquisa = input('Digite o nome a ser pesquisado: ').capitalize()

# verifica se o nome está na lista ou não
try:
    # retorna o indice do nome pesquisado
    indice = pesquisa.index(pesquisa)
    print(f'Nome encontrado: {pesquisa} no índice {indice}.')
except:
    print(f'{pesquisa} não encontrado na lista.')
