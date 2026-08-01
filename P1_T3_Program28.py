# Movie ticket price calculator.

def Calculator(Ticket_Price,No_of_tickets,Age):
    Price = None

    if (Age == "Child"):
        Price = Ticket_Price * 0.5
    elif (Age == "Senior"):
        Price = Ticket_Price * 0.8
    else:
        Price = Ticket_Price

    Final_Price =  Price * No_of_tickets
    
    return Final_Price

def main():
    Ticket_Price = 200

    No_of_tickets = int(input("Enter the number of tickets : "))
    Age = input("Enter the age catagory(Child/Adult/Senior)")

    Ret = Calculator(Ticket_Price,No_of_tickets,Age)

    print(f"The final ticket price is {Ret}")

if __name__=="__main__":
    main()