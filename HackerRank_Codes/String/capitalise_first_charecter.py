

def solve(s):
    if s and len(s) < 1000:
        words=s.split()
        capitalize_words=[]
        for word in words:
            if word and word[0].isalpha():
                capitalize_words.append(word[0].upper()+word[1:])
            elif word and word[0].isalnum():
                capitalize_words.append(word)
        return " ".join(capitalize_words)

print(solve("heLLo 123abc hi"))

