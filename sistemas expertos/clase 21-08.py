def diagnosticar():
    print("=== Sistema Experto Diagnóstico de Fallas en un Automóvil ===\n")
    
    reglas = {
        "no_arranca_sin_luces": "Batería descargada",
        "no_arranca_con_luces": "Fallo en el motor de arranque",
        "arranca_se_apaga": "Problema en el suministro de combustible",
        "humo_negro": "Mezcla rica de combustible",
        "humo_blanco": "Falla en la junta de culata"
    }

    while True:
        arranca = input("¿El auto arranca? (si/no): ").lower()
        if arranca == "no":
            luces = input("¿Las luces del tablero encienden? (si/no): ").lower()
            if luces == "no":
                print("\nPosible causa:", reglas["no_arranca_sin_luces"])
            else:
                print("\nPosible causa:", reglas["no_arranca_con_luces"])

        elif arranca == "si":
            apaga = input("¿Se apaga al acelerar? (si/no): ").lower()
            if apaga == "si":
                print("\nPosible causa:", reglas["arranca_se_apaga"])
            else:
                humo = input("¿El auto expulsa humo por el escape? (si/no): ").lower()
                if humo == "si":
                    color = input("¿Color del humo? (negro/blanco/otro): ").lower()
                    if color == "negro":
                        print("\nPosible causa:", reglas["humo_negro"])
                    elif color == "blanco":
                        print("\nPosible causa:", reglas["humo_blanco"])
                    else:
                        print("\nNo se reconoce el tipo de humo. Requiere revisión.")
                else:
                    print("\nEl auto no presenta fallas conocidas en la base de reglas.")
        else:
            print("Respuesta inválida, intenta de nuevo.")

        otra = input("\n¿Desea realizar otro diagnóstico? (si/no): ").lower()
        if otra != "si":
            print("\nGracias por usar el Sistema Experto de Diagnóstico de Fallas")
            break

diagnosticar()