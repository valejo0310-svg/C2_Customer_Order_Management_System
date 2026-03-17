from First_registration import customer_registration #Importing the registration of the customer's function
#Creation of the main function
#Function used to call all the other functions on the main archive
def main ():
    print ("""
    ==========================================
      ~ welcome to the registration system ~ 
    ==========================================
    """.center(60)) #Welcome message to the system
    #Variables created to store all the client's data such as Id, names and emails
    customer_ID = input ("Please enter customer's ID:")
    client_name = input ("\nPlease enter the customer's name: ")
    email = input ("\nPlease enter the customer´s email: ")
    #Creation of the variable "customer" to call the registration function
    customer = customer_registration(customer_ID, client_name, email) 
    print (customer)#Print used to show the variable that contains the costumer's info



main ()#Calling the main function