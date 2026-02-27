# FILE NAME - coin_toss.py
# NAME: Nicholas Thurston
# DATE: 2/26/2026
# BRIEF DESCRIPTION: Coin Toss Program
# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience
########## ENTER YER CODE BELOW THIS LINE ##########

import random

def main():
    def coin_toss():
        # random number between 1 and 100
        num = random.randint(1,100)

        # start coin flip
        print('===== Coin Flipper =====')

        # coin flip logic
        if num >= 51:
            print("Tails")
        else:
            print("Heads")


    coin_toss()
main()








########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

The hardest part was remembering the proper method from the random module.





'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[X] I pretty much get it.
[ ] I'm solid. Totally got it.
'''
