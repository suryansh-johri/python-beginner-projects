while True:
    import random
    counter=0
    print(
    """Welcome to robo world 
    Let's start the Game""")
    x=input("""
    1. To start the Game
    2. To read instruction 
            
    """)
    if x=="1":
        random_num=random.randint(1,100)
        # print(random_num)
        while True:
            guess=int(input("enter the number : "))
            counter=counter+1
            if random_num==guess:
                break 
            elif guess>random_num:
               print("Guess smaller number")
            else:
               print("Guess larger number")
        if counter==3:
            print("Hurray , U WON ")
        else:
            print("number of attempts : ",counter)
            print("Better luck next time")
    if x=="2":
     print("""
    Guess the Number
            
    Game Instructions

    1.The game chooses one number between 1 and 100.

    2.The player must guess the number.

    3.The player gets only three chance.

    🏆 Result

    1. If the guess is correct, you win 🎉

    2. If the guess is wrong, better luck next time 🙂

    📜 Rules

    1.Guess only three times.

    2.Enter a number from 1 to 100.

    3.No 4th chance.

    💡 Example

    Game number: 25

    Your guess: 25 → You win

    Your guess: 10 → Better luck next time""")
