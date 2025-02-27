with open("C:\\Users\\C605\\Desktop\\1000words.txt","r")as file:
   line=file.readline()

words_line=line.strip()
words=[word.split('"') for word in words_line.split(",")]
def print_words_first_letters(words,firstletters):
    print(f"Words starts with letters {firstletters}:")
    for word_list in words:
        for word in word_list:
         if (word.lower().startswith(firstletters.lower())):
            print(word)
            found=True
    if not found:
        print("There is no words match with these starting letters")
print_words_first_letters(words,"e")
print_words_first_letters(words,"ha")

print("Please enter a number")
x= int(input())
if(3<=x<=9):
 for i in range(1,x):
    print("*"*i)
 for i in range(x,0,-1):
    print("*"*i)
else:
    print("You can not enter numbers lower than3 or higher than 9")
