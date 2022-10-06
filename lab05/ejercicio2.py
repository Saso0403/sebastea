try:
    file = input("Llame a su archivo\n>>>")
    openn = open(file, "r", encoding="UTF-8")

    for linea in openn:
        print(linea.upper())
except:
    print("Intente una vez mas")