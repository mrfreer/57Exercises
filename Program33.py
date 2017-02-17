import random
#Magic 8 Ball

answers = ['Yes','No','Maybe','Ask again later']
input("What's your question?")
print(answers[random.randint(1,4)])
