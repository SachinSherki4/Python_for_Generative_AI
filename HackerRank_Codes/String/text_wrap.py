import textwrap

def wrpt_text(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input("enter continous string"), int(input("enter max width"))
    index=[i for i in range(1, len(string)+1,max_width)]
    print(index)
    print(len(string))
    print(wrpt_text(string, max_width))



