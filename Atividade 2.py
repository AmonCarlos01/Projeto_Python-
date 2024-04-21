A = "Cachorro Quente"
B = "Bauru Simples"
C = "Bauru com ovo"
D = "Hamburguer"
E = "Cheeseburguer"
F = "Suco"
G = "Refrigerante"

codigo = float(input("Digite o codigo:"))

if codigo == 100 :
    print (A,"1,20")
if codigo == 101:
    print (B,"1,30")
if codigo == 102 :
    print (C,"1,50")
if codigo == 103 :
    print (D,"1,20")
if codigo == 104 :
    print (E,"1,70")
if codigo == 105 :
    print (F,"2,20")
if codigo == 106 :
    print (G,"1,00")
    
if codigo >106 :
    print ("CODIGO INVALIDO")
    
if codigo <100 :
    print ("CODIGO INVALIDO")
    


