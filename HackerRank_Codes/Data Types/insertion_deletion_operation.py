
if __name__ == '__main__':
    ar=[]
    n=int(input("Enter number of operation you wants to perform"))
    for  _ in range(n):
        comm_arg=input().strip().split(" ") #
        cmd=comm_arg[0] # first index always contain operation wants to perform
        if cmd=="print":
            print(ar)
        elif cmd == "reverse":
            ar.reverse()
        elif cmd == "pop":
            ar.pop()
        elif cmd == "insert":
            pos=int(comm_arg[1])
            value = int(comm_arg[2])
            ar.insert(pos, value)
        elif cmd == "remove":
            val = int(comm_arg[1])
            ar.remove(val)
        elif cmd == "append":
            valu= int(comm_arg[1])
            ar.append(valu)
        elif cmd =="sort":
            ar.sort()