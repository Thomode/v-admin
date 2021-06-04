import json

ruta_config = "/etc/v2ray/config.json"
#ruta_config = "config_br.json"

def clients_list(user_seller):
    try:
        with open(ruta_config, "r") as file_r:
            config = json.load(file_r)
            file_r.close()

            users = config["inbounds"][0]["settings"]["clients"]

        cont_client = 1

        for client in users:
            try:
                email = client["email"]
                id_client = client["id"]

                name, seller = email.split("@")

                if seller == user_seller:
                    if cont_client > 0 and cont_client < 10:
                        message_client = "0" + str(cont_client) + ") " + id_client + "    " + name
                    else:
                        message_client = str(cont_client) + ") " + id_client + "    " + name

                    print(message_client)
                    cont_client += 1
            except:
                pass
    except:
        print("Archivo no encontrado")

def clients_search(name_search, user_seller):
    name_search = name_search.lower()
    name_search_len = len(name_search)

    try:
        with open(ruta_config, "r") as file_r:
            config = json.load(file_r)
            file_r.close()
            users= config["inbounds"][0]["settings"]["clients"]

        vali_client = False

        for client in users:
            try:
                email = client["email"]
                id_client = client["id"]

                name, seller = email.split("@")

                if user_seller == seller:
                    if name_search == name:
                        vali_client = True
                        print(id_client + " " + name)
                    else:
                        name_reg = ""
                        for i in range(name_search_len):
                            name_reg = name_reg + name[i]

                        if name_search == name_reg:
                            vali_client = True
                            print("\n" + id_client + " " + name)
            except:
                pass

        if not vali_client:
            print("Usuario no encontrado")

    except NameError:
        print("Archivo no encontrado")

def clients_register(user_seller):
    pass


def validation_seller(user_seller):
    with open(ruta_config, "r") as file_r:
        config = json.load(file_r)
        file_r.close()
        users_clients = config["inbounds"][0]["settings"]["clients"]

    vali_seller = False
    for client in users_clients:
        try:
            email = client["email"]
            name, seller = email.split("@")

            if user_seller == seller:
                vali_seller = True
        except:
            pass
    return vali_seller

def banner(user_seller=None):
    men = "V-ADMIN 1.0"
    length = 60

    print(length*"=")
    print(men.center(length))
    if user_seller != None:
        message_seller = "Bienvenido: " + user_seller
        print(message_seller.center(length))
    print(length*"=")

def menu(user_seller):
    op = "1"
    while op != "0":
        banner(user_seller)
        print("\n1) Mostrar Clientes",
              "\n2) Buscar Cliente",
              "\n0) Salir")
        op = input("\nIngresar opcion: ")
        print("")

        if op == "1":
            clients_list(user_seller)
            input("\nPresionar ENTER para continuar")

        elif op == "2":
            name_search = input("Ingresar el nombre o iniciales que desea buscar: ")
            clients_search(name_search, user_seller)
            input("\nPresionar ENTER para continuar")

        elif op == "0":
            print("Fin del programa")
        else:
            print("Opcion Invalida!")

def start():
    banner()

    vali = "1"
    while vali != "0":
        user_seller = input("\nIngresar usuario del vendedor (salir con 0): ")
        if user_seller == "0":
            vali = "0"
        else:
            vali_seller = validation_seller(user_seller)

            if vali_seller:
                vali = "0"
                menu(user_seller)
            else:
                print("Usuario del vendedor no registrado")

if __name__ == "__main__":
    start()


