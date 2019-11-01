import math
'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''


# Sua classe algoritmo de ordenação precisar ter um método ordenar
import time
class InsertSort(object):
	def ordenar(self, colecao):
		start = time.time()
		for j in range(1, len(colecao)):
			key = colecao[j]
			i = j - 1

			while i >= 0 and int(colecao[i]['weight']) > int(key['weight']):
				colecao[i + 1] = colecao[i]
				i -= 1

			colecao[i + 1] = key

		print("--- %s segundos/ InsertSort ---" % (time.time() - start))
		return colecao
##########################################################################################
class Substitutos(object):
	def selectSort(self, colecao):
		for i in range(0, len(colecao)):
			minimo = i
			for j in range(i + 1, len(colecao)):
				if int(colecao[j]['weight']) < int(colecao[minimo]['weight']):
					minimo = j
			temp = colecao[minimo]
			colecao[minimo] = colecao[i]
			colecao[i] = temp
		return colecao

	def shellSort(self, colecao):
		h = 1
		for h in range(h, len(colecao), (3 * h) - 1):
			h = int(h)

		while h > 0:
			h = math.ceil((h - 1) / 3)
			for i in range(h, len(colecao)):
				aux = colecao[i]
				j = i
				while j >= h and int(colecao[j - h]['weight']) > int(aux['weight']):
					colecao[j] = colecao[j - h]
					j = j - h
					if j < h:
						break

				colecao[j] = aux

		return colecao
###########################################################################################
class QuickSort(object):
	def troca(self, colecao, media, fim):
		auxiliar = colecao[media]
		colecao[media] = colecao[fim]
		colecao[fim] = auxiliar

	def particao(self, colecao, inicio, fim):
		#Procura a mediana da coleção
		meio = int((inicio + fim)/2)
		a = int(colecao[inicio]['weight'])
		b = int(colecao[meio]['weight'])
		c = int(colecao[fim]['weight'])
		mediana = 0
        #Verifica qual é a mediana
		if a < b:
			if b < c:
				mediana = meio
			else:
				if a < c:
					mediana = fim
				else:
					mediana = inicio
		else:
			if c < b:
				mediana = meio
			else:
				if c < a:
					mediana = fim
				else:
					mediana = inicio
		
		self.troca(colecao, mediana, fim)

#---------- QuickSort criado por Cormen ----------------#
		
		pivo = colecao[fim]#O pivo é o último elemento da coleção
		i = inicio - 1

		for j in range(inicio, fim):
			if int(colecao[j]['weight']) <= int(pivo['weight']):
				i += 1
				self.troca(colecao, i, j)

		self.troca(colecao, i + 1, fim)#Coloca o pivô na sua posição de ordenação
		return i + 1

	def quickSort(self, colecao, inicio, fim):
		if inicio < fim:
			sort = self.particao(colecao, inicio, fim) #Particiona a coleção
			self.quickSort(colecao, inicio, sort - 1) #Ordena o lado esquerdo da coleção
			self.quickSort(colecao, sort + 1, fim)	#Ordena o lado direto da coleção
			return colecao


	def ordenar(self, colecao):
		start = time.time()

		self.quickSort(colecao, 0, len(colecao) - 1)
		
		print("--- %s segundos ---" % (time.time() - start))
		return colecao
################################################################################################
class QuickSortFinal(object):
	
	def troca(self, colecao, media, fim):
		auxiliar = colecao[media]
		colecao[media] = colecao[fim]
		colecao[fim] = auxiliar

	def particao(self, colecao, inicio, fim):
		#Procura a mediana da coleção
		meio = int((inicio + fim)/2)
		a = int(colecao[inicio]['weight'])
		b = int(colecao[meio]['weight'])
		c = int(colecao[fim]['weight'])
		mediana = 0
        #Verifica qual é a mediana
		if a < b:
			if b < c:
				mediana = meio
			else:
				if a < c:
					mediana = fim
				else:
					mediana = inicio
		else:
			if c < b:
				mediana = meio
			else:
				if c < a:
					mediana = fim
				else:
					mediana = inicio
		
		self.troca(colecao, mediana, fim)

