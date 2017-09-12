choice = raw_input('Enjoying the course? (y/n)')
while choice != "y" or choice != "n":
  if choice == "y" or choice == "n":#fill in the condition
    print("pass")
    break
else:
    choice = raw_input("Sorry I didn't catch that.  Enter again: ")