class ATM:
    def __init__(self, PIN = " ", Balance = 0):
        self.pin = PIN
        self.balance = Balance
        

    def bank_balance(self):
      
        self.balance = int(input("enter amount :"))
        print("your balance : ",self.balance)
       


    def menu(self):
        user_input = input(
            """ Hi how can I help you?
                1. Press 1 to create pin
                2. Press 2 to change pin
                3. Press 3 to check balance
                4. Press 4 to withdraw
                5. Anything else to exit  \n : """
        )
        
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("enter a new pin : ")

        confirm_pin = input("enter confirm  pin : ")

        if user_pin == confirm_pin:
            self.pin = user_pin
            
            print("pin is created succesfully")
            self.menu()
        else:
            print("not match new pin and confirm pin")
            self.create_pin()
            
    

    def change_pin(self):
        old = input("enter old pin : ")
        if old == self.pin:
            print("correct pin")
            set_pin = input("enter a new set_pin : ")
            confirm_set_pin = input("enter confirm set_pin : ")
            if set_pin == confirm_set_pin:
                self.pin = set_pin
                print("succesfully new pin is created")
                print("\n want to check_balance(enter yes or no)")
            
                request = input("enetr yes or no :")
                if request == "yes".lower() :
                    self.check_balance()
                elif request == "no".lower():
                    self.menu()
            else:
                print("New pin do not match")
        else:
            print("incorrect pin")
            self.change_pin()

    def check_balance(self):
        user_pin = input("Enter your pin : ")
        if user_pin == self.pin:
            print("correct pin")
            print("your bank balance : ",self.balance)
            self.menu()
            
   
        else:
            print("incorrect pin")
            self.check_balance()

            
    def withdraw(self):
        user_pin = input("enter your pin : ")
        if self.pin == user_pin:
            print("correct pin")
            amount = int(input("enter amount : "))
            if amount<= self.balance:
                self.balance = self.balance - amount
                print("withdrawl successfully : ",amount ,"\n your bank_balance : " ,self.balance)
                self.menu()
            else:
                print("not have enough money")
        else:
            print("incorrct pin")
            self.withdraw()
            

atm = ATM("1234",5000)
atm.menu()

           


        





           

        



    


        



            

            









    

    
        



