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
	matR = cria_tadmatriz(matA['lin'], matA['col'])
	
	if matA['lin'] == matB['lin'] and matA['col'] == matB['col']:
		for i in range(1, matA['lin'] + 1):
			for j in range(1, matA['col'] + 1):
				soma = get_IJ(matA, i, j) + get_IJ(matB, i, j)
				
				matR = set_IJ(matR, i, j, soma)
		
		return matR
	else:
		print('as matrizes nao podem ser somadas')

def main():
	matriz = cria_tadmatriz(2, 3)
	matriz2 = cria_tadmatriz(2, 3)
	
	matriz = set_IJ(matriz, 1, 3, 5)
	matriz = set_IJ(matriz, 2, 2, 8)
	matriz = set_IJ(matriz, 3, 2, 5)
	matriz = set_IJ(matriz, 1, 1, 6)
	matriz = set_IJ(matriz, 1, 2, 5)
	
	matriz2 = set_IJ(matriz2, 1, 3, 3)
	matriz2 = set_IJ(matriz2, 2, 2, 9)
	matriz2 = set_IJ(matriz2, 3, 2, 7)
	matriz2 = set_IJ(matriz2, 1, 1, 10)
	matriz2 = set_IJ(matriz2, 1, 2, 4)
	
	print(str_matriz(matriz))
	print(str_matriz(matriz2))
	print(str_matriz(soma(matriz, matriz2)))
	
	return 0

main()
