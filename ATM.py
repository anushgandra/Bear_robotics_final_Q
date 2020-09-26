class ATM(object):
    def __init__(self):
        self.acc_num = 0
        self.action = 0
        self.balance = 0
        self.card_number = 0
        self.transaction()

    def check_card_insertion(self):
        '''
        Checks whether card is inserted properly or not, runs in a loop till card is inserted
        :return: True or False
        '''
        raise NotImplementedError()

    def get_card_num(self):
        '''
        Gets card number from card inserted
        :return: Card number
        '''
        raise NotImplementedError()

    def insert_card(self):
        '''
        checks whether the card is inserted properly and updates self.card_number
        :return: nothing
        '''
        print("Insert card to begin")
        while (self.check_card_insertion() == False):
            print("Card is inserted incorrectly. Insert card again")
        self.card_number = self.get_card_num()

    def check_PIN(self, pin_num):
        '''
        Checks whether pin number is valid or not
        :param pin_num: pin number to check
        :return: True or False
        '''
        raise NotImplementedError()

    def get_PIN_number(self):
        '''
        Verifies the PIN number entered
        :return: nothing
        '''
        x = input("Enter PIN number: ")
        x = int(x)
        while(self.check_PIN(x)==False):
            x = input("Sorry Wrong PIN entered.\nEnter PIN number again: ")
            x = int(x)

    def get_all_accounts(self):
        '''
        Get all accounts associated with card number(self.card_number)
        :return: list of all account options, a list of ints where each int corresponds to an account
        '''
        raise NotImplementedError()

    def check_acc_option(self, acc_opts, option):
        '''
        checks whether a valid account is selected
        :param acc_opts: possible account options
        :param option: selected option
        :return: True or False
        '''
        if (option in acc_opts):
            return True;
        return False;

    def get_acc_number(self, option):
        '''
        Gets the account number of the account chosen from list of accounts associated with self.card_number
        :param option: account chosen from the list of accounts, type int
        :return: account number
        '''
        raise NotImplementedError()

    def choose_account(self):
        '''
        Gets the account number of the account chosen and updates acc_num
        :return: Nothing
        '''
        acc_opts = self.get_all_accounts()
        x = input("Choose which account you would like to view: ")
        x = int(x)
        while(self.check_acc_option(acc_opts, x)==False):
            x = input("Sorry option not available.\nChoose which account you would like to view: ")
            x = int(x)
        self.acc_num = self.get_acc_number(x)


    def check_action(self):
        '''
        Checks whether selected action is correct or not
        :return: True or False
        '''
        if(self.action!=1 and self.action!=2 and self.action!=3):
            return False;
        return True;

    def choose_action(self):
        '''
        Allows you to choose withdrawl/deposit/view_balance
        :return: Nothing
        '''
        x = input("Choose one of the following:\nPress 1 to see balance\nPress 2 to deposit money\nPress 3 to withdraw money: ")
        self.action = int(x)
        while(self.check_action()==False):
            x = input("Sorry action not available\n.Choose one of the following:\nPress 1 to see balance\nPress 2 to deposit money\nPress 3 to withdraw money: ")
            self.action = int(x)


    def retrieve_balance(self):
        '''
        retrieves balance in account using self.acc_num for account number
        :return: balance in the account
        '''
        raise NotImplementedError()

    def withdraw_balance(self, amount):
        '''
        Withdraws money from account using self.acc_num for account number, controls hardware
        :param amount: amount to withdraw
        :return: nothing
        '''
        raise NotImplementedError()

    def update_balance(self):
        '''
        Updated balance in account using self.acc_num for account number and self.balance for new balance
        :return: nothing
        '''
        raise NotImplementedError()

    def insert_money(self):
        '''
        Function to communicate with hardware and insert money into account specified by self.acc_num
        :return: Nothing
        '''
        raise NotImplementedError()

    def perform_action(self):
        '''
        Performs the action selected: Withdrawal/deposit/view balance and updates the balance in the account
        :return: Nothing
        '''
        self.balance = self.retrieve_balance()
        if(self.action==1):
            print("Available balance in your account is: ", self.balance)
        elif(self.action==2):
            x = input("How much would you like to withdraw? : ")
            x = int(x)
            if(x<=0 or x>self.balance):
                x = input("Sorry invalid amount entered for withdrawal. How much would you like to withdraw? : ")
                x = int(x)
            self.withdraw_balance(x)
            self.balance -= x
        elif(self.action == 3):
            deposit_amount = self.insert_money()
            self.balance += deposit_amount
        self.update_balance()
        print("Available balance in your account is: ", self.balance)

    def transaction(self):
        '''
        Function that does the entire transaction
        :return:
        '''
        self.insert_card()
        self.get_PIN_number()
        self.choose_account()
        self.choose_action()
        self.perform_action()
        print("Transaction complete, have a nice day and do not forget to take your card")






















