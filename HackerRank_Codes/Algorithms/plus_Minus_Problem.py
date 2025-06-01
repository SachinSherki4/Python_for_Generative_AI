

def plusMinus(arr):
    # Write your code here
    plus=minus=zero=0
    result=[]
    for i in range(0, len(arr)):
        if arr[i]==0:
            zero +=1
        elif arr[i]>0:
            plus +=1
        else:
            minus +=1
    print(plus/len(arr))
    print(minus/len(arr))
    print(zero/len(arr))

if __name__ == '__main__':
    n = int(input("Array Length : ").strip())

    arr = list(map(int, input("Input Elements : ").rstrip().split()))
    print(arr)
    plusMinus(arr)
