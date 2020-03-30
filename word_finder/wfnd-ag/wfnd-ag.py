#1. bible books
with open('books.txt','r') as input_file:
    base = [line.strip() for line in input_file] #remove whitespace,'\n' and put into list with words in each line as list elements
#print(base)
#print(type(base))

#2. the paragraph
with open('text.txt', 'r') as test_file:
    test = test_file.read().lower()
test = ''.join(filter(str.isalpha, test)) #remove everything but alphabets
#print(test)
#print(type(test))

#3. check if base[i] in test
i = 1
for x in base:
    if str(x).lower() in test:
        print(i,str(x))
        i += 1

#4. Quit
quit = input("Press <enter> to quit:")

        

