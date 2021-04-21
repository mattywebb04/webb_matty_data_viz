import csv
import matplotlib.pyplot as plt

gold = 0
silver = 0
bronze = 0

with open('OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)

	line = 0

	for row in reader:
    # titles
		if line != 0:
			if (row[7] == "Gold") and (row[4] == "CAN"):
				gold += 1
			elif (row[7] == "Silver") and (row[4] == "CAN"):
				silver += 1
			elif (row[7] == "Bronze") and (row[4] == "CAN"):
				bronze += 1
		line = line + 1



medals = [gold, silver, bronze]
label = ["Gold", "Silver", "Bronze"]
colors = ["#f8a488", "#5aa897", "#8fd6e1"]

plt.title("Canadian Total Medals")
plt.pie(medals, labels=label, colors=colors, startangle=0, autopct='%.2f%%')
plt.show()
