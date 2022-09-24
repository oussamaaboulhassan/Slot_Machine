import random


#the rows are the width of the machine itself, cols are the number of columns in the machine.
ROWS = 3
COLS = 3
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


#the symbols in the slot machine, used a dict to illustrate the concept, we 2 have to A, 4 B... 
symbol_count= {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


#the symbol value gives us what every symbol is the slot machine worth.
symbol_value= {
    "A": 6,
    "B": 4,
    "C": 2,
    "D": 1,
}


#this fonction checks when the random happened, if the 3 symbols are the sam, if they are the same its a win otherwise its a lose.
#we have 3 lines in this game, this fonction checks each line and if we have any maching symbols, and it add the number of lines maching at the end.
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet   
            winnings_lines.append(line + 1) 
        return winnings, winnings_lines    


#the fonction call the random module and put the random value in the 1st list "column" and put the above in a 2nd list "columns".
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)   
    return columns


#this fonction prints out the value of the list "columns" from get_slot_machine_spin.
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()        


#this fonction accepts the int inputed by the user as a deposit amount.
def deposit():
    while True:
        amount = input("What would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater that 0! ")
        else:
            print ("Please enter a number. ")
    return amount            


#this fonction gets the number of lines that the user want to bet on (between 1 and 3)
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines! ")
        else:
            print ("Please enter a number. ")
    return lines   


#this fonction gets the betting amount from the user input and its between the MAX_BET and the MIN_BET.
def get_bet():
    while True:
        amount = input(f"What would you like to bet (${MIN_BET}-${MAX_BET}): $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print ("Please enter a number. ")
    return amount  


#this fonction have a balance parameter that's called from another fonction and it uses that parameter to check if you're out of money to bet and break the loop if so,
#and also print out the winnigs and the winning lines and return the the left from the deposit the user made.
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"Bet out of balance, your balance is ${balance}")     

    print(f"You are betting ${bet} on {lines} lines, your total bet is: ${total_bet}!")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!!!!")
    print(f"You won on lines: ", *winnings_lines)
    return winnings - total_bet


#this is the main fonction that gets the value of the deposit and controls if you want to play or quit.
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        spinnn = input("Press Enter to spin (q to quit ).")
        if spinnn == "q" or "quit":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")    




main()