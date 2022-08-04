repeat = True

def yesOrNo():
    i = 0
    while i < 2:
        answer = input("Do you want try again? (yes or no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            return True
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            return False
        else:
            i += 1
            if i < 2:
                print('Please enter yes or no')
            else:
                print("Nothing done")


while repeat:
    print("This program is checking if the input is Palindrome")
    inpText = input("Enter your input: ")
    # inpText = 'Hello World From Pankaj Hi There'
    temp = inpText.replace(" ", "").lower()
    print(temp)
    print("-------------")
    temp2 = temp[::-1]
    print(temp2)
    print("-------------")
    if temp==temp2:
        print(True)
    else:
        print(False)
    repeat = yesOrNo()






