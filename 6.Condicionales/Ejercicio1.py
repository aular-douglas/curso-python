letra = input("Ingrese una letra: ")

'''if letra.lower() == "a":
    print ("Es una vocal")
else:
    if letra.lower() == "e":
        print ("Es una vocal")
    else:
        if letra.lower() == "i":
            print ("Es una Vocal")
        else:
            if letra.lower() == "o":
                print ("es una vocal")
            else:
                if letra.lower() == "u":
                    print ("Es una vocal")
                else:
                    print ("No es una vocal")'''

if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("NO es una vocal")
