valor = float(input())

newS = 0
if valor <= 2000:
    print("Isento")
    
elif valor <= 3000:
    
    imposto = (valor - 2000)*8/100
    print("R$ {:.2f}".format(imposto))
    
elif valor <= 4500:
    
    imposto1 = (valor - 3000)
    valorImposto1 = imposto1 * 18 / 100
    imposto2 = (valor - 2000) - imposto1
    valorImposto2 = imposto2 * 8 / 100
    
    print("R$ {:.2f}".format(valorImposto1 + valorImposto2))

elif valor > 4500:
    imposto1 = valor - 4500 
    imposto2 = (valor - 3000) - imposto1 
    imposto3 = (valor - 2000) - imposto1 - imposto2
    
    valor1 = imposto1 * 28/100 
    valor2 = imposto2 * 18 / 100
    valor3 = imposto3 * 8 / 100
    
    print("R$ {:.2f}".format(valor1 +  valor2 + valor3))

    
    
    
    

    
    
    
