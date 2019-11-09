import json
'''
linha=[]
matriz=[]
for x in range(50):
	for y in range(50):
		linha.append(0)
	matriz.append(linha)
	linha=[]
arq=open("jooj.txt","wt")
json.dump(matriz,arq,indent=4)
arq.close()
arq=open("jooj.txt","rt")
jooj=json.load(arq)
print(jooj[0])
'''
def main():
	arq=open("Dominios_GovBR_basico.csv","rt",encoding="Windows-1252")
	cabec=arq.readline().strip().split(";")
	pos = arq.tell()
	linha=arq.readline()
	dic_saida={}
	
	while linha != "":
		lstlinha=linha.strip().split(";")
		dic_saida[lstlinha[0]]=pos
		pos=arq.tell()
		linha=arq.readline()
		
	arq.close()
	
	arq=open("jooj.json","wt")
	json.dump(dic_saida,arq,indent=4)
	
	arq.close()
	arq=open("jooj.json","rt")
	d=json.load(arq)
	arq.close()
	arq=open("Dominios_GovBR_basico.csv","rt",encoding="Windows-1252")
	arq.seek(d["rapidinha.gov.br"], 0)
	print(arq.readline())
	
	
	
	
	return 0
	
if __name__ == "__main__":
	main()
