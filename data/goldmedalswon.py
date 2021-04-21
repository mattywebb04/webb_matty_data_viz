import csv
import matplotlib.pyplot as plt

icehockey = 0
skating = 0
skiing = 0
bobsleigh = 0
biathlon = 0
curling = 0


#opens up csv file with csv reader
with open('OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line = 0
	for row in reader:
		if line != 0:
			if (row[7] == "Gold") and (row[4] == "CAN"):
				if (row[2] == 'Ice Hockey'):
					icehockey += 1
				elif (row[2] == 'Skating'):
					skating += 1
				elif (row[2] == 'Skiing'):
					skiing += 1
				elif (row[2] == 'Bobsleigh'):
					bobsleigh += 1
				elif (row[2] == 'Biathlon'):
					biathlon += 1
				elif (row[2] == 'Curling'):
					curling += 1
		line = line + 1



medals = [icehockey, skating, skiing, bobsleigh, biathlon, curling]
label = ['Ice Hockey', 'Skating', 'Skiing', 'Bobsleigh', 'Biathlon', 'Curling']
colors = ["#f8a488", "#5aa897", "#8fd6e1", '#8fd9a8', '#d2e69c', '#ffaaa7']

plt.title("Canadian Total Gold Medals Sports")
plt.pie(medals, labels=label, colors=colors, startangle=0, autopct='%.0f%%')
plt.show()