#---------- QuickSort criado por Cormen ----------------#
		
		pivo = colecao[fim]#O pivo é o último elemento da coleção
		i = inicio - 1

		for j in range(inicio, fim):
			if int(colecao[j]['weight']) <= int(pivo['weight']):
				i += 1
				self.troca(colecao, i, j)

		self.troca(colecao, i + 1, fim)#Coloca o pivô na sua posição de ordenação
		return i + 1

	def quickSortFinal(self, colecao, inicio, fim, L, ordem):
		if inicio < fim:
			sort = self.particao(colecao, inicio, fim) #Particiona a coleção
			self.quickSortFinal(colecao, inicio, sort - 1, L, ordem) #Ordena o lado esquerdo da coleção
			self.quickSortFinal(colecao, sort + 1, fim, L, ordem)	#Ordena o lado direto da coleção
		return colecao
		
	def ordenar(self, colecao):
		L = int(input("Digite L:\n"))
		ordem = int(input("Qual algoritmo de ordenação usar\n1.InsertSort\n2.SelectSort\n3.ShellSort\n"))
		
		start = time.time()

		self.quickSortFinal(colecao, 0, len(colecao) - 1, L, ordem)

		sub = Substitutos()
		inset = InsertSort()
		if ordem == 1:
			inset.ordenar(colecao)
		elif ordem == 2:
			sub.selectSort(colecao)
		elif ordem == 3:
			sub.shellSort(colecao)
		else:
			print("Entrada desconhecida, utilizando InsertSort como padrão...\n")
			inset.ordenar(colecao)

		print("--- %s segundos ---" % (time.time() - start))
		return colecao
#################################################################################################
class QuickSortParcial(object):
	
	def troca(self, colecao, media, fim):
		auxiliar = colecao[media]
		colecao[media] = colecao[fim]
		colecao[fim] = auxiliar

	def particao(self, colecao, inicio, fim):
		#Procura a mediana da coleção
		meio = int((inicio + fim)/2)
		a = int(colecao[inicio]['weight'])
		b = int(colecao[meio]['weight'])
		c = int(colecao[fim]['weight'])
		mediana = 0
        #Verifica qual é a mediana
		if a < b:
			if b < c:
				mediana = meio
			else:
				if a < c:
					mediana = fim
				else:
					mediana = inicio
		else:
			if c < b:
				mediana = meio
			else:
				if c < a:
					mediana = fim
				else:
					mediana = inicio
		
		self.troca(colecao, mediana, fim)

#---------- QuickSort criado por Cormen ----------------#
		
		pivo = colecao[fim]#O pivo é o último elemento da coleção
		i = inicio - 1

		for j in range(inicio, fim):
			if int(colecao[j]['weight']) <= int(pivo['weight']):
				i += 1
				self.troca(colecao, i, j)

		self.troca(colecao, i + 1, fim)#Coloca o pivô na sua posição de ordenação
		return i + 1

	def quickSortParcial(self, colecao, inicio, fim, L, ordem):
		if L < fim - inicio + 1 :
			sort = self.particao(colecao, inicio, fim) #Particiona a coleção
			self.quickSortParcial(colecao, inicio, sort - 1, L, ordem) #Ordena o lado esquerdo da coleção
			self.quickSortParcial(colecao, sort + 1, fim, L, ordem)	#Ordena o lado direto da coleção
		else:
			sub = Substitutos()
			inset = InsertSort()
			if ordem == 1:
				inset.ordenar(colecao)
			elif ordem == 2:
				sub.selectSort(colecao)
			elif ordem == 3:
				sub.shellSort(colecao)
			else:
				print("Entrada desconhecida, utilizando InsertSort como padrão...\n")
				inset.ordenar(colecao)
		return colecao
		
	
	def ordenar(self, colecao):
		L = int(input("Digite L:\n"))
		ordem = int(input("Qual algoritmo de ordenação usar\n1.InsertSort\n2.SelectSort\n3.ShellSort\n"))
		start = time.time()

		self.quickSortParcial(colecao, 0, len(colecao) - 1, L, ordem)
		sub = Substitutos()
		inset = InsertSort()
		if ordem == 1:
			inset.ordenar(colecao)
		elif ordem == 2:
			sub.selectSort(colecao)
		elif ordem == 3:
			sub.shellSort(colecao)
		else:
			print("Entrada desconhecida, utilizando InsertSort como padrão...\n")
			inset.ordenar(colecao)

		print("--- %s segundos ---" % (time.time() - start))
		return colecao
	
