#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tad_matriz.py
#  
#  Copyright 2019 Matheus <matheus@dual-core>
#  

def cria_tadmatriz(nLin, nCol):
	tadMat = {'lin': nLin, 'col': nCol}
	
	return tadMat

def set_IJ(tadMat, i, j, val):
	if i > 0 and i <= tadMat['lin'] and j > 0 and j <= tadMat['col']:
		if val == 0:
			if i * 10 + j in tadMat:
				del tadMat[i * 10 + j]
		else:
			tadMat[i * 10 + j] = val
	else:
		print('Posição não existe')
	
	return tadMat

def get_IJ(tadMat, i, j):
	if i > 0 and i <= tadMat['lin'] and j > 0 and j <= tadMat['col']:
		if (i * 10 + j) in tadMat:
			return tadMat[i * 10 + j]
		else:
			return 0
	else:
		print('Posição não existe')

def str_matriz(tadMat):
	str_mat = ''
	
	for i in range(1, tadMat['lin'] + 1):
		for j in range(1, tadMat['col'] + 1):
			if i * 10 + j in tadMat:
				str_mat = str_mat + str(tadMat[i * 10 + j]) + ' '
			else:
				str_mat = str_mat + '0 '
		
		str_mat = str_mat + '\n'
	
	return str_mat

def soma(matA, matB):
	if matA['lin'] == matB['lin'] and matA['col'] == matB['col']:
		matR = cria_tadmatriz(matA['lin'], matA['col'])
		for i in range(1, matA['lin'] + 1):
			for j in range(1, matA['col'] + 1):
				soma = get_IJ(matA, i, j) + get_IJ(matB, i, j)
				
				matR = set_IJ(matR, i, j, soma)
		
		return matR
	else:
		print('as matrizes nao podem ser somadas')

def transposta(m):
	matT = cria_tadmatriz(m['col'], m['lin'])
	
	for i in range(1, m['lin'] + 1):
		for j in range(1, m['col'] + 1):
			matT = set_IJ(matT, j, i, get_IJ(m, i, j))
	
	return matT

def getlinha(m1, lin):
	lst = []
	
	for i in range(1, m1['col'] + 1):
		if (lin * 10 + i) in m1:
			lst.append(m1[lin * 10 + i])
		else:
			lst.append(0)
	print(lst)
	return lst

def getcoluna(m1, col):
	lst = []
	
	for i in range(1, m1['lin'] + 1):
		if (i * 10 + col) in m1:
			lst.append(m1[i * 10 + col])
		else:
			lst.append(0)
	print(lst)
	return lst

def multLst(lst1, lst2):
	mult = 0
	
	for i in range(len(lst1)):
		mult += lst1[i] * lst2[i]
	
	return mult

def multiplica(m1, m2):
	mR = cria_tadmatriz(m1['lin'], m2['col'])
	
	if m1['col'] == m2['lin']:
		for i in range(1, m1['lin'] + 1):
			lstLin = getlinha(m1, i)
			for j in range(1, m2['col'] + 1):
				lstCol = getcoluna(m2, j)
				val = multLst(lstLin, lstCol)
				
				if val != 0:
					mR = set_IJ(mR, i, j, val)
	
	return mR

def main():
	matriz = cria_tadmatriz(2, 2)
	matriz2 = cria_tadmatriz(2, 2)
	
	matriz = set_IJ(matriz, 1, 3, 5)
	matriz = set_IJ(matriz, 2, 2, 8)
	matriz = set_IJ(matriz, 3, 2, 5)
	matriz = set_IJ(matriz, 1, 1, 6)
	matriz = set_IJ(matriz, 1, 2, 5)
	matriz = set_IJ(matriz, 2, 2, 0)
	
	matriz2 = set_IJ(matriz2, 1, 3, 3)
	matriz2 = set_IJ(matriz2, 2, 2, 9)
	matriz2 = set_IJ(matriz2, 3, 2, 7)
	matriz2 = set_IJ(matriz2, 1, 1, 10)
	matriz2 = set_IJ(matriz2, 1, 2, 4)
	
	print(str_matriz(matriz))
	print(str_matriz(matriz2))
	#print(str_matriz(soma(matriz, matriz2)))
	
	print(str_matriz(transposta(matriz)))
	
	print(multiplica(matriz, matriz2))
	
	return 0

if __name__ == '__main__':
	main()
