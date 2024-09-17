from termcolor import colored # type: ignore
import time
import math
from fractions import Fraction
import devCodes
import random
import pickle
import os

MEMORY_FILE = 'memory.pkl'

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, 'rb') as file:
                return pickle.load(file)
        except (EOFError, pickle.PickleError) as e:
            print(colored(f"Error loading memory: {e}", "red"))
            return {}
    return {}

def save_memory(memory):
    try:
        with open(MEMORY_FILE, 'wb') as file:
            pickle.dump(memory, file)
    except IOError as e:
        print(colored(f"Error saving memory: {e}", "red"))

def clear_memory():
    global memory
    memory = {}
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
    print(colored("Memory cleared.", "cyan"))

def store_in_memory(key, result):
    global memory
    memory[key] = result
    save_memory(memory)
    print(colored(f"Stored in memory: {key} = {result}", "cyan"))

def list_memory():
    if not memory:
        print(colored("No results stored in memory.", "red"))
        return
    print(colored("Stored results:", "cyan"))
    for idx, (key, value) in enumerate(memory.items(), 1):
        print(f"{idx}: {key} = {value}")

def view_memory(index):
    if 1 <= index <= len(memory):
        key = list(memory.keys())[index - 1]
        print(colored(f"{key}: {memory[key]}", "cyan"))
    else:
        print(colored("Invalid selection. Please enter a valid index.", "red"))

def get_color_for_number():
    colors = {
        1: 'red',
        2: 'green',
        3: 'yellow',
        4: 'blue',
        5: 'magenta',
        6: 'cyan',
        7: 'white',
        8: 'grey',
        9: 'light_red',
        10: 'light_green'
    }
    number = random.randint(1, 10)
    return number, colors.get(number, 'white')

def display_banner():
    banner = """
                                                             
,-.----.                                                     
\\    /  \\            ,----..               ,--,              
|   :    \\          /   /   \\            ,--.'|              
|   |  .\\ :        |   :     :           |  | :              
.   :  |: |        .   |  ;. /           :  : '              
|   |   \\ :    .--,.   ; /--`   ,--.--.  |  ' |      ,---.   
|   : .   /  /_ ./|;   | ;     /       \\ '  | |     /     \\  
;   | |`-', ' , ' :|   : |    .--.  .-. ||  | :    /    / '  
|   | ;  /___/ \\: |.   | '___  \\__\\/:: . .'  : |__ .    ' /   
:   ' |   .  \\  ' |'   ; : .'| ," .--.; ||  | '.'|'   ; :__  
:   : :    \\  ;   :'   | '/  :/  /  ,.  |;  :    ;'   | '.'| 
|   | :     \\  \\  ;|   :    /;  :   .'   \\  ,   / |   :    : 
`---'.|      :  \\  ;`---`    `--`---'              `----'   
  `---`       `--`                                          
    """
    print(colored(banner, get_color_for_number()[1]))
    print(devCodes.Time())
def ask_yes_no(question):
    while True:
        response = input(f"{question} (0 = No, 1 = Yes): ").strip()
        if response in ('0', '1'):
            return response == '1'
        print(colored("Invalid input. Please enter 0 or 1.", "red"))

def ask_for_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print(colored("Invalid input. Please enter a valid number.", "red"))
        except SyntaxError:
            print(colored("Syntax error. Please enter a valid number.", "red"))

def ask_for_fraction(prompt):
    while True:
        try:
            return Fraction(input(prompt).strip())
        except ValueError:
            print(colored("Invalid input. Please enter a valid fraction (e.g., 1/2).", "red"))
        except SyntaxError:
            print(colored("Syntax error. Please enter a valid fraction.", "red"))

