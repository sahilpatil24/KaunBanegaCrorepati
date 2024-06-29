print("Welcome to Kaun Banega Crorepati")
name = input("Enter your name: ")
l = [[
    "Name the summer capital of Jammu and Kashmir?",
    ["Srinagar", "Jammu", "Leh", "Gulmarg"], "Srinagar"
],
     [
         "Name the gas which is filled in balloons?",
         ["Nitrogen", "Oxygen", "Helium", "Carbon Dioxide"], "Helium"
     ],
     [
         "Who was the first Prime Minister of India?",
         [
             "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Vallabhbhai Patel",
             "Rajendra Prasad"
         ], "Jawaharlal Nehru"
     ],
     [
         "Who was the first woman Prime Minister of India?",
         ["Sonia Gandhi", "Sarojini Naidu", "Pratibha Patil", "Indira Gandhi"],
         "Indira Gandhi"
     ],
     [
         "Name the deepest ocean in the world?",
         ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean"],
         "Pacific Ocean"
     ]]

print("Hello", name)
print("\n\nThere will be 5 questions in this game")
print("Each question will have 4 options")
print("You have to enter the choice from a to d")

choice = 'c'
questionAnsweredCorrectly = 0
for i in range(5):
    print("here is question no:", i + 1)
    print(l[i][0])
    print("Here are the options:")
    for j in range(4):
        if j == 0:
            print("a. ", end=" ")
            print(l[i][1][j])
        elif j == 1:
            print("b. ", end=" ")
            print(l[i][1][j])
        elif j == 2:
            print("c. ", end=" ")
            print(l[i][1][j])
        elif j == 3:
            print("d. ", end=" ")
            print(l[i][1][j])

    print("\nEnter the answer(from option a to d in lowercase): ", end=" ")
    choice = input()
    if choice == "a":
        if l[i][1][0] == l[i][2]:
            print("Your answer is correct\n")
        else:
            print("Your answer is wrong.\nBetter luck next time. :)")
            break
    if choice == "b":
        if l[i][1][1] == l[i][2]:
            print("Your answer is correct\n")
        else:
            print("Your answer is wrong.\nBetter luck next time. :)")
            break
    if choice == "c":
        if l[i][1][2] == l[i][2]:
            print("Your answer is correct\n")
        else:
            print("Your answer is wrong.\nBetter luck next time. :)")
            break
    if choice == "d":
        if l[i][1][3] == l[i][2]:
            print("Your answer is correct\n")
        else:
            print("Your answer is wrong.\nBetter luck next time. :)")
            break
    questionAnsweredCorrectly = questionAnsweredCorrectly + 1

print("Prize Won:", questionAnsweredCorrectly * 5000)
