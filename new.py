word_count=[]
let_count=[]

a=input("enter the sentence here = ")
for i in a.split():
    word_count.append(i)
    let_count.append(len(i))
print("total number of words in sentence are ",len(word_count))
print("total number of letters in sentence are ",sum(let_count))