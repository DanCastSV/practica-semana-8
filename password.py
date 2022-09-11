#Daniel Enrique Zaldaña Castillo 
#Moises Antonio Martínez
def pwd(password):
    pwd_ = password
    if len(pwd_) < 8:
        print("Contraseña no es segura, la contraseña debe de cotener un minimo de 8 caracteres")
    elif pwd_.count(" ")>0:
        print("La contraseña no es segura, la contraseña no debe de contener espacios en blanco")
    else:
        pwd2_=input("Por favor vuelva a ingresar su contraseña: ")
        if pwd2_==pwd_:
            print("La contraseña es valida")
        else:
            print("La contraseña no es valida")

    
    return 
