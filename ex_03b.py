budget = 0
budget_set = False

print("***Budget Calculator***")
print("Welcome to your budget calculator")
print("S - Set Budget, M - Deduct Expenditure, A - Add to Budget, R - Reset Budget, D - Display Budget, X - Exit")

while True:
    prompt = input("Please enter the desired prompt: ")
    if prompt == "X":
        break
    elif prompt == "S":
        if not budget_set:
            T = int(input("Please enter the desired budget: "))
            budget = T
            budget_set = True
        else:
            print("Budget Already Set. Press 'R' to Reset the budget")
    elif prompt == "M":
        expenditure = int(input("Please enter expenditure: "))
        if budget - expenditure < 0:
            print("Budget too small to perform deduction")
        else:
            budget -= expenditure
            print(expenditure, "has been deducted from your budget. ")
    elif prompt == "A":
        addition = int(input("Please enter added revenue: "))
        budget += addition
        print(addition, "has been added to your budget. ")
    elif prompt == "R":
        new_budget = int(input("Please enter new budget: "))
        budget = new_budget
    elif prompt == "D":
        print("Current value of budget:", budget)
    else:
        print("Invalid Key")
    print("")