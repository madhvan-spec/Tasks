# Word Frequency Counter    
import string
with open('task8file.txt' , 'r' , encoding='utf-8') as f:
    word_list = [word.strip(string.punctuation).lower() for line in f for word in line.strip().split()]
    # print(word_list)    
word_count = {}
for i in word_list:
    if i in word_count:
        word_count[i] +=1
    else:
        word_count[i] = 1

print(word_count)
    

        