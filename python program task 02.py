age = int(input("Enter your age:"))
voter_id = input("Do you have a Voter ID? (yes/no): ")
if age>=18:
    print("you can eligible")
if voter_id == "yes":
    print("You can vote.")
else:
    print("You can't vote.")
