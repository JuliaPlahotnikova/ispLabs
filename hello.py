import logging
logging.basicConfig(level=logging.INFO)

def main():
    while True:
     sign = input("Sign (+,-,*,/): ")
     if sign == '0':
          break
     if sign in ('+', '-', '*', '/'):
           number1 = float(input("First number: "))
           number2 = float(input("Second number: "))
     if sign == '+':
            result = number1 + number2
            logging.info(f'{result}')
     elif sign == '-':
             result = number1 - number2
             logging.info(f'{result}')
     elif sign == '*':
             result = number1 * number2
             logging.info(f'{result}')
     elif sign == '/':
             if number2 != 0:
                result = number1 / number2
                logging.info(f'{result}')
             else:
                logging.info('Division by zero!')
     else:
        logging.info('Invalid operation sign!')
        return
        
if __name__ == '__main__':
    main()
