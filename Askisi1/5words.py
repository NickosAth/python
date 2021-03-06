import re

def removeVowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u')  
    newWord = word
    for vowel in vowels:
        newWord = newWord.replace(vowel, "")
    return newWord    

with open("random.txt","r") as a:      
    data = a.read().split()
a.close()
#lower all chars for no duplicate words at sorting process
data =[word.lower() for word in data]
#special chars remove
data =[word.strip('.,')for word in data]
#remove duplicates
data = list(set(data))
#sort(The list is sorted based on the length of the element, from the lowest count to highest.)
data.sort(reverse=True,key=len)
#we need to keep the 5 biggest words
data = data[0:5]

#remove vowels(a,e,i,o,u)

data =[removeVowels(word) for word in data]

for word in data:
#[-1::-1](It starts from the end and once a time it moves one letter left(-1) ) 
    word =word[-1::-1]
    print(word)
