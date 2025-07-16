import random
name = input("Enter your name:")
print("Hello "+name," ,Let's start the quiz!")

q = [
    ("#What is the ouput of 2+3?", ["a)4", "b)5", "c)6", "d)3"], "b"),
    ("# Which keyword is used to define a function?", ["a)func", "b)define", "c)def", "d)function"], "c"),
    ("# What is the symbol used to write a comment in python?", ["a)#", "b)/*", "c)<!--", "d)//"], "a"),
    ("#Which data type is immutable?", ["a)list", "b)dict", "c)tuple", "d)set"], "c"),
    ("# How to create a list?", ["a)(1,2,3)", "b)[1,2,3]", "c){1,2,3}", "d)<1,2,3>"], "b"),
    ("# Which is the Largest planet?", ["a)Mars", "b)Earth", "c)Saturn", "d)Jupiter"], "d"),
    ("# Opposite of hot?", ["a)warm", "b)Cold", "c)Cool", "d)Heat"], "b"),
    ("# How many days in a week?", ["a)5", "b)6", "c)7", "d)8"], "c"),
    ("# Which cricket player is known as the run mission?", ["a)dhoni", "b)ashwin", "c)suresh raina", "d)virat kolhi"], "d"),
    ("# What is the output of 10/2?", ["a)5", "b)3", "c)1", "d)8"], "a")
]

random.shuffle(q)
s = 0
for i in q:
    print(i[0]); [print(o) for o in i[1]]
    a = input("Ans (a/b/c/d): ")
    if a == i[2]: s += 1

print("Score:", s, "/10")
print("Thank you for playing!")
      
