import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

canada_gold = 0
usa_gold = 0
norway_gold = 0



with open('OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line = 0
	for row in reader:
		if line != 0:
			if (row[7] == "Gold") and (row[4] == "USA"):
				usa_gold += 1
			elif (row[7] == "Gold") and (row[4] == "CAN"):
				canada_gold += 1
			elif (row[7] == "Gold") and (row[4] == "NOR"):
				norway_gold += 1
		line = line + 1



labels = ['Canada', 'USA', 'Norway']
x = np.arange(len(labels))
medals = [canada_gold, usa_gold, norway_gold]

plt.bar(x, medals, align='center', alpha=0.8)
plt.xticks(x, labels)
plt.ylabel('Total Medals')
plt.title('Top 3 Countries Gold medals')

plt.show()
