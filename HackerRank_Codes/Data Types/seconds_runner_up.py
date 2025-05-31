
if __name__=='__main__':
    n=int(input("Enter input size of array : ")) # enter array size
    arr= map(int, input("Enter all scores with comma seperated : ").split(" ")) # enter same input as size specify
    print(f"from highest to lowest {sorted(set(arr))}")
    print(sorted(set(arr),reverse=True)[1])



