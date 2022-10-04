#HISTOGRAMA 

L1 = [17.8, 17.89, 17.47, 17.47, 
18.31, 19.8, 18.30, 18.75, 19.37,
17.61, 18.60, 17.39, 19.23, 17.85,
17.80, 16.85, 16.69, 16.65, 17.21,
17.06, 18.23, 18.04, 18.57, 16.21,
17.86]



L1.sort() 
print(L1) 


casa = 0.5
i = 14.0


while i < 22:
    print(i, end="") 
    print('*', end="") 
    for n in L1:
        if (n >= i and n < (i + casa)):
            print('||',  end="") 
    i += casa
    print("") 

       
acumulador = 0     
for n in L1:
    acumulador += n


#PARTE DO CÓDIGO QUE REALIZA OS CÁLCULOS DE MÉDIA/DESVIO PADRÃO/INCERTEZA/TESTE Z
#media = acumulador/len(L1) 
#print(media)

#dp = [] 
#for n in L1:
#    dp.append(n-media)
    
    
#print(dp) 
