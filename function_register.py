def function_register(accumulated_tuple):
    print("PRODUCT REGISTRATION")
    product_counter = 1 
    continue_ciclo = "yes"
    products = (
        {
            "ID" : "5",
            "nombre": "leche",
            "price" : "5000"
        },
        {
            "ID" : "6",
            "nombre": "pan",
            "price" : "3000"
        },
        {
            "ID" : "7",
            "nombre": "queso",
            "price" : "2500"
        },
        {
            "ID" : "8",
            "nombre": "mantequila",
            "price" : "4000"
        },
        {
            "ID" : "10",
            "nombre": "lechuga",
            "price" : "4500"
        }
    )
    
    while continue_ciclo == "yes":
        print(f"-------- Product {product_counter} --------")
        try:
            id_product = int(input("Enter the product ID: "))
            
            if id_product <= 0:
                print("The ID must be a positive number.")
                continue # Reinicia el ciclo para pedir el ID de nuevo

            product_name = input("Enter the product name: ")
            unit_price = float(input("Enter the price of the product: "))

            # Creamos el diccionario
            product = {
                "ID": id_product,
                "nombre": product_name,
                "price": unit_price
            }

            # Guardamos el diccionario dentro de la tupla (concatenación)
            accumulated_tuple = accumulated_tuple + (product,)
            
            product_counter += 1
            continue_ciclo = input("Desea registrar otro producto? (yes/no): ").lower()

        except ValueError:
            print("Please enter a valid numeric value.")
            
    return accumulated_tuple # ¡Importante devolver la tupla actualizada!
