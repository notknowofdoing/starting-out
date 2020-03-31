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
