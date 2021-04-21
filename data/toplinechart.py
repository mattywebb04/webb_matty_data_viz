import csv
import matplotlib.pyplot as plt

can_1924 = 0
can_1928 = 0
can_1932 = 0
can_1936 = 0
can_1940 = 0
can_1944 = 0
can_1948 = 0
can_1952 = 0
can_1956 = 0
can_1960 = 0
can_1964 = 0
can_1968 = 0
can_1972 = 0
can_1976 = 0
can_1980 = 0
can_1984 = 0
can_1988 = 0
can_1992 = 0
can_1994 = 0
can_1998 = 0
can_2002 = 0
can_2006 = 0
can_2010 = 0
can_2014 = 0

usa_1924 = 0
usa_1928 = 0
usa_1932 = 0
usa_1936 = 0
usa_1940 = 0
usa_1944 = 0
usa_1948 = 0
usa_1952 = 0
usa_1956 = 0
usa_1960 = 0
usa_1964 = 0
usa_1968 = 0
usa_1972 = 0
usa_1976 = 0
usa_1980 = 0
usa_1984 = 0
usa_1988 = 0
usa_1992 = 0
usa_1994 = 0
usa_1998 = 0
usa_2002 = 0
usa_2006 = 0
usa_2010 = 0
usa_2014 = 0

nor_1924 = 0
nor_1928 = 0
nor_1932 = 0
nor_1936 = 0
nor_1940 = 0
nor_1944 = 0
nor_1948 = 0
nor_1952 = 0
nor_1956 = 0
nor_1960 = 0
nor_1964 = 0
nor_1968 = 0
nor_1972 = 0
nor_1976 = 0
nor_1980 = 0
nor_1984 = 0
nor_1988 = 0
nor_1992 = 0
nor_1994 = 0
nor_1998 = 0
nor_2002 = 0
nor_2006 = 0
nor_2010 = 0
nor_2014 = 0

