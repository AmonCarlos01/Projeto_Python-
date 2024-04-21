letra = input("Digite uma letra minúscula:")
if len(letra) == 1 and letra.islower():
    
    if letra in ['a', 'e', 'i','o', 'u']:
        print("A letra inserida é uma vogal.")
        
    else: 
        print("A letra inserida é uma consoante.")
