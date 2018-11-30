# 201358937 Tonge_Brandon-CA06.py
# November 2018
# This program will accept multiple user inputs regarding the production of a stage show.
# It will then calculate how long it will take to make a profit if the show has a full
# house every night. It also give the option to generate 5 days where a random number of
# seats have been sold (over 40%) and then use the average to again predict the number of
# days until a profit is made.

import random
import math

# Main Function
def main():

    # Main Menu
    print("\n---Main Menu---")
    print("A - Theatre")
    print("E - Extend")
    print("X - Exit Program")
    print("")
    choice = str.upper(input("Please select an option from the menu: "))

    # TEST
    # print(choice)

    # Function Selection
    if(choice == "A"):
        theatre()

    elif(choice == "E"):
        extended()

    elif(choice == "X"):
        exit()

    else:
        print("\nPlease enter a valid choice!\n")
        main()


# Theatre Function
def theatre():

    # Accept the users inputs
    while True:
        prod_cost = input("\nPlease enter the overall cost of the production: £")
        try:
            prod_cost = float(prod_cost)
            break
        except:
            print("\nPlease enter a valid number!")
            continue

    print("\nWhat is the cost of tickets in -")
    while True:
        bandA = input("Band A: £")
        try:
            bandA = float(bandA)
            break
        except:
            print("\nPlease enter a valid number!")
            continue

    while True:
        bandB = input("Band B: £")
        try:
            bandB = float(bandB)
            break
        except:
            print("\nPlease enter a valid number!")
            continue

    while True:
        bandC = input("Band C: £")
        try:
            bandC = float(bandC)
            break
        except:
            print("\nPlease enter a valid number!")
            continue

    while True:
        drinkws = input("\nPlease enter the wholesale cost of drinks: £")
        try:
            drinkws = float(drinkws)
            break
        except:
            print("\nPlease enter a valid number!")
            continue

    while True:
        programws = input("\nPleas enter the wholesale cost of programs: £")
        try:
            programws = float(programws)
            break
        except:
            print("\nPlease enter a valid number!")
            continue

    # User choice in which function to run
    while True:
        print("\n- Show Turnout -")
        print("Assume full house   =  1")
        print("Assume random house =  2")
        choice = input("Please choose an option: ")
        if(choice == "1" or choice == "2"):
            try:
                choice = int(choice)
                break
            except:
                print("Please enter one of the options below!")
                continue
        else:
            print("Please enter one of the options below!")
            continue


    if(choice == 1):
        fullhouse(prod_cost, bandA, bandB, bandC, drinkws, programws)

    else:
        randomhouse(prod_cost, bandA, bandB, bandC)

    main()


# Full House Function
def fullhouse(prod_cost, bandA, bandB, bandC, drinkws, programws):

    # Create list with a full house
    numc = 5
    numr = 5
    seats = [[1 for row in range(numr)] for col in range(numc)]

    # Test
    print()
    for i in range(numr):
        print(seats[i])

    # Count how many seats are filled for each reference in seats
    seats_filled = sum(i.count(1) for i in seats)

    # Money made per each band and consumables
    prof_banda = float((seats[0].count(1) + (seats[1].count(1))) * bandA)
    prof_bandb = float((seats[3].count(1) + (seats[3].count(1))) * bandB)
    prof_bandc = float((seats[4].count(1)) * bandC)
    prof_drinks = float(drinkws + (drinkws / 2))
    prof_programs = float(programws + (programws / 4))
    overall_drinks = float(seats_filled * prof_drinks)
    overall_programs = float(math.ceil(float(seats_filled / 2)) * prof_programs)

    # Test
    # print(prof_banda, prof_bandb, prof_bandc)

    print("\n- Seat Sales Alone - ")
    # Overall price of seats for the night
    overall_band = float(prof_banda + prof_bandb + prof_bandc)
    print(f"The total for seat sales is = £{overall_band}")
    print(f"- Band A = £{prof_banda}")
    print(f"- Band B = £{prof_bandb}")
    print(f"- Band C = £{prof_bandc}")

    # Days until a profit is made
    days_profit = math.ceil(float(prod_cost / overall_band))
    print(f"With production costing £{prod_cost} it will take {days_profit} days to make a profit.")

    # Print seats and consumables for the night
    print("\n- Seat and Consumables -")
    print(f"The total for seat sales is = £{overall_band}")
    print(f"The drinks sales are = £{overall_drinks}")
    print(f"The program sale are = £{overall_programs}")

    # Days until a profit is made
    days_profit2 = math.ceil((float(prod_cost / (overall_band + overall_drinks + overall_programs))))
    print(f"With production costing £{prod_cost} it will take {days_profit2} days to make a profit.")
    main()


# Random House Function
def randomhouse(prod_cost, bandA, bandB, bandC):

    prof_banda = 0
    prof_bandb = 0
    prof_bandc = 0

    # Create list and randomly populate it
    for i in range(5):
        numc = 5
        numr = 5

        seats = [[0 for row in range(numr)] for col in range(numc)]

        # Populate the list with 10 - 25 "1" in randomly selected positions
        for pos in random.sample(range(25), random.randint(10, 25)):
            seats[pos // 5][pos % 5] = 1

        # Test print
        print()
        print(f"   - Day {i + 1} -")
        for i in range(numr):
            print(seats[i])


        # Money made per each band
        prof_banda = prof_banda + float(((seats[0].count(1)) + (seats[1].count(1))) * bandA)
        prof_bandb = prof_bandb + float(((seats[2].count(1)) + (seats[3].count(1))) * bandB)
        prof_bandc = prof_bandc + float((seats[4].count(1)) * bandC)


    # Test
    # print("\n", prof_banda, prof_bandb, prof_bandc)

    # Overall price of seats for the night
    average_band = (float(prof_banda + prof_bandb + prof_bandc)) / 5
    print(f"The average profit over five nights is = £{average_band}")

    # Days until a profit is made
    days_profit = math.ceil(float(prod_cost / average_band))
    print(f"With production costing £{prod_cost} it will take {days_profit} days to make a profit.")

    main()


# Extended Function
def extended():

    print("Extended")
    main()


main()