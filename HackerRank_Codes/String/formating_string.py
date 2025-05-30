

def formatting_string(number):
    width= len(bin(number)[2:])  # bin(5) = 0b101 [2:] remove 0b so width = 3
    for i in range(1,number+1):
        o= oct(i)[2:] # [2:] is to remove the prefix 0O
        h = hex(i)[2:]
        h = h.upper()
        b = bin(i)[2:]
        d =str(i)
        print(f"{d:>{width}} {o:>{width}} {h:>{width}} {b:>{width}}")

if __name__ == '__main__':
    n = int(input())
    formatting_string(n)