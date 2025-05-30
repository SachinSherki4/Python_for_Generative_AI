
if __name__ == '__main__':
    string= input("Enter String")
    if string and len(string) < 1000:
        is_alnum=False
        is_digit=False
        is_alpha=False
        is_lower=False
        is_upper=False

        for i in string:
            if is_digit and is_alpha:
                is_alpha=True
            elif i.islower():
                is_lower=True
            elif i.isupper():
                is_upper=True
            elif i.isdigit():
                is_digit=True
            elif i.isalnum():
                is_alnum=True

        print(is_digit)
        print(is_alpha)
        print(is_alnum)
        print(is_upper)
        print(is_lower)


