#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadmatriz.py

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# ---------------------------------------------------------------------

def criar_matriz(quant_linhas,quant_colunas):
	m = {"linhas":quant_linhas,"colunas":quant_colunas}
	return m
#end criar

def getnumlinhas(m):
	return m["linhas"]
#end getnumlinhas

def getnumcolunas(m):
	return m["colunas"]
#end getnumcolunas

def getposi(m,l,c):
	if (l,c) in m:
		return m[(l,c)]
	else:
		return 0
#end getposi

def mostrar(m):
	for l in range(getnumlinhas(m)):
		for c in range(getnumcolunas(m)):
			print(getposi(m,l,c),end=" ")
		print()
#end mostrar 

def setvalor(m,l,c,v):
	if (l,c) in m:
		if v == 0:
			del m[(l,c)]
		else:
			m[(l,c)] = v
	else:
		m[(l,c)] = v
		
	return m
#end setvalor
		
def soma(mA,mB):
	mC= criar_matriz(getnumlinhas(mA),getnumcolunas(mA))
	for l in range(getnumlinhas(mA)):
		for c in range(getnumcolunas(mA)):
			if mA!=0 or mB!=0:
				mC[(l,c)] = mA[(l,c)] + mB[(l,c)]
	return mC
#end soma			
	
def transposta(m):
	t = criar_matriz(getnumcolunas(m),getnumlinhas(m))
	for l in range(getnumlinhas(m)):
		for c in range(getnumcolunas(m)):
			if c == 0:
				if getposi(m,l,c) != 0:
					v = getposi(m,l,c)
					setvalor(t,c,l,v)
				
			
		
