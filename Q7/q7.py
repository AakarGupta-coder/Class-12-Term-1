#(a)
def count(n):
    return len(str(n))
#(b)
def reverse(n):
    return int(str(n)[::-1])
#(c)
def hasdigit(n):
    return any(c.isdigit() for c in str(n))
#(d)
def show(n):
    digits = [int(d) for d in str(n)]
    expanded_form = ' + '.join([f"{digits[i]} * 10^{len(digits)-i-1}" 
    for i in range(len(digits))])
    return expanded_form
# Main program
try:
    num = int(input("Enter a number: "))
    print("Number of digits:", count(num))
    print("Reverse of the number:", reverse(num))
    print("Has digit:", hasdigit(num))
    print("Expanded form:", show(num))
except ValueError:
    print("Invalid input. Please enter a valid number.")
