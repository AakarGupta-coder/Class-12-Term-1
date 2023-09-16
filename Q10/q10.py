def binaryconversion(number):
    binary = bin(number)
    print(number,'in binary system =', binary[2:])
    	
def octalconversion(number):
    octal = oct(number)
    print(number,'in octal system =', octal[2:])

def hexadecimalconversion(number):
    hexadecimal = hex(number)
    print(number,'in hexadecimal system =', hexadecimal[2:])

num = int(input('Enter a number: '))
op = input('Enter the desired type conversion (B/O/H): ')
if op == 'b' or op == 'B':
    binaryconversion(num)
elif op == 'o' or op == 'O':
    octalconversion(num)
elif op == 'h' or op == 'H':
    hexadecimalconversion(num)
else:
    print('Invalid type conversion.')
    exit
