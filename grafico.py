array = [1, 800, 5, 1000, 780, 1500, 1800, 320, 620, 470, 21] 


tara = 200
fatorConversao = 100
taraC = int(tara/fatorConversao) 

i = -1

arrayAproximado = [] 
	
	
for num in array:
    arrayAproximado.append(int((num - (num % tara))/100)) 

print(arrayAproximado) 


print(array) 


print("=====================")


print("""
	
	
   Gráfico do seu crescimento econômico 
	        por semana
	
	
	""") 

print("""____________________________valores ➡️ """)

while i < len(arrayAproximado):
    i = i + 1
    b = arrayAproximado[i] 
    if i == len(arrayAproximado) - 1:
        break
    else:
        if b > arrayAproximado[(i + 1)]:
            while b > arrayAproximado[(i + 1)]:
        	        escreve = "|" 
        	        vazio = " " 
                	vazio = 	vazio * b
                	escreve = escreve + vazio + "." 
                	print(escreve) 
                	b = b - taraC
        elif b  < arrayAproximado[(i + 1)]:
            while b < arrayAproximado[(i + 1)]:
        	        escreve = "|" 
        	        vazio = " " 
                	vazio = 	vazio * b
                	escreve = escreve + vazio + "." 
                	print(escreve) 
                	b = b + taraC

ult = array[len(array) - 1] 
escreve = "|" 
vazio = " " 
vazio = 	vazio * int((ult/fatorConversao)) 
escreve = escreve + vazio + "." + str(ult) 
print(escreve)

print("""|
|
|
|
T
e
m
p
o
⬇️
""") 


print("""
	
__________________________________________

Tempo fora de escala 

__________________________________________
""")

#COLOCAR OS PONTOS ONDE SÃO REPRESENTADOS OS VALORES DO ARRAY
    


#print(array)
#print("__________________________________________") 
