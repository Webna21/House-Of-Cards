#  By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Andrew Li
#               Cameron King
#               Gavin Munoz
#               Thomas Janes
# Section:      559
# Assignment:   House of Cards, Final Project
# Date:         11/30/2024

import matplotlib.pyplot as plt
import numpy as np

## Estimated Profit ##
estimatedProfit = 105 # 140k

## Input the values of our final design ##
cards = int(input("Cards used: "))
time = int(input("Time used: "))
height = int(input("height reached: "))
pennies = int(input("pennies held: "))
sicciors = input("Sccisors used: ")
tape = input("Tape used: ")

## Debugging ## 
percentError = 0 # test with a specific percent error




with open("HouseofCardsResults.csv", "r") as OG_FILE:
#### Extract data from csv ####

    #headers of data
    header = OG_FILE.readline().strip()             
    header_2 = OG_FILE.readline().strip()
    
    #clean data
    data = [line.strip().split(',') for line in OG_FILE]
    
    Team_num = [row[0] for row in data]
    Profits = [float(row[1]) if row[1] else 0 for row in data]
    Profit_accuracy = [row[2] if row[2] else "0" for row in data]
    Height = [float(row[3]) if row[3] else 0 for row in data]
    Pennies = [float(row[4]) if row[4] else 0 for row in data]
    
    data_dict = {} # CSV file data is stored here
    
    for i in range(len(Team_num)):
        
        data_dict[Team_num[i]] = (Profits[i], Profit_accuracy[i], Height[i], Pennies[i])

#### Profit calulations ####

    def profit(cds:int,tme:int,hgt:int,pny:int,tp:bool,scis:bool):
        """Using the data points:
           cards, time, height, number of pennies, if you bought tape, if you boug scissors

           You can calulate the Profit of a build
        """
        prof = 0
        if hgt >= 36: # 36 inch profit
            prof += 100
        prof -= cds # take out cost of cards
        if hgt > 36: # extra inches bonus
            prof += (hgt-36)*2
            #print(hgt-36)
        prof+= pny*0.05 # penny profit
        if tme < 25: # time bonus
            prof += 25-tme
        elif tme > 25: # time penalty
            prof -= tme-25
        if tp == "y": # tape cost
            prof -= 10
            #print(" - tape used")
        if scis == "y": # scissor cost
            prof -= 5
            #print(" - sccisors used")
        return prof


    # this is to be entered by reponding to imputs
    actual = profit(cards,time,height,pennies,tape,sicciors) # profit(55,20,90,20,"y","y")
    ## premarked Estiamted result in thousand increments ie: 150 -> 150,000
    estimated = estimatedProfit 
    ## calulates precent error
    if percentError == False:
        pcntErr = round(abs(1-actual/estimated),2)*100
    else:
        pcntErr = percentError
        print("*Percent error Override*")

    #print(f"\nyou made {actual}k!")
    #print(f"{pcntErr}% off you estimated amount {estimated}K")

## graph the profit vs. Percent error chart ##

    pltx = np.arange(2)
    plt1y = np.array((estimated,actual))
    plt2y = np.array((0,round(pcntErr)))

    axs1 = plt.subplot()
    
    l1 = axs1.bar(pltx,plt1y,color = "b", label = "Dollars")
    #axs1.bar_label(container= 2 ,labels=("Dollars","percent"))
    axs1.set_ylabel(f"Profit ({r"$10^{3}$"})")
    axs1.set_xticks(())
    axs1.set_ylim(estimated-30,estimated+20)
    axs1.set_xlabel(f"Estimated profit: {estimated}k   |   Accuracy: {100-pcntErr}%   |   Actual profit: {actual}k")
    axs1.set_title("Profit vs Percent Error")

    axs2 = axs1.twinx()
    l2 = axs2.bar(pltx,plt2y,color = "r", label = "Percent")
    axs2.set_ylabel("Pecent error (%)")
    axs2.set_ylim(0,100)
    axs1.legend([l1,l2],[l1.get_label(),l2.get_label()])

    plt.show()
    
## Height Vs. Weight Graph (team comparison)## 


    # data_dict
    
    plt.show
## Profit Vs. Percent error (Team comparison) ##

    
    plt.show()
