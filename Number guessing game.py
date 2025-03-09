message=int(input("Enter a number= "))
correct_number= 9
guess_count=0
max_no_of_attempts=2
while guess_count < max_no_of_attempts:
    print("Guess")
    guess_count += 1
    if message==correct_number:
        print("U have gotten the right answer")

else:
    print("Incorrect, keep trying")


