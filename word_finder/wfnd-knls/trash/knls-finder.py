def finder(text,dictionary):
    words = []
    #count = 0
    for entry in dictionary:
        t_index = -1
        for letter in text:
            cache = ''
            t_index+=1
            if letter == entry[0]:
                for i in range(len(entry)):
                    try:
                        cache += text[t_index+i]
                    except:
                        break
                if entry == cache:
                    words.append(entry)
                    break
                
    return words


def finderv2(text,dictionary):
    words = []
    for entry in dictionary:
        if entry.lower() in text:
            words.append(entry)
    return words
