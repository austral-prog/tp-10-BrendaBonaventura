def max_value(dic):
	maximo=0
	nombre = ""
	for clave, valor in dic.items():
		if valor>maximo:
			maximo=valor
			nombre=clave
	return nombre

def reverse(dicc):
	a={}
	for clave, valor in dicc.items():
		if valor in a:
			a[valor]+=clave
		else:
			a[valor]=clave
	return a

def word_frequency_counter(lista):
	dic={}
	for items in lista:
		if items in dic:
			dic[items]+=1
		else:
			dic[items]=1
	return dic

def find_biggest_expense(dic):
	answer=("", 0)
	for clave, valor in dic.items():
		average=0
		for i in valor:
			average+=i
		average=average/len(valor)
		if answer[1]<average:
			answer=(clave, average)
	return answer[0]


def sum_of_expenses(dic):
	a={}
	for clave, valor in dic.items():
		suma=0
		for nro in valor:
			suma+=nro
			a[clave]=suma
	return a

def sum_of_expenses_by_type(dic):
	a={}
	for clave, valor in dic.items():
		for tipo, expense in valor:
			if tipo in a:
				a[tipo]+=expense
			else:
				a[tipo]=expense
	return a
