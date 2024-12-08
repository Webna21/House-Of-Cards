# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Thomas Janes
#           Cameron King
#           Andrew Li
#           Gavin Munoz
# Section: ENGR-102-559
# Assignment: Team Design Project Fall 2024
# Date: 8 December 2024

import matplotlib.pyplot as plt
import numpy as np
import turtle as t

'''
This program calculates the total profit and percent error between expected and actual profit,
graphs the profit and percent error and outputs results to console,
graphs height vs. weight compared to previous teams,
graphs profit and percent error compared to previous teams,
appends results to "HouseofCards.csv" on the last row,
creates a .txt file with the results,
and generates drawing of the structure with turtle graphics.
'''

def costs():
    '''
    Calculates, prints, returns the cost.
    '''
    cards_purchased = int(input("\t\tCards purchased: "))
    rolls_of_tape = int(input("\t\tRolls of tape used: ") or 1)
    pairs_of_scissors = int(input("\t\tPairs of scissors used: ") or 1)
    time_beyond_25 = float(input("\t\tTime used beyond 25 minutes: ") or 0)
    print("Costs")
    print(f"Cards purchased:\t\t{cards_purchased} x $1000 each =\t{cards_purchased*1000}")
    print(f"Rolls of tape used:\t\t{rolls_of_tape} x $10000 each =\t{rolls_of_tape*10000}")
    print(f"Pairs of scissors used:\t\t{pairs_of_scissors} x $5000 each =\t{pairs_of_scissors*5000}")
    print(f"Time used beyond 25 minutes:\t{time_beyond_25} x $2000 each =\t{time_beyond_25*2000}")
    print(f"Total Costs:\t\t\t\t\t\t{cards_purchased*1000 + rolls_of_tape*10000 + pairs_of_scissors*5000 + time_beyond_25*2000}")
    return cards_purchased*1000 + rolls_of_tape*10000 + pairs_of_scissors*5000 + time_beyond_25*2000



def revenue():
    '''
    Calculates, prints, and returns the revenue.
    '''
    successfully_built = int(input("\t\tSucessfully built structure (Y/N): ") in ["Y",'y',"yes","YES","1"] or True)
    height = int(input("\t\tHeight above 36 inches: ") or 0)
    strength = int(input("\t\tPennies beyond 10: ") or 0)
    speed = int(input("\t\tAvailable time not utilized (minutes under 25): ") or 0)
    print("Revenue")
    print(f"Successfully built structure: \t\t\t\t{successfully_built} x $100000 = \t\t{successfully_built * 100000}")
    print(f"Height. Additional height (inches above 36): \t\t{height} x $2000 each = \t{height*2000}")
    print(f"Strength. Additional pennies (beyond 10): \t\t{strength} x $500 each = \t{strength*500}")
    print(f"Speed. Available time not utilized (minutes under 25): \t{speed} x $1000 each = \t{speed*1000}")
    print(f"Total Revenue: \t\t\t\t\t\t\t\t\t{successfully_built * 100000 + height*2000 + strength*500 + speed*1000}")
    return successfully_built * 100000 + height*2000 + strength*500 + speed*1000



def totalProfitcalculation():
    '''
    Calculates, prints, and returns the profit.
    '''
    cost = costs()
    rev = revenue()
    print(f"\nTotal Profit = Total Revenue - Total Costs = {rev} - {cost} = {rev-cost}")
    return rev-cost



def calculateTotalProfitAndAccuracy():
    '''
    Calculates, prints, and returns the expected profit, acutal profit, and percent error between them.
    '''
    print("Expected".center(100,"-"))
    expected = totalProfitcalculation()
    print("Actual".center(100,"-"))
    actual = totalProfitcalculation()
    print("Accuracy".center(100,"-"))
    print(f"Expected: \t{expected}\nActual: \t{actual}")
    percentError = abs((actual-expected)/expected) * 100
    print(f"Percent Error = (Actual - Expected)/(Expected) * 100% = {percentError:.3f}%")

    return expected, actual, percentError



