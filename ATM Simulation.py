"""CSC 161: Object Oriented Design

Blessing Babajide
Lab Section TR 12:30 - 1:45pm
Fall 2019
"""

from graphics import GraphWin, Text, Rectangle, Entry, Point
import time

class ATMachine:

    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
        return True

    def deposit(self, amount):
        self.balance += amount

        return self.balance


class User:

    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

    def get_user_id(self):
        return self.user_id

    def get_pin(self, user_id):
        return users[user_id]


def make_acc():
    print("Welcome to the ATM. Make your accounts before proceeding: ")
    users = dict()
    ans = "yes"
    while ans != "no":
        user_id = input("Enter username: ")
        pin = int(input("Enter pin(digits only): "))
        while pin < 9999 and pin > 1000:
            balance = int(input("How much balance do you have: "))
            users[user_id] = pin, balance
            break
        else:
            print("sorry! pin has to be 4 digits. try again")
        ans = input("Another user?(yes/no): ")
    return users

# extra credit code function below

def graphics_version():         
    users = make_acc()
    print("You're ready to continue!")
    time.sleep(0.5)
    
    ans1 = "yes"
    while ans1 == "yes":
        win = GraphWin("ATMachine", 600, 500)
        win.setCoords(0.0, 0.0, 3.0, 4.0)
        Text(Point(1.4, 3.6), "Welcome to the ATM!").draw(win)
        message = Text(Point(1.7, 2.5), "What account would you like to open today(enter user id): ")
        message.draw(win)
        
        userid = Entry(Point(1.5, 2), 10)
        userid.draw(win)
        
        Rectangle(Point(2.1, 1.2), Point(2.5, 1.4)).draw(win).setFill("red")
        button = Text(Point(2.3, 1.3), "next")
        button.draw(win)
        win.getMouse()
        userid.undraw()

        if userid.getText() in users:
            message.setText("Enter pin for user: ")
            pin = Entry(Point(1.5, 2), 10)
            pin.setText("0.0")
            pin.draw(win)
            win.getMouse()
            pin_, bal = users[userid.getText()]
            if float(pin.getText()) == pin_:
                person = User(userid, pin, bal)
                money = ATMachine(bal)
                message.setText("Enter 1 to withdraw, 2 to deposit, 3 for balance")
                pin.undraw()
                option = Entry(Point(1.5, 2), 10)
                option.setText("0")
                option.draw(win)
                win.getMouse()
                if float(option.getText()) == 1:
                    message.setText(("Enter amount to withdraw: "))
                    option.undraw()
                    amount = Entry(Point(1.5, 2), 10)
                    amount.setText(" ")
                    amount.draw(win)
                    win.getMouse()
                    amount = eval(amount.getText())
                    if money.withdraw(amount):
                        message2 = Text(Point(1.5, 1.8), "{0} withdrawn! closing balance ${1}".format(amount, bal-amount))
                        message2.draw(win)
                        win.getMouse()
                    else:
                        win.getMouse()
                        message2 = Text(Point(1.5, 2), "Insufficient funds in your account")
                        message2.draw(win)
                        win.getMouse()
                elif float(option.getText()) == 2:
                    message.setText("Enter amount to deposit: ")
                    option.undraw()
                    amount = Entry(Point(1.5, 2), 10)
                    amount.setText(" ")
                    amount.draw(win)
                    win.getMouse()
                    amount = float(amount.getText())
                    money.deposit(amount)
                    message2 = Text(Point(1.5, 1.8), "Deposit of amount {0} successful!, closing balance ${1}".format(amount, money.check_balance()))
                    message2.draw(win)
                    win.getMouse()
                    message2.setText(" ")
                elif float(option.getText()) == 3:
                    option.undraw()
                    message2 = Text(Point(1.5, 1.8), "Your account balance is ${0}".format(money.check_balance()))
                    message2.draw(win)
                    win.getMouse()
                    message2.setText(" ")            
            else:
                error = Text(Point(1.7, 2.7), "invalid combination try again: ")
                error.draw(win)
        else:
            win.getMouse()
            error = Text(Point(1.7, 2.7), "user not found try again: ")
            error.draw(win)
        message.setText("Would you like to make another transaction? (yes/no)")
        ans = Entry(Point(1.5, 2), 10)
        ans.setText(" ")
        ans.draw(win)
        win.getMouse()
        ans1 = str(ans.getText())
          
    win.close()
    print("Thank you for using this ATM. Have a nice day")


def main():
    users = make_acc()
    print("You're ready to continue!")
    while True:
        userid = input("What account would you like to open today(enter user id):  ")
        if userid in users:
            pin = int(input("Enter pin for user: "))
            pin_, bal = users[userid]
            if pin == pin_:
                person = User(userid, pin, bal)
                money = ATMachine(bal)
                while True:
                    option = int(input("Enter 1 to withdraw, 2 to deposit, 3 for balance, 4 to quit: "))
                    if option == 1:
                        amount = float(input("Enter amount to withdraw: "))
                        if money.withdraw(amount):
                            print("{0} withdrawn! closing balance {1}".format(amount, bal-amount))
                        else:
                            print("Insufficient funds in your account")
                    elif option == 2:
                        amount = float(input("enter amount: "))
                        money.deposit(amount)
                        print("Deposit of amount {0} successful!, closing balance {1}".format(amount, money.check_balance()))
                    elif option == 3:
                        print("Your account balance is {0}".format(money.check_balance()))

                    elif option == 4:
                        print("Thank you! Hope you had a nice time!")
                        # implementation of extra credit code by choice below
                        tres = input("Would you like to see a tentative graphical representation of this program(yes/no)?: ")
                        if tres == "yes":
                            graphics_version()
                        else:
                            print("hmm okay have a nice day still!")
            else:
                print("invalid combination try again: ")
        else:
            print("user not found try again: ")

if __name__ == '__main__':
    main()
