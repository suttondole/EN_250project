import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functools import reduce





#GENERATING FIGURE(1) STARTS ---

thisData = pd.read_csv("importedFromR.csv")
shortenedThisData = thisData.head(30)
shortenedThisDataFiltered = shortenedThisData.loc[(shortenedThisData["EXT.DIV"] > 2)]
listOfSpeciesRichness = shortenedThisDataFiltered["EXT.DIV"].to_list()
listOfSimpsonIndex = shortenedThisDataFiltered["INT.DIV"].to_list()
listOfIDNums = list(range(1, len(listOfSpeciesRichness) + 1))
dictPreDataFrame = {"ID": listOfIDNums, "Species Richness" : listOfSpeciesRichness, "Simpson Index": listOfSimpsonIndex}
myDataFrame = pd.DataFrame(dictPreDataFrame)


'''UNCOMMENT TO OUTPUT FIGURE(1)
plt.bar(myDataFrame["ID"], myDataFrame["Species Richness"])
plt.locator_params(axis='y', integer=True, tight=True)
plt.title('Species Richness by Sample Set')
plt.xlabel('Sample Set')
plt.ylabel('Species Richness')
plt.show()
'''

#---GENERATING FIGURE(1) ENDS






#GENERATING FIGURE(2) STARTS ---



listOfTotalNumOfSpecies = []
for x in listOfSpeciesRichness:
    listOfTotalNumOfSpecies.append(x * (x-1))
scaled50_listOfSimpsonIndex = []
for x in listOfSimpsonIndex:
    scaled50_listOfSimpsonIndex.append(x * 50)

'''UNCOMMENT TO OUTPUT FIGURE(2)
X_axis = np.arange(12)
plt.bar(X_axis - .1, listOfTotalNumOfSpecies[0:12], .2, label = 'Sum of species counts')
plt.bar(X_axis + .1, listOfSpeciesRichness[0:12], .2, label = 'Species richness')
plt.bar(X_axis + .3, scaled50_listOfSimpsonIndex[0:12], .2, label = 'Simpson Index')
plt.xticks(X_axis, listOfIDNums[0:12])
plt.xlabel("Sample sets")
plt.title("Comparison of Sum of Species Counts and Species Richness")
plt.legend()
plt.show()
'''




#---GENERATING FIGURE(2) ENDS









#GENERATING FIGURE(3) STARTS ---





shannon = pd.read_csv("shannonData.csv")
totalCount = reduce(lambda c1, c2: c1 + c2, shannon["Count"].to_list())
listOfShannons = []
for x in shannon["Count"].to_list():
    currentPi = float(x / totalCount)
    currentLNofPi = np.log(currentPi)
    listOfShannons.append(round(currentPi * currentLNofPi, 2))
totalShannon = -1 * reduce(lambda sh1, sh2: sh1 + sh2, listOfShannons)
totalShannonList = [totalShannon] + (["N/A"] * 6)
shannon["Shannon Wiener index"] = totalShannonList
shannon.to_csv("shannonDataOut.csv")







#---GENERATING FIGURE(3) ENDS









#---FIGURE(4) WAS CREATED IN EXCEL SO WE WILL READ IT INTO ABGData






#GENERATING FIGURE(5) STARTS ---





ABGData = pd.read_csv("ABGcomparissions.csv")

habitatXalphaDict = {}
allSpeciesList = []
for (habitat, value) in ABGData.iteritems():
    if habitat == "Species":
        pass
    else:
        thisSpeciesList = value.to_list()
        allSpeciesList.append(thisSpeciesList)
        habitatXalphaDict[habitat] = len(list(filter(lambda val: val == "Y", thisSpeciesList)))

habitatXtoYBetaList = []

for x in range(len(allSpeciesList)):
    currentBeta = 0
    for y in range(len(allSpeciesList[x])):
        if x == len(allSpeciesList) - 1:
            if allSpeciesList[x][y] != allSpeciesList[0][y]:
                currentBeta += 1
        elif allSpeciesList[x][y] != allSpeciesList[x+1][y]:
            currentBeta += 1
    habitatXtoYBetaList.append(currentBeta)

dictABGDataOut = {"Habitat" : list(habitatXalphaDict.keys()), "Alpha" : list(habitatXalphaDict.values()), "Beta": habitatXtoYBetaList, "Gamma": len(allSpeciesList[0])}
dataFrameABGDataOut = pd.DataFrame(dictABGDataOut)
dataFrameABGDataOut.to_csv('scaleDiversity.csv')




#---GENERATING FIGURE(5) ENDS
