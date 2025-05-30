

def count_substring(full_string, sub_string):
    count=0
    if len(full_string) < 200:
        for i in range(len(full_string)- len(sub_string) +1):
            if full_string[i : i+len(sub_string)] == sub_string:
                count += 1
    return count


if __name__ == '__main__':
    full_string = input().strip()
    sub_string = input().strip()

    count = count_substring(full_string, sub_string)
    print(count)


