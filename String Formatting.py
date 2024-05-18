def print_formatted(number):
    number_stack = ""
    width = len(bin(number)) - 1
    for i in range(1, number + 1):
        number_stack += str(i).rjust(width - 1)
        number_stack += str(oct(int(i)))[2:].rjust(width)
        number_stack += str(hex(int(i)))[2:].upper().rjust(width)
        number_stack += str(bin(int(i)))[2:].rjust(width) + "\n"
    print(number_stack[:-1])

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)