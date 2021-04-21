import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

canada_gold_hockey = 0
usa_gold_hockey = 0
norway_gold_hockey = 0



with open('OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line = 0
	for row in reader:
		if line != 0:
			if (row[7] == "Gold") and (row[4] == "CAN") and (row[2] == "Ice Hockey"):
				canada_gold_hockey += 1
			elif (row[7] == "Gold") and (row[4] == "USA") and (row[2] == "Ice Hockey"):
				usa_gold_hockey += 1
			elif (row[7] == "Gold") and (row[4] == "NOR") and (row[2] == "Ice Hockey"):
				norway_gold_hockey += 1
		line = line + 1



labels = ['Canada', 'USA', 'Norway']
x = np.arange(len(labels))
medals = [canada_gold_hockey, usa_gold_hockey, norway_gold_hockey]

plt.bar(x, medals, align='center', alpha=0.8)
plt.xticks(x, labels)
plt.ylabel('Total Gold Medals in Hockey')
plt.title('Top 3 Countries Total Gold Medals in Hockey')

plt.show()
