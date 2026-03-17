def customer_registration (customer_ID, client_name, email): 
#Function created to allow the system to register the client's information
#Parameters to show all the local variables
    registration = {
        "ID" : customer_ID,
        "customer" : client_name,
        "email" : email
    }#Dictionary used to store all the client's data entere (Id, customer's name and email)
    return registration 