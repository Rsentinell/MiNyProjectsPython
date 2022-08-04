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
    print("This program is checking if the two inputs are Anagram")
    inpText1 = input("Enter your first input: ")
    inpText2 = input("Enter your second input: ")

    temp1 = inpText1.replace(" ", "").lower()
    temp2 = inpText2.replace(" ", "").lower()
    
    if temp1==temp2:
        print(True)
    else:
        print(False)
    repeat = yesOrNo()
