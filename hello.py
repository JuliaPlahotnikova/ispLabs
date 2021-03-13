import logging

logging.basicConfig(level=logging.INFO)


def main():
    while True:
        sign = input("Sign (+,-,*,/): ")
        if sign == "0":
            break
            
        if sign in ("+", "-", "*", "/"):
            try: 
                number1 = float(input("First number: "))
                number2 = float(input("Second number: "))
            except ValueError:
                logging.error("Invalid number, try again!")
                continue
                
        if sign == "+":
            logging.info("%s", number1 + number2)
        elif sign == "-":
            logging.info("%s", number1 - number2)
        elif sign == "*":
            logging.info("%s", number1 * number2)
        elif sign == "/":
            if number2 != 0:
                logging.info("%s", number1 / number2)
                
            else:
                logging.info("Division by zero!")
        else:
            logging.info("Invalid operation sign!")
            return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.error("Exit")
