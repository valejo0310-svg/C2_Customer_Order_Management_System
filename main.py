from First_registration import customer_registration #Importing the registration of the customer's function

#~~~ Text Styles for console ~~~#

# Basic formatting
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
UNDER   = "\033[4m"
BLINK   = "\033[5m"
INVERT  = "\033[7m"

# Text colors (30-37)
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

#Creation of the main function
#Function used to call all the other functions on the main archive
def main ():#Welcome message to the system
    print (f"""{MAGENTA}{BOLD}
╔═══════════════════════════════════════════════════════════╗{RESET}
                {GREEN}{BOLD}🥑 RIWIMART RETAIL CHAIN 🥑{RESET}
   {MAGENTA}🌷 Welcome to the Customer Order Management System! 🌷
╚═══════════════════════════════════════════════════════════╝{RESET}""") #Some text formatting is used to make the welcome message more attractive
    Option= 0
    while Option<= 0 :#Loop created to keep asking the user when they enter a wrong option
        try:          #Try and except created to catch the error when the user enters a non-integer value    
            Option = int(input(f"""{MAGENTA}{BOLD}{"-"*24} MAIN MENU {"-"*25}{RESET} 
{GREEN}1) 🤵​  Enter Costumer 
2) 🍎  Enter Product 
3) ​🧾​  Create Order
4) ​🔍​  View Orders
5) 💀​  Quit {RESET}
{MAGENTA}{BOLD}{"="*60}{RESET}
{GREEN}~ Please select an option:
➤ {RESET} """)) 
            if Option < 1 or Option > 5: #Condition created to catch the error when the user enters a number that is not on the menu
                print(f"\n{RED}{BOLD}{'❌ ERROR: Please enter a valid number ❌':^60}{RESET}\n") 
                Option = int(input(f"""{MAGENTA}{BOLD}{"-"*24} MAIN MENU {"-"*25}{RESET} 
{GREEN}1) 🤵​  Enter Costumer 
2) 🍎  Enter Product 
3) ​🧾​  Create Order 
4) ​🔍  View Orders
5) 💀​  Quit {RESET}
{MAGENTA}{BOLD}{"="*60}{RESET}
{GREEN}~ Please select an option:
➤ {RESET} """))     
        except ValueError:
            print(f"\n{RED}{BOLD}{'❌ ERROR: Please enter a valid integer ❌':^60}{RESET}\n")

    #First condition created to call the function of the customer's registration when the user selects the first option of the menu.
    #if Option == 1:
        

        



main ()#Calling the main function
