#0. Input
input1 = 'books.txt' #text file that contains names of all bible books
input2 = 'text.txt'  #text file containing the paragraph with hidden bible book names to find

#1. bible books
with open(input1,'r') as input_file:
    list_of_books = [line.strip() for line in input_file] #remove whitespace before and after string

#2. the paragraph
with open(input2, 'r') as test_file:
    test = test_file.read()
#filter(func a,iterable b) applies 'func a' to each item in b, and returns 'True' or 'False'. Then joins all 'True' values together. 
test = ''.join(filter(str.isalpha, test)) #remove everything but alphabets

#3. check if base[i] in test
i = 1
for book in list_of_books:
    if str(book).lower() in test.lower():
        print(i,str(book))
        i += 1

#4. Quit
quit = input("Press <enter> to quit:")

        
#Testing
#print(base)
#print(type(base))

#print(test)
#print(type(test))