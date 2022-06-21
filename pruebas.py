
num = (input("Digite un numero entero de dos digitos: "))


def num_par (num = str):
    digito1 = int (num[0])
    digito2 = int (num[1])
    
    if digito1 % 2 == 0:
        print ("El primer digito es par")
        if digito2 % 2 == 0:
            print ("El segundo digito es par")
        else:
            print ("El segundo digito no es par")
    else:
        print ("El primer digito no es par")

print (num_par (num))