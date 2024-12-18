"1. Write a program which will find factors of given number and find whether the\
factor is even or odd.\
Hint: Use Loop with if-else statements"

# def find_factors_and_check_odd_or_even(number):
#     print(f"Factors of {number}:")
#     for i in range(1,number+1):
#         if number % i == 0:
#             if i % 2 == 0:
#                 print(f"{i} is Even")
#             else:
#                 print(f"{i} is Odd")
#
# try:
#     num=int(input("Enter a positive integer:"))
#     if num > 0:
#         find_factors_and_check_odd_or_even(num)
#     else:
#         print("Enter a positive integer")
# except ValueError:
#     print("Invalid input. Please enter a positive integer")


"2. Write a code which accepts a sequence of words as input and prints the words in a\
sequence after sorting them alphabetically.\
Hint: In case of input data being supplied to the question, it should be assumed to\
be a console input"\

# words=input("Enter a sequence of words separated by spaces: ")
# words_list=words.split()
# print(words_list)
# sorted_words= sorted(words_list)
# print("Sorted words: ",",".join(sorted_words))

"3. Write a program, which will find all the numbers between 1000 and 3000 (both\
included) such that each digit of a number is an even number. The numbers\
obtained should be printed in a comma separated sequence on a single line.\
Hint: In case of input data being supplied to the question, it should be assumed to\
be a console input. Divide each digit with 2 and verify is it even or not"\

# def is_all_digit_even(number):
#     for digit in str(number):
#         if int(digit) % 2 != 0:
#             return False
#     return True
# even_digit_number=[str(num) for num in range(1000,3001) if is_all_digit_even(num)]
# print(",".join(even_digit_number))

"4. Write a program that accepts a sentence and calculate the number of letters and\
digits.\
Suppose if the entered string is: Python0325\
Then the output will be:\
LETTERS: 6\
DIGITS:4\
Hint: Use built-in functions of string."\

# def count_letters_and_digits(input_string):
#     letters = 0
#     digits = 0
#     for char in input_string:
#         if char.isalpha():
#             letters+=1
#         elif char.isdigit():
#             digits+=1
#     return letters, digits
#
# input_string= input("Enter a sentence: ")
# letters, digits= count_letters_and_digits(input_string)
# print(f"LETTERS: {letters}")
# print(f"DIGITS: {digits}")

"5. Design a code which will find the given number is Palindrome number or not.\
Hint: Use built-in functions of string."\

s=input("Enter a string:")
for i in range(0,len(s)//2):
    if(s[i] != s[len(s)-i-1]):
        found=False
        break
else:
    found=True
if found:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")






