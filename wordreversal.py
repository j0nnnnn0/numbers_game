# Ask the user to enter a word and write a program that reverses the word and prints the result. 
# For example, if the user enters "Python," the program should output "nohtyP."

# prompt the user to enter a word, which we'll treat as a string
word = str(input("Enter a word: "))

# In Python, strings are sequences of characters, and you can access individual characters within a string using indexing.
# The syntax [start:stop:step] is used to slice a sequence in Python. 
# In the case of word[::-1], the slicing is done as follows:
# - start is not specified, which means it defaults to the beginning of the sequence.
# - stop is not specified, which means it defaults to the end of the sequence.
# - step is -1, indicating that the slicing should be done in reverse order.
# - So, when word[::-1] is used, it returns a new string that contains all the characters of word, but in reverse order.
reversed_word = word[::-1]

# rekcuf taht tnirp :-)
print(f"the word reversal is {reversed_word}")