################################################################################################
class MergeSort(object):
	def mergeSort(self, colecao):
		if len(colecao) > 1:
			meio = int(len(colecao) / 2)
			esquerda = colecao[:meio] #Atribuindo a primeira metade ao vetor esquerda
			direita = colecao[meio:] #Atribuindo a segunda metade ao vetor direito
		#Subdividindo recursivamente até que o vetor tenha tamanho 1
			self.mergeSort(esquerda)
			self.mergeSort(direita)

			i = j = k = 0 #Índice inicial do vetor esquerda, direita e coleção, respectivamente

			while i < len(esquerda) and j < len(direita):
        #Dividindo colecao em dois subarrays
				if int(esquerda[i]['weight']) < int(direita[j]['weight']):
					colecao[k] = esquerda[i]
					i += 1
				else:
					colecao[k] = direita[j]
					j += 1
				k += 1
		#Mesclando os subarrays esquerda e direita na colecao
			while i < len(esquerda):
                
				colecao[k] = esquerda[i]
				i += 1
				k += 1

			while j < len(direita):
				colecao[k] = direita[j]
				j += 1
				k += 1

		return colecao

	def ordenar(self, colecao):
		start = time.time()

		self.mergeSort(colecao)

		print("--- %s segundos ---" % (time.time() - start))
		return colecao
###############################################################################################
class MergeSortParcial(object):

	def mergeSortParcial(self, colecao, L, ordem):
		if len(colecao) > L:
			meio = int(len(colecao) / 2)
			esquerda = colecao[:meio] #Atribuindo a primeira metade ao vetor esquerda
			direita = colecao[meio:] #Atribuindo a segunda metade ao vetor direito
		#Subdividindo recursivamente até que o vetor tenha tamanho L
			self.mergeSortParcial(esquerda, L, ordem)
			self.mergeSortParcial(direita, L, ordem)

			i = j = k = 0 #Índice inicial do vetor esquerda, direita e coleção, respectivamente

			while i < len(esquerda) and j < len(direita):
        #Dividindo colecao em dois subarrays
				if int(esquerda[i]['weight']) < int(direita[j]['weight']):
					colecao[k] = esquerda[i]
					i += 1
				else:
					colecao[k] = direita[j]
					j += 1
				k += 1
		#Mesclando os subarrays esquerda e direita na colecao
			while i < len(esquerda):
                
				colecao[k] = esquerda[i]
				i += 1
				k += 1

			while j < len(direita):
				colecao[k] = direita[j]
				j += 1
				k += 1
		else:
			sub = Substitutos()
			inset = InsertSort()
			if ordem == 1:
				inset.ordenar(colecao)
			elif ordem == 2:
				sub.selectSort(colecao)
			elif ordem == 3:
				sub.shellSort(colecao)
			else:
				print("Entrada desconhecida, utilizando InsertSort como padrão...\n")
				inset.ordenar(colecao)
		return colecao

	def ordenar(self, colecao):
		L = int(input("Digite L:\n"))
		ordem = int(input("Qual algoritmo de ordenação usar\n1.InsertSort\n2.SelectSort\n3.ShellSort\n"))
		start = time.time()

		self.mergeSortParcial(colecao, L, ordem)

		print("--- %s segundos ---" % (time.time() - start))
		return colecao
##################################################################################################
class MergeSortFinal(object):

	def mergeSortFinal(self, colecao, L):
		if len(colecao) > L:
			meio = int(len(colecao) / 2)
			esquerda = colecao[:meio] #Atribuindo a primeira metade ao vetor esquerda
			direita = colecao[meio:] #Atribuindo a segunda metade ao vetor direito
		#Subdividindo recursivamente até que o vetor tenha tamanho L
			self.mergeSortFinal(esquerda, L)
			self.mergeSortFinal(direita, L)

			i = j = k = 0 #Índice inicial do vetor esquerda, direita e coleção, respectivamente

			while i < len(esquerda) and j < len(direita):
        #Dividindo colecao em dois subarrays
				if int(esquerda[i]['weight']) < int(direita[j]['weight']):
					colecao[k] = esquerda[i]
					i += 1
				else:
					colecao[k] = direita[j]
					j += 1
				k += 1
		#Mesclando os subarrays esquerda e direita na colecao
			while i < len(esquerda):
                
				colecao[k] = esquerda[i]
				i += 1
				k += 1

			while j < len(direita):
				colecao[k] = direita[j]
				j += 1
				k += 1

		return colecao

	def ordenar(self, colecao):
		L = int(input("Digite L:\n"))
		ordem = int(input("Qual algoritmo de ordenação usar\n1.InsertSort\n2.SelectSort\n3.ShellSort\n"))
		end = time.time()

		self.mergeSortFinal(colecao, L)

		sub = Substitutos()
		inset = InsertSort()
		if ordem == 1:
			inset.ordenar(colecao)
		elif ordem == 2:
			sub.selectSort(colecao)
		elif ordem == 3:
			sub.shellSort(colecao)
		else:
			print("Entrada desconhecida, utilizando InsertSort como padrão...\n")
			inset.ordenar(colecao)

		print("--- %s segundos ---" % (time.time() - start))
		return colecao
#################################################################################################