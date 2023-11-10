print("***Palindrome Tester***")
print("How does it work?")
print("When prompted, type the palindrome. Type '0' to exit the system and '1' to check the palindromes you have passed in")
print("\n")

def palindrome(word):
    mainword = word.lower()
    for i in range (0, len(mainword)):
        if mainword[i] == mainword[len(word) - (i+1)]:
            continue
        else:
            return False
    return True

palindromes = []

while True:
    word = str(input("Type in your palindrome: "))
    if word == "0":
        break
    elif word == "1":
        print("Palindromes: ")
        for item in palindromes:
            print(item)
    else:
        if palindrome(word):
            palindromes.append(word)
            print(word, "is a palindrome.")
        else:
            print(word, "is not a palindrome.")
    print("")