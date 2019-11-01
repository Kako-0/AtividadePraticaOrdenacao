from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import time
'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":
	#Menu para escolher qual algoritmo de ordenação usar e em seguida com quantos vertices terá
	print("1.QuickSort\n2.MergeSort\n3.InsertSort\n4.QuickSort + inserção parcial\n5.QuickSort + inserção final\n6.MergeSort + inserção parcial\n7.MergeSort + inserção final\n")
	qualOrdena = input("Escolha qual algoritmo de ordenacao irá usar\n")
	if int(qualOrdena) == 1:
		algoritimoDeOrdenacao = QuickSort()
	elif int(qualOrdena) == 2:
		algoritimoDeOrdenacao = MergeSort()
	elif int(qualOrdena) == 3:
		algoritimoDeOrdenacao = InsertSort()
	elif int(qualOrdena) == 4:
		algoritimoDeOrdenacao = QuickSortParcial()
	elif int(qualOrdena) == 5:
		algoritimoDeOrdenacao = QuickSortFinal()
	elif int(qualOrdena) == 6:
		algoritimoDeOrdenacao = MergeSortParcial()
	elif int(qualOrdena) == 7:
		algoritimoDeOrdenacao = MergeSortFinal()
	else:
		print("Entrada desconhecida, utilizando QuickSort como padrão...\n")
		algoritimoDeOrdenacao = QuickSort()

	print("Escolha quantos vértices deseja usar\n")
	qualVertice = input("1. 7 vértices\t2. 100 vértices\t3. 1000 vértices\t4. 10000 vértices\t5. 100000 vértices\n")
	if int(qualVertice) == 1:
		arquivoJson = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/grafos/7vertices.json'
		arquivoDeSaida = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/arvores_geradas/resultadoCom7Vertices.txt'
	elif int(qualVertice) == 2:
		arquivoJson = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/grafos/100vertices.json'
		arquivoDeSaida = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/arvores_geradas/resultadoCom100Vertices.txt'
	elif int(qualVertice) == 3:
		arquivoJson = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/grafos/1000vertices.json'
		arquivoDeSaida = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/arvores_geradas/resultadoCom1000Vertices.txt'
	elif int(qualVertice) == 4:
		arquivoJson = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/grafos/10000vertices.json'
		arquivoDeSaida = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/arvores_geradas/resultadoCom10000Vertices.txt'
	elif int(qualVertice) == 5:
		arquivoJson = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/grafos/100000vertices.json'
		arquivoDeSaida = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/arvores_geradas/resultadoCom100000Vertices.txt'
	else:
		print("Entrada desconhecida, usando 7 vértices como padrão...\n")
		arquivoJson = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/grafos/7vertices.json'
		arquivoDeSaida = '/home/kayro/Documentos/MEUAtividadePratica01_2019.2/arvores_geradas/resultadoCom7Vertices.txt'
	
	grafo = Grafo()
	grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
	grafo.carregarGrafo(arquivoJson)

	arvoreGeradoraMinima =  grafo.executarKruskal() 
	SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)
    

