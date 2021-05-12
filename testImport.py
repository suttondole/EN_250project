import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

thisData = pd.read_csv("importedFromR.csv")
shortenedThisData = thisData.head(30)
shortenedThisDataFiltered = shortenedThisData.loc[(shortenedThisData["EXT.DIV"] > 2)]
listOfSpeciesRichness = shortenedThisDataFiltered["EXT.DIV"].to_list()
listOfSimpsonIndex = shortenedThisDataFiltered["INT.DIV"].to_list()
listOfIDNums = list(range(1, len(listOfSpeciesRichness) + 1))
#for x in range(1, len(listOfSpeciesRichness) + 1):
#    dictOfData[x] = [listOfSpeciesRichness[x-1], round(listOfSimpsonIndex[x-1], 3)]
dictPreDataFrame = {"ID": listOfIDNums, "Species Richness" : listOfSpeciesRichness, "Simpson Index": listOfSimpsonIndex}
myDataFrame = pd.DataFrame(dictPreDataFrame)


'''UNCOMMENT TO OUTPUT SPECIES RICHNESS BAR GRAPH
plt.bar(myDataFrame["ID"], myDataFrame["Species Richness"])
plt.locator_params(axis='y', integer=True, tight=True)
plt.title('Species Richness by Sample Set')
plt.xlabel('Sample Set')
plt.ylabel('Species Richness')
plt.show()
'''

listOfTotalNumOfSpecies = []
for x in listOfSpeciesRichness:
    listOfTotalNumOfSpecies.append(x * (x-1))
scaled50_listOfSimpsonIndex = []
for x in listOfSimpsonIndex:
    scaled50_listOfSimpsonIndex.append(x * 50)
    
X_axis = np.arange(12)
plt.bar(X_axis - .1, listOfTotalNumOfSpecies[0:12], .2, label = 'Sum of species counts')
plt.bar(X_axis + .1, listOfSpeciesRichness[0:12], .2, label = 'Species richness')
plt.bar(X_axis + .3, scaled50_listOfSimpsonIndex[0:12], .2, label = 'Simpson Index')
plt.xticks(X_axis, listOfIDNums[0:12])
plt.xlabel("Sample sets")
plt.title("Comparison of Sum of Species Counts and Species Richness")
plt.legend()
plt.show()
