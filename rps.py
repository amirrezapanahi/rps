#!/usr/bin/env python
#
#


"""
    rock paper scissors with an ai
    ai will already have made its mind up as to which option to choose
    countdown will take place from 3 .. 1
    get user input in the form ("r" = rock, "p" = paper, "s" = scissors)
    if user doesnt input anything within that timeframe then restart the round
    repeat 3 times as its best of 3
    count the scores at the end and display who the winner is

"""

import time
import readchar
import random

done = 0
valid = ['r', 'p', 's']
humanScore = 0
aiScore = 0


def sleep(x):
    time.sleep(x)


def countdown():
    options = ["rock", "paper", "scissors", "SHOOT!"]
    for i in range(0, len(options)):
        sleep(0.7)
        print(options[i])


def validate(input):
    if input not in valid:
        return False
    else:
        return True


# i want a flag that tracks the rock papers scissors shoot and once it reaches shoot then read the inputs

def ai():
    ai_option = random.choice(valid)
    return ai_option


def results(ai, input):
    if validate(input):
        print("")
        print("You: " + input)
        print("AI : " + ai)
        print("")
    else:
        print("")
        print("You: N/A")
        print("AI : N/A")
        print("")


def outcome(ai, input, done):

    global aiScore
    global humanScore

    outcome1 = ["r", "p"]
    outcome2 = ["r", "s"]
    outcome3 = ["p", "s"]

    if ai == input:
        print("Tie!")
    else:
        if all(x in outcome1 for x in [ai, input]):
            if ai == "p":
                aiScore = aiScore + 1
            else:
                humanScore = humanScore + 1

            done = done + 1

        if all(x in outcome2 for x in [ai, input]):
            if ai == "r":
                aiScore = aiScore + 1
            else:
                humanScore = humanScore + 1

            done = done + 1

        if all(x in outcome3 for x in [ai, input]):
            if ai == "s":
                aiScore = aiScore + 1
            else:
                humanScore = humanScore + 1

            done = done + 1

    print("You: " + str(humanScore) + "     " + "AI: " + str(aiScore))
    print()

    return done


def countscores(aiScore, humanScore):
    return aiScore > humanScore


def main():
    global input
    global done

    play = str(input("play? y/n "))
    if play == "y":
        print()
        while done != 3:
            countdown()
            human = readchar.readkey()
            airesult = ai()
            results(airesult, human)
            done = outcome(airesult, human, done)

        if countscores(aiScore, humanScore):
            print("AI wins")
        else:
            print("Human wins")


if __name__ == "__main__":
    # execute only if run as a script
    main()