def graphTotalProfitAndAccuracy(estimated, actual, percentError):
    '''
    Displays a bar graph of the expected profit, actual profit, and the percent error between them.
    '''
    pltx = np.arange(3)
    plt1y = np.array((estimated,actual,0))
    plt2y = np.array((0,0,percentError))

    axs1 = plt.subplot()
    
    l1 = axs1.bar(pltx,plt1y,color = "b", label = "Profit")
    axs1.set_ylabel(f"Profit (Thousand Dollars)")
    axs1.set_xticks(())
    # axs1.set_ylim(estimated-30,estimated+20)
    axs1.set_ylim(0, max(150, estimated, actual))
    axs1.set_xlabel(f"Expected profit: {estimated}k   |   Actual profit: {actual}k   |   Percent Error: {percentError:.3f}%")
    axs1.set_title("Profit and Percent Error")

    axs2 = axs1.twinx()
    l2 = axs2.bar(pltx,plt2y,color = "r", label = "Percent Error")
    axs2.set_ylabel("Pecent error (%)")
    axs2.set_ylim(0,100)
    axs1.legend((l1,l2), (l1.get_label(),l2.get_label()))

    plt.show()



def extractFileData():
    '''
    Extracts data from "HouseofCardsResults.csv" and returns the heights, pennies, profits, and profit accuracies.
    '''
    with open("HouseofCardsResults.csv") as file:
        for _ in range(2):
            file.readline()

        data = [row.strip().split(',') for row in file]
        
        profits = [int(row[1]) for row in data]
        profitAccuracies = [int(row[2][:-1]) for row in data]
        heights = [float(row[3]) for row in data]
        pennies = [int(row[4]) for row in data]
        

        return (heights, pennies), (profits, profitAccuracies)



def graphHeightWeightComparison(expectedPennies, expectedHeight):
    '''
    Displays a scatter plot illustrating previous teams' height vs. weight compared to our's.
    '''
    data, _ = extractFileData()
    heights = data[0]
    pennies = data[1]
    plt.grid(True)
    plt.scatter(pennies, heights, color="blue",label="Previous Teams")
    plt.title("Height vs. Weight")
    plt.xlabel("Pennies")
    plt.ylabel("Height (Inches)")
    plt.scatter(expectedPennies,expectedHeight,color="red",label="Our Team")
    plt.legend(loc="upper right")

    plt.show()



def graphProfitPercentErrorComparison(expectedProfit, profitPercentError):
    '''
    Displays a scatter plot illustrating previous teams' profit and percent error compared to our's.
    '''
    _, data = extractFileData()
    profits = data[0]
    profitAccuracies = data[1]
    plt.grid(True)
    plt.scatter(profits, profitAccuracies, color="blue",label="Previous Teams")
    plt.title("Profit and Profit Percent Error")
    plt.xlabel("Profit (Dollars)")
    plt.ylabel("Profit Percent Error (%)")
    plt.scatter(expectedProfit,profitPercentError,color="red",label="Our Team")
    plt.legend(loc="lower left")

    plt.show()



def appendTeamResultsCSV(actualProfit,profitPercentError,actualHeight,actualPennies):
    '''
    Appends our profit, precent error, height, and pennies to "HouseOfCardsResults.csv".
    '''
    with open("HouseofCardsResults.csv","a") as file:
        file.write(f"59,{actualProfit},{profitPercentError}%,{actualHeight},{actualPennies}")



def resultsToTxt(actualProfit,profitPercentError,actualHeight,actualPennies):
    '''
    Writes to "results.txt" our profit, percent error, height, and pennies.
    '''
    with open("results.txt","w") as file:
        file.write(f"Profit: {actualProfit}\n")
        file.write(f"Profit Percent error: {profitPercentError}%\n")
        file.write(f"Height: {actualHeight}\n")
        file.write(f"Pennies: {actualPennies}\n")



def cyl1():
    '''
    Draws a cylinder.
    '''
    t.color("White")
    t.width(2)
    t.pd()
    t.forward(15)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(15)
    t.right(180)

def cyl2():
    '''
    Draws a cylinder.
    '''
    t.color("White")
    t.width(2)
    t.pd()
    t.forward(14)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(14)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(14)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(14)
    t.right(180)
    
def cyl3():
    '''
    Draws a cylinder.
    '''
    t.color("White")
    t.width(2)
    t.pd()
    t.forward(12)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(12)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(12)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(12)
    t.right(180)

def leg1():
    '''
    Draws the first leg.
    '''
    t.goto(-100,-300)
    #1
    t.right(3)
    cyl1()
    #2
    t.right(3)
    cyl1()
    #3
    t.right(3)
    cyl1()
    #4
    t.right(2)
    cyl1()
    #5
    t.right(2)
    cyl1()
    #6
    t.right(2)
    cyl1()
    #7
    t.right(1)
    cyl1()
    #8
    t.right(1)
    cyl1()
    #9
    t.right(1)
    cyl1()
    #right by 18degs
    #10
    t.left(5)
    cyl1()
    #12
    t.left(6)
    cyl1()
    #13
    t.left(7)
    cyl1()
    #left by 18degs
    t.pu()
    
def leg2():
    '''
    Draws the second leg.
    '''
    t.goto(100,-250)
    t.left(3)
    cyl2()
    #2
    t.left(3)
    cyl2()
    #3
    t.left(3)
    cyl2()
    #4
    t.left(2)
    cyl2()
    #5
    t.left(2)
    cyl2()
    #6
    t.left(2)
    cyl2()
    #7
    t.left(1)
    cyl2()
    #8
    t.left(1)
    cyl2()
    #9
    t.left(1)
    cyl2()
    #left by 18degs
    #10
    t.right(5)
    cyl2()
    #12
    t.right(6)
    cyl2()
    #13
    t.right(7)
    cyl2()
    #right by 18degs
    t.pu()
    
def leg3():
    '''
    Draws the third leg.
    '''
    t.goto(0,-200)
    #1
    t.right(1)
    cyl3()
    #2
    t.right(2)
    cyl3()
    #3
    t.right(3)
    cyl3()
    #4
    t.right(2)
    cyl3()
    #5
    t.right(1)
    cyl3()
    #6
    t.left(.5)
    cyl3()
    #right by 19degs
    #7
    t.left(3)
    cyl3()
    #8
    t.left(4)
    cyl3()
    #9
    t.left(5)
    cyl3()
    #10
    t.left(4)
    cyl3()
    #12
    t.left(3)
    cyl3()
    #13
    t.right(19)
    cyl3()
    #left by 19degs
    t.pu()
    
def base():
    '''
    Draws the base.
    '''
    t.color("White")
    t.width(2)
    t.pu()
    t.goto(-100,-300)#leg1
    t.pd()
    t.goto(100,-250)#leg2
    t.goto(0,-200)#leg3
    t.goto(-100,-300)#leg1
    t.goto(-85,-300)#leg1.5
    t.goto(115,-250)#hopper
    t.goto(15,-200)#leg2.5
    t.goto(-85,-300)#leg3.5

def displayStuctureWithTurtle():
    '''
    Displays our structure in an isometric view with turtle graphics.
    '''
    screen = t.Screen()
    screen.bgcolor('Black')
    t.goto(-100,-300)
    t.speed(100)
    leg1()
    leg2()
    leg3()
    base()
    t.done()

def main():
    '''
    Runs the program.
    '''
    expected, actual, percentError = calculateTotalProfitAndAccuracy()
    graphTotalProfitAndAccuracy(expected/1000, actual/1000, percentError)


    expectedPennies = 10
    expectedHeight = 65
    graphHeightWeightComparison(expectedPennies, expectedHeight)
    expectedProfit = 100000
    profitPercentError = 14
    graphProfitPercentErrorComparison(expectedProfit, profitPercentError)


    actualProfit = 96000
    profitPercentError = 14
    actualHeight = 100
    actualPennies = 10
    appendTeamResultsCSV(actualProfit,profitPercentError,actualHeight,actualPennies)
    resultsToTxt(actualProfit,profitPercentError,actualHeight,actualPennies)


    displayStuctureWithTurtle()

if __name__ == "__main__":
    main()
