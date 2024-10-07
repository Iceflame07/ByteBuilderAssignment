'''
generate random subtraction problem and present the question for them correctly and save
prompt the computer to output random questions and save
Prompt the user to attempt each problem up to 10 times and save
Prompt the user to answer and provide feedback correct or incorrect and save
prompt the computer to calculate and display the user final score after all attempt and save
'''

import random

number1 = random.randint(1,10)
print(number1)

number2 =[random.randrange(1,10) for i in range(0,10)]
print(number2)


