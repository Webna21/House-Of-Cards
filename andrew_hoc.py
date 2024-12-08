#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Andrew Li
#               Cameron King
#               Gavin Munoz
#               Thomas Janes
# Section:      ENGR-559
# Assignment:   House of Cards - Final Project
# Date:         8 December 2024

import matplotlib.pyplot as plt
import numpy as np


def costs():
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
    cost = costs()
    rev = revenue()
    print(f"\nTotal Profit = Total Revenue - Total Costs = {rev} - {cost} = {rev-cost}")
    return rev-cost

def calculateTotalProfitAndAccuracy():
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
    pltx = np.arange(2)
    plt1y = np.array((estimated,actual))
    plt2y = np.array((0,percentError))

    axs1 = plt.subplot()
    
    l1 = axs1.bar(pltx,plt1y,color = "b", label = "Profit")
    axs1.set_ylabel(f"Profit (Thousand Dollars)")
    axs1.set_xticks(())
    # axs1.set_ylim(estimated-30,estimated+20)
    axs1.set_ylim(0, max(150, estimated, actual))
    axs1.set_xlabel(f"Expected profit: {estimated}k   |   Percent Error: {percentError:.3f}%   |   Actual profit: {actual}k")
    axs1.set_title("Profit and Percent Error")

    axs2 = axs1.twinx()
    l2 = axs2.bar(pltx,plt2y,color = "r", label = "Percent Error")
    axs2.set_ylabel("Pecent error (%)")
    axs2.set_ylim(0,100)
    axs1.legend((l1,l2), (l1.get_label(),l2.get_label()))

    plt.show()

def extractFileData():
    with open("HouseofCardsResults.csv") as file:
        for _ in range(2):
            file.readline()

        data = [row.strip().split(',') for row in file]
        
        teamNumbers = [int(row[0]) for row in data]
        profits = [int(row[1]) for row in data]
        profitAccuracies = [int(row[2][:-1]) for row in data]
        heights = [float(row[3]) for row in data]
        pennies = [int(row[4]) for row in data]
        
        # data_dict = {}
        # for i in range(len(data)):
        #     data_dict[teamNumbers[i]] = (profits[i], profitAccuracies[i], heights[i], pennies[i])

        return (heights, pennies), (profits, profitAccuracies)

def graphHeightWeightComparison(fileData):
    data, _ = extractFileData()
    heights = data[0]
    pennies = data[1]
    print(heights)
    print()
    print(pennies)

def graphProfitPercentErrorComparison(fileData):
    pass

def fileModification():
    pass

def main():
    #expected, actual, percentError = calculateTotalProfitAndAccuracy()
            # expected = 105000
            # actual = 120000
            # percentError = abs((actual-expected)/expected) * 100
    #graphTotalProfitAndAccuracy(expected/1000, actual/1000, percentError)


    fileData = extractFileData()
    graphHeightWeightComparison(fileData)
    graphProfitPercentErrorComparison(fileData)

if __name__ == "__main__":
    main()