import re

String = input("Enter a String: ")
String = String.replace(" ", "")
String = re.sub("[@#!$&*()_+/.,<>?:';]", "", String)
S2 = String[::-1]
if String == S2:
    print("palindrome")
else:
    print("Not a palindrome")
print(String)
