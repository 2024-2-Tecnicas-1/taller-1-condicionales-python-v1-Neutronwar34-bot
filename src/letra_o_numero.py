def evaluar(caracter):
    if len(caracter) >1:
        return "entrada no permitida"
    if caracter.isalpha():
 
        if caracter.isupper():
            return "Es letra mayúscula"
        
        elif caracter.islower():
            return "Es letra minúscula"
        
    elif caracter.isdigit():
        return "Es número"
    
    else:
        return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