def perform_operations(number1):
    print(colored('Lets Do Some Math', 'cyan'))
    print('---------------------------------------------------------------------------------')

    if ask_yes_no('Do Trigonometry'):
        try:
            sin_val = math.sin(math.radians(number1))
            cos_val = math.cos(math.radians(number1))
            tan_val = math.tan(math.radians(number1))
            print(f"Sine of {number1}: {sin_val}")
            print(f"Cosine of {number1}: {cos_val}")
            print(f"Tangent of {number1}: {tan_val}")
            print('---------------------------------------------------------------------------------')
            store_in_memory('Trigonometry', {'sine': sin_val, 'cosine': cos_val, 'tangent': tan_val})
        except ValueError as e:
            print(colored(f"Math error: {e}", "red"))

    if ask_yes_no('Do Logarithms'):
        log_base = ask_for_number('Enter Log Base (e.g., 10 for log base 10): ')
        try:
            log_val = math.log(number1, log_base)
            print(f"Logarithm base {log_base} of {number1}: {log_val}")
            print('---------------------------------------------------------------------------------')
            store_in_memory('Logarithm', log_val)
        except ValueError as e:
            print(colored(f"Math error: {e}", "red"))
        except ZeroDivisionError:
            print(colored("Log base cannot be zero.", "red"))

    if ask_yes_no('Do Factorial'):
        if number1.is_integer() and number1 >= 0:
            try:
                factorial_val = math.factorial(int(number1))
                print(f"Factorial of {int(number1)}: {factorial_val}")
                store_in_memory('Factorial', factorial_val)
            except OverflowError as e:
                print(colored(f"Overflow error: {e}", "red"))
        else:
            print(colored("Factorial is only defined for non-negative integers.", "red"))
        print('---------------------------------------------------------------------------------')

    if ask_yes_no('Check if Prime'):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        try:
            prime_check = is_prime(int(number1))
            print(f"{int(number1)} is {'a prime number' if prime_check else 'not a prime number'}.")
            print('---------------------------------------------------------------------------------')
            store_in_memory('Prime Check', prime_check)
        except ValueError as e:
            print(colored(f"Value error: {e}", "red"))

    if ask_yes_no('Generate Random Number'):
        try:
            random_start = int(input('Enter starting range for random number: ').strip())
            random_end = int(input('Enter ending range for random number: ').strip())
            random_number = random.randint(random_start, random_end)
            print(f"Random number between {random_start} and {random_end}: {random_number}")
            print('---------------------------------------------------------------------------------')
            store_in_memory('Random Number', random_number)
        except ValueError as e:
            print(colored(f"Value error: {e}", "red"))

def perform_fraction_operations():
    print(colored('Fraction Math Operations', 'cyan'))
    print('---------------------------------------------------------------------------------')

    fraction1 = ask_for_fraction("Give a Fraction (e.g., 1/2): ")
    fraction2 = ask_for_fraction("Give Another Fraction (e.g., 1/3): ")

    if ask_yes_no('Do Fraction Math'):
        try:
            print(f"Added Fraction: {fraction1 + fraction2}")
            print(f"Subtracted Fraction: {fraction1 - fraction2}")
            print(f"Multiplied Fraction: {fraction1 * fraction2}")
            print(f"Divided Fraction: {fraction1 / fraction2}")
            store_in_memory('Added Fraction', fraction1 + fraction2)
            store_in_memory('Subtracted Fraction', fraction1 - fraction2)
            store_in_memory('Multiplied Fraction', fraction1 * fraction2)
            store_in_memory('Divided Fraction', fraction1 / fraction2)
        except ZeroDivisionError:
            print(colored("Cannot divide by zero in fraction operations.", "red"))

def perform_basic_operations(number1, number2):
    print(colored('Basic Arithmetic Operations', 'cyan'))
    print('---------------------------------------------------------------------------------')

    if ask_yes_no('Divide'):
        try:
            result = number1 / number2
            print(f"Divided: {result}")
            store_in_memory('Divided Number', result)
        except ZeroDivisionError:
            print(colored("Cannot divide by zero.", "red"))

    if ask_yes_no('Add'):
        result = number1 + number2
        print(f"Added: {result}")
        store_in_memory('Added Number', result)

    if ask_yes_no('Subtract'):
        result = number1 - number2
        print(f"Subtracted: {result}")
        store_in_memory('Subtracted Number', result)

    if ask_yes_no('Multiply'):
        result = number1 * number2
        print(f"Multiplied: {result}")
        store_in_memory('Multiplied Number', result)

    if ask_yes_no('Exponentiate'):
        result = number1 ** number2
        print(f"Exponentiated: {result}")
        store_in_memory('Exponentiated Number', result)

    if ask_yes_no('Modulus'):
        result = number1 % number2
        print(f"Modulus: {result}")
        store_in_memory('Modulus Number', result)

def main():
    global memory
    memory = load_memory()

    display_banner()
    print(colored('Hello', 'red'), colored('World', 'green'))
    time.sleep(1)

    number1 = ask_for_number("Give a Number: ")
    perform_operations(number1)

    number2 = ask_for_number("Give Another Number: ")
    perform_basic_operations(number1, number2)

    perform_fraction_operations()

    print('---------------------------------------------------------------------------------')
    print(colored('Math is done!', 'green'))

    while True:
        print('\nWhat would you like to do?')
        print('1: List Memory')
        print('2: View Specific Memory')
        print('3: Clear Memory')
        print('4: Exit')
        choice = int(input('Enter your choice: ').strip())

        if choice == 1:
            list_memory()
        elif choice == 2:
            list_memory()
            try:
                index = int(input('Enter the number of the item to view: ').strip())
                view_memory(index)
            except ValueError:
                print(colored("Invalid input. Please enter a number.", "red"))
        elif choice == 3:
            clear_memory()
        elif choice == 4:
            print(colored("Exiting program.", "cyan"))
            break
        else:
            print(colored("Invalid choice. Please select a valid option.", "red"))

if __name__ == "__main__":
    main()