with open('OlympicsWinter.csv') as csvfile:
  reader = csv.reader(csvfile)

  line = 0

  for row in reader:
    # titles
    if line != 0:
      if (row[0] == "1924") and (row[4] == "USA"):
        usa_1924 += 1
      elif (row[0] == "1928") and (row[4] == "USA"):
        usa_1928 += 1
      elif (row[0] == "1932") and (row[4] == "USA"):
        usa_1932 += 1
      elif (row[0] == "1936") and (row[4] == "USA"):
        usa_1936 += 1
      elif (row[0] == "1940") and (row[4] == "USA"):
        usa_1940 += 1
      elif (row[0] == "1944") and (row[4] == "USA"):
        usa_1944 += 1
      elif (row[0] == "1948") and (row[4] == "USA"):
        usa_1948 += 1
      elif (row[0] == "1952") and (row[4] == "USA"):
        usa_1952 += 1
      elif (row[0] == "1956") and (row[4] == "USA"):
        usa_1956 += 1
      elif (row[0] == "1960") and (row[4] == "USA"):
        usa_1960 += 1
      elif (row[0] == "1964") and (row[4] == "USA"):
        usa_1964 += 1
      elif (row[0] == "1968") and (row[4] == "USA"):
        usa_1968 += 1
      elif (row[0] == "1972") and (row[4] == "USA"):
        usa_1972 += 1
      elif (row[0] == "1976") and (row[4] == "USA"):
        usa_1976 += 1
      elif (row[0] == "1980") and (row[4] == "USA"):
        usa_1980 += 1
      elif (row[0] == "1984") and (row[4] == "USA"):
        usa_1984 += 1
      elif (row[0] == "1988") and (row[4] == "USA"):
        usa_1988 += 1
      elif (row[0] == "1992") and (row[4] == "USA"):
        usa_1992 += 1
      elif (row[0] == "1994") and (row[4] == "USA"):
        usa_1994 += 1
      elif (row[0] == "1998") and (row[4] == "USA"):
        usa_1998 += 1
      elif (row[0] == "2002") and (row[4] == "USA"):
        usa_2002 += 1
      elif (row[0] == "2006") and (row[4] == "USA"):
        usa_2006 += 1
      elif (row[0] == "2010") and (row[4] == "USA"):
        usa_2010 += 1
      elif (row[0] == "2014") and (row[4] == "USA"):
        usa_2014 += 1
      elif (row[0] == "1924") and (row[4] == "CAN"):
        can_1924 += 1
      elif (row[0] == "1928") and (row[4] == "CAN"):
        can_1928 += 1
      elif (row[0] == "1932") and (row[4] == "CAN"):
        can_1932 += 1
      elif (row[0] == "1936") and (row[4] == "CAN"):
        can_1936 += 1
      elif (row[0] == "1940") and (row[4] == "CAN"):
        can_1940 += 1
      elif (row[0] == "1944") and (row[4] == "CAN"):
        can_1944 += 1
      elif (row[0] == "1948") and (row[4] == "CAN"):
        can_1948 += 1
      elif (row[0] == "1952") and (row[4] == "CAN"):
        can_1952 += 1
      elif (row[0] == "1956") and (row[4] == "CAN"):
        can_1956 += 1
      elif (row[0] == "1960") and (row[4] == "CAN"):
        can_1960 += 1
      elif (row[0] == "1964") and (row[4] == "CAN"):
        can_1964 += 1
      elif (row[0] == "1968") and (row[4] == "CAN"):
        can_1968 += 1
      elif (row[0] == "1972") and (row[4] == "CAN"):
        can_1972 += 1
      elif (row[0] == "1976") and (row[4] == "CAN"):
        can_1976 += 1
      elif (row[0] == "1980") and (row[4] == "CAN"):
        can_1980 += 1
      elif (row[0] == "1984") and (row[4] == "CAN"):
        can_1984 += 1
      elif (row[0] == "1988") and (row[4] == "CAN"):
        can_1988 += 1
      elif (row[0] == "1992") and (row[4] == "CAN"):
        can_1992 += 1
      elif (row[0] == "1994") and (row[4] == "CAN"):
        can_1994 += 1
      elif (row[0] == "1998") and (row[4] == "CAN"):
        can_1998 += 1
      elif (row[0] == "2002") and (row[4] == "CAN"):
        can_2002 += 1
      elif (row[0] == "2006") and (row[4] == "CAN"):
        can_2006 += 1
      elif (row[0] == "2010") and (row[4] == "CAN"):
        can_2010 += 1
      elif (row[0] == "2014") and (row[4] == "CAN"):
        can_2014 += 1
      elif (row[0] == "1924") and (row[4] == "NOR"):
        nor_1924 += 1
      elif (row[0] == "1928") and (row[4] == "NOR"):
        nor_1928 += 1
      elif (row[0] == "1932") and (row[4] == "NOR"):
        nor_1932 += 1
      elif (row[0] == "1936") and (row[4] == "NOR"):
        nor_1936 += 1
      elif (row[0] == "1940") and (row[4] == "NOR"):
        nor_1940 += 1
      elif (row[0] == "1944") and (row[4] == "NOR"):
        nor_1944 += 1
      elif (row[0] == "1948") and (row[4] == "NOR"):
        nor_1948 += 1
      elif (row[0] == "1952") and (row[4] == "NOR"):
        nor_1952 += 1
      elif (row[0] == "1956") and (row[4] == "NOR"):
        nor_1956 += 1
      elif (row[0] == "1960") and (row[4] == "NOR"):
        nor_1960 += 1
      elif (row[0] == "1964") and (row[4] == "NOR"):
        nor_1964 += 1
      elif (row[0] == "1968") and (row[4] == "NOR"):
        nor_1968 += 1
      elif (row[0] == "1972") and (row[4] == "NOR"):
        nor_1972 += 1
      elif (row[0] == "1976") and (row[4] == "NOR"):
        nor_1976 += 1
      elif (row[0] == "1980") and (row[4] == "NOR"):
        nor_1980 += 1
      elif (row[0] == "1984") and (row[4] == "NOR"):
        nor_1984 += 1
      elif (row[0] == "1988") and (row[4] == "NOR"):
        nor_1988 += 1
      elif (row[0] == "1992") and (row[4] == "NOR"):
        nor_1992 += 1
      elif (row[0] == "1994") and (row[4] == "NOR"):
        nor_1994 += 1
      elif (row[0] == "1998") and (row[4] == "NOR"):
        nor_1998 += 1
      elif (row[0] == "2002") and (row[4] == "NOR"):
        nor_2002 += 1
      elif (row[0] == "2006") and (row[4] == "NOR"):
        nor_2006 += 1
      elif (row[0] == "2010") and (row[4] == "NOR"):
        nor_2010 += 1
      elif (row[0] == "2014") and (row[4] == "NOR"):
        nor_2014 += 1
    line = line + 1


canmedals = [can_1924, can_1928, can_1932, can_1936, can_1940, can_1944, can_1948, can_1952, can_1956, can_1960, can_1964, can_1968, can_1972, can_1976, can_1980, can_1984, can_1988, can_1992, can_1994, can_1998, can_2002, can_2006, can_2010, can_2014]
usamedals = [usa_1924, usa_1928, usa_1932, usa_1936, usa_1940, usa_1944, usa_1948, usa_1952, usa_1956, usa_1960, usa_1964, usa_1968, usa_1972, usa_1976, usa_1980, usa_1984, usa_1988, usa_1992, usa_1994, usa_1998, usa_2002, usa_2006, usa_2010, usa_2014]
normedals = [nor_1924, nor_1928, nor_1932, nor_1936, nor_1940, nor_1944, nor_1948, nor_1952, nor_1956, nor_1960, nor_1964, nor_1968, nor_1972, nor_1976, nor_1980, nor_1984, nor_1988, nor_1992, nor_1994, nor_1998, nor_2002, nor_2006, nor_2010, nor_2014]
titles = [1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

plt.plot(titles, canmedals,  color="#f8a488", linewidth=2.0, label='Canada')
plt.plot(titles, usamedals, color="#5aa897", linewidth=2.0, label='United States')
plt.plot(titles, normedals, color="#8fd6e1", linewidth=2.0, label='Norway')
plt.title("Top three countries medals")
plt.ylabel("Total Medals")
plt.xlabel("Olympic Winter Year")
plt.show()
