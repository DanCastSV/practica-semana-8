#Daniel Enrique Zaldaña Castillo 
#Moises Antonio Martínez 

def usuar(user):
    u=user 

    if len(u) < 6:
        print("El usuario ingresado no es valido, para que sea valido debe de contener al menos 6 caracteres")
    elif len(u) > 12:
         print("El usuario ingresado no es valido, el maximo de caracteres permitidos es 12")
    elif u.isalnum()==False:
         print("El usuario ingresado no es valido, para que el usuario sea valido")
         print("debe de contener caractares 'A-Z' 'a-z' '0-9'")
         print("los caracteres #$&/()=! y los espacios en blanco no son permitidos")
    else :
        print("el usuario es valido")
    return 

