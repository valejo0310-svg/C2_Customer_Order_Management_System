from First_registration import customer_registration  #Importing the registration of the customer's function
#Creation of the main function
#Function used to call all the other functions on the main archive
accumulated_tuple =()
print ("""
    ==========================================
      ~ welcome to the registration system ~ 
    ==========================================
    """.center(60))
accumulated_tuple = customer_registration (accumulated_tuple)
print (accumulated_tuple)
