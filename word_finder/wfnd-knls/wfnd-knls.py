def finder(text,dictionary):
    words = []
    #count = 0
    for entry in dictionary:
        t_index = -1
        for letter in text:
            cache = ''
            t_index+=1
            if letter == entry[0].lower():
                for i in range(len(entry)):
                    try:
                        cache += text[t_index+i]
                    except:
                        break
                if entry.lower() == cache:
                    words.append(entry)
                    break
                
    return words
    
def finderv2(text,dictionary):
    words = []
    for entry in dictionary:
        if entry.lower() in text:
            words.append(entry)
    return words
    
def extract_text(file):
    from string import ascii_letters as letters
    original_text = file.read().lower()
    file.close()
    text = ''
    for i in original_text:
        if i in letters:
            text += i
        else:
            continue
    return text
    
def get_file(prompt):
	filename = input(f"Name of file containing {prompt}: ")
	while True:
		try:
			file = open(filename,"r")
		except:
			filename = input("That file does not exist on the disk. Try again.\nEnter file name: ")
		else:
			break
	return file
	
def dictionarize(input):
	result = input.strip("\n").split(",")
	return result

file = get_file("text")
text = extract_text(file)
dictionary = dictionarize(get_file("dictionary").read())

result = finder(text,dictionary)
count = 0

for i in result:
    count+=1
    if count <= 9:
        print(f"  {count}. {i}")
    if count <=99 and count > 9:
        print(f" {count}. {i}")
    if count <=999 and count > 99:
        print(f"{count}. {i}")
