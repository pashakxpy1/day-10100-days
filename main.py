myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
ptips=float(input("what % of tip: "))
answer = round(myBill / numberOfPeople,2)
total = answer + answer * ptips/100
print("You all owe", answer, "and totla=", total)