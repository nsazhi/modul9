def all_variants(text):
    for n in range(len(text)):
        for i in range(len(text)):
            s = text[i: i + (n + 1)]
            try:
                text[i + n] in text
            except:
                break
            else:
                yield s
                i += 1
        n += 1


a = all_variants("abc")
for i in a:
    print(i)
