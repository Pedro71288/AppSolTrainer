def digitos(car):
    return car in "0123456789"

def principal():
    #Variables
    cant_letras = r1 = r3=  r4 = 0
    r2 = None
    #1
    cant_digitos = cant_min =  0
    #2
    si_dig = True
    #3
    cant_n = 0
    cant_a = False

    #apertura de archivo
    m = open("entrada2.txt")
    texto = m.read()
    m.close()

    #Inicio de proceso
    for car in texto:
        if car in " .":
            if cant_letras > 0:
                #1
                if cant_digitos == 1 and cant_min == cant_letras - 1:
                    r1 += 1
                #2
                if si_dig and (r2 is None or cant_letras < r2):
                    r2 = cant_letras
                #3
                if cant_n == 2 and cant_a:
                    r3 += 1
                #4
                pass

            #reinicio de variables
            cant_letras = 0
            #1
            cant_digitos = cant_min = 0
            #2
            si_dig = False
            #3
            cant_n = 0
            cant_a = False
            #4
        else:
            cant_letras += 1
            #1
            if digitos(car):
                cant_digitos +=1
            elif car.islower():
                cant_min += 1
            #2
            if digitos(car):
                si_dig = True
            #3
            if car in "Nn":
                cant_n += 1
            if cant_letras <= 4 and car in "AÀaà":
                cant_a = True
            #4
            if car in "sS":
                si_s = True
            else:
                if si_s and car in "EèÈe":
                    si_se = True
                si_s = False


    #prints
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
if __name__ == "__main__":
    principal()