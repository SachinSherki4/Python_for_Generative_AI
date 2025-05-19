
def printing_numbers(n):
    print("Starting Printing numbers : ")
    printn(n)

def printn(n):
    if n > 5:
        return
    print(n)
    # This is last function in call, it dont do anything just handover the flow to printn(n+1) function, it is
    # upto this function to continue further -  it is call tail recursion.
    printn(n+1)

printing_numbers(1)