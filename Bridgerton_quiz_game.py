print("Welcome to the Bridgerton Quiz Game!")

playing = input("Dear Gentle Reader, Would you like to play?(yes/no)").lower()

if playing != "yes":
    print("BYE!! BIRDIE!!")
    quit()

print("Great!! Let's play!!")
score = 0

answer = input("What is the name of the eldest Bridgerton sibling?").lower()



if answer == "anthony":
    print("Correct!!")
    score +=1
else:
    print("Wrong!!")

answer = input("What was the real identity of Lady Whistledown?").lower()

if answer == "penelope featherington".lower():
    print("Correct!!")
    score +=1
elif answer == "penelope".lower() or answer == "penelope bridgerton".lower():
    print("Correct!!")
    score +=1
else:
    print("Wrong!!")

answer = input("What is the name of the Duke of Hastings?").lower()
if answer == "Simon".lower():
    print("Correct!!")
    score +=1
else:
    print("Wrong!!")
    
answer = input("Who does Francesca Bridgerton marry?").lower()
if answer == "Lord Kilmartin".lower():
    print("Correct!!")
    score +=1 
else:
    print("Wrong!!")
    
    
print("You got", score, "questions correct!!")
print("BYE!! BIRDIE!!")