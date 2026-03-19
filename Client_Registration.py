def customer_registration (accumulated_tuple):
    predetermined_tuple = ({
    "Customer's ID " : "0001",
    "Customer's name " : "Guest", 
    "Customer's Email" : "Guest0001@gmail.com"
},)
    n = int(input("how many clients do you want to register?: "))
    print ("CUSTOMER REGISTRATION")
    for i in range(n):
        print("customer", i+1)

        ID_valido = False #Variable 
        while ID_valido == False:
                try:
                    
                    customer_ID = int (input ("Please enter customer's ID:"))
                    if customer_ID < 0: 
                        print("The ID can not be negative nor a 0.")
                    else:
                        break  
                except ValueError:
                    print ("Please enter the right value.") 

        name = input("Customer's name: ")
        email = input("Customer's email: ")

        customer = {
            "Customer's ID " :customer_ID,
            "Customer's name " : name, 
            "Customer's Email" : email
        }

        accumulated_tuple = accumulated_tuple + (customer,)

    print (predetermined_tuple)
    return accumulated_tuple
   
