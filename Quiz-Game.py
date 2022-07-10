import time

print("Welcome to the quiz\n")

question_1 = "Who was the first President of India ?"
question_2 = "Who was the first Prime Minister of India ?"
question_3 = "Which language is the oldest ?"
question_4 = "Which river is the biggest in the world ?"
question_5 = "In which city Statue Of Liberity located ?"


correct_ans_1 = "rajendra prasad"
correct_ans_2 = "jawaharlal nehru"
correct_ans_3 = "sanskrit"
correct_ans_4 = "amazon river"
correct_ans_5 = "new york"

score = 0

end_statement = "Thank you for participating in our quiz"

while (True):
    start_game = str(input("Do you want to start the game? (y/n) :"))
    
    if (start_game == "y"):
        
        for i in range(1,4):
            print(f"The quiz will start in {i}")
            time.sleep(1)

        print("")
        print("Here is your first question")
        print("")
        time.sleep(0.5)
        
        ##### Question 1
        user_ans1 = str(input(f"{question_1} :"))
        user_ans1 = user_ans1.lower()
        if (user_ans1 == correct_ans_1):
            score += 1
            # OR score = score + 1
        else:
            pass
        
        ##### Question 2
        user_ans2 = str(input(f"{question_2} :"))
        user_ans2 = user_ans2.lower()
        if (user_ans2 == correct_ans_2):
            score += 1
        else:
            pass
        
        ##### Question 3
        user_ans3 = str(input(f"{question_3} :"))
        user_ans3 = user_ans3.lower()
        if (user_ans3 == correct_ans_3):
            score += 1
        else:
            pass
        
        
        ##### Question 4
        user_ans4 = str(input(f"{question_4} :"))
        user_ans4 = user_ans4.lower()
        if (user_ans4 == correct_ans_4):
            score += 1
        else:
            pass
        
        ##### Question 5
        user_ans5 = str(input(f"{question_5} :"))
        user_ans5 = user_ans5.lower()
        if (user_ans5 == correct_ans_5):
            score += 1
        else:
            pass
        
        print("")
        time.sleep(1)
        
        score_statement = f"your total score is {score} / 5"
        
        if (score == 5):
            print(end_statement)
            print(f"Amazing! {score_statement}")
        elif (score == 4):
            print(end_statement)
            print(f"Excellent! {score_statement}")
        elif (score == 3):
            print(end_statement)
            print(f"Good job! {score_statement}")
        else:
            print(end_statement)
            print(f"{score_statement} . Better luck next time! ")
        
        break

    elif (start_game != "y") and (start_game != "n"):
        print("Sorry I could not understand")

    else:
        break

