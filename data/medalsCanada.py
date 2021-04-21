import csv
import matplotlib.pyplot as plt

gold_1924 = 0
gold_1928 = 0
gold_1932 = 0
gold_1936 = 0
gold_1940 = 0
gold_1944 = 0
gold_1948 = 0
gold_1952 = 0
gold_1956 = 0
gold_1960 = 0
gold_1964 = 0
gold_1968 = 0
gold_1972 = 0
gold_1976 = 0
gold_1980 = 0
gold_1984 = 0
gold_1988 = 0
gold_1992 = 0
gold_1994 = 0
gold_1998 = 0
gold_2002 = 0
gold_2006 = 0
gold_2010 = 0
gold_2014 = 0

silver_1924 = 0
silver_1928 = 0
silver_1932 = 0
silver_1936 = 0
silver_1940 = 0
silver_1944 = 0
silver_1948 = 0
silver_1952 = 0
silver_1956 = 0
silver_1960 = 0
silver_1964 = 0
silver_1968 = 0
silver_1972 = 0
silver_1976 = 0
silver_1980 = 0
silver_1984 = 0
silver_1988 = 0
silver_1992 = 0
silver_1994 = 0
silver_1998 = 0
silver_2002 = 0
silver_2006 = 0
silver_2010 = 0
silver_2014 = 0

bronze_1924 = 0
bronze_1928 = 0
bronze_1932 = 0
bronze_1936 = 0
bronze_1940 = 0
bronze_1944 = 0
bronze_1948 = 0
bronze_1952 = 0
bronze_1956 = 0
bronze_1960 = 0
bronze_1964 = 0
bronze_1968 = 0
bronze_1972 = 0
bronze_1976 = 0
bronze_1980 = 0
bronze_1984 = 0
bronze_1988 = 0
bronze_1992 = 0
bronze_1994 = 0
bronze_1998 = 0
bronze_2002 = 0
bronze_2006 = 0
bronze_2010 = 0
bronze_2014 = 0

with open('OlympicsWinter.csv') as csvfile:
  reader = csv.reader(csvfile)

  line = 0

  for row in reader:
    # titles
    if line != 0:
      if (row[0] == "1924") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1924 += 1
      elif (row[0] == "1928") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1928 += 1
      elif (row[0] == "1932") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1932 += 1
      elif (row[0] == "1936") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1936 += 1
      elif (row[0] == "1940") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1940 += 1
      elif (row[0] == "1944") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1944 += 1
      elif (row[0] == "1948") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1948 += 1
      elif (row[0] == "1952") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1952 += 1
      elif (row[0] == "1956") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1956 += 1
      elif (row[0] == "1960") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1960 += 1
      elif (row[0] == "1964") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1964 += 1
      elif (row[0] == "1968") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1968 += 1
      elif (row[0] == "1972") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1972 += 1
      elif (row[0] == "1976") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1976 += 1
      elif (row[0] == "1980") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1980 += 1
      elif (row[0] == "1984") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1984 += 1
      elif (row[0] == "1988") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1988 += 1
      elif (row[0] == "1992") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1992 += 1
      elif (row[0] == "1994") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1994 += 1
      elif (row[0] == "1998") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_1998 += 1
      elif (row[0] == "2002") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_2002 += 1
      elif (row[0] == "2006") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_2006 += 1
      elif (row[0] == "2010") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_2010 += 1
      elif (row[0] == "2014") and (row[7] == "Silver") and (row[4] == "CAN"):
        silver_2014 += 1
      elif (row[0] == "1924") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1924 += 1
      elif (row[0] == "1928") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1928 += 1
      elif (row[0] == "1932") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1932 += 1
      elif (row[0] == "1936") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1936 += 1
      elif (row[0] == "1940") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1940 += 1
      elif (row[0] == "1944") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1944 += 1
      elif (row[0] == "1948") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1948 += 1
      elif (row[0] == "1952") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1952 += 1
      elif (row[0] == "1956") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1956 += 1
      elif (row[0] == "1960") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1960 += 1
      elif (row[0] == "1964") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1964 += 1
      elif (row[0] == "1968") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1968 += 1
      elif (row[0] == "1972") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1972 += 1
      elif (row[0] == "1976") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1976 += 1
      elif (row[0] == "1980") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1980 += 1
      elif (row[0] == "1984") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1984 += 1
      elif (row[0] == "1988") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1988 += 1
      elif (row[0] == "1992") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1992 += 1
      elif (row[0] == "1994") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1994 += 1
      elif (row[0] == "1998") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_1998 += 1
      elif (row[0] == "2002") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_2002 += 1
      elif (row[0] == "2006") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_2006 += 1
      elif (row[0] == "2010") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_2010 += 1
      elif (row[0] == "2014") and (row[7] == "Gold") and (row[4] == "CAN"):
        gold_2014 += 1
      elif (row[0] == "1924") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1924 += 1
      elif (row[0] == "1928") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1928 += 1
      elif (row[0] == "1932") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1932 += 1
      elif (row[0] == "1936") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1936 += 1
      elif (row[0] == "1940") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1940 += 1
      elif (row[0] == "1944") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1944 += 1
      elif (row[0] == "1948") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1948 += 1
      elif (row[0] == "1952") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1952 += 1
      elif (row[0] == "1956") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1956 += 1
      elif (row[0] == "1960") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1960 += 1
      elif (row[0] == "1964") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1964 += 1
      elif (row[0] == "1968") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1968 += 1
      elif (row[0] == "1972") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1972 += 1
      elif (row[0] == "1976") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1976 += 1
      elif (row[0] == "1980") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1980 += 1
      elif (row[0] == "1984") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1984 += 1
      elif (row[0] == "1988") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1988 += 1
      elif (row[0] == "1992") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1992 += 1
      elif (row[0] == "1994") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1994 += 1
      elif (row[0] == "1998") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_1998 += 1
      elif (row[0] == "2002") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_2002 += 1
      elif (row[0] == "2006") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_2006 += 1
      elif (row[0] == "2010") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_2010 += 1
      elif (row[0] == "2014") and (row[7] == "Bronze") and (row[4] == "CAN"):
        bronze_2014 += 1
    line = line + 1


goldmedals = [gold_1924, gold_1928, gold_1932, gold_1936, gold_1940, gold_1944, gold_1948, gold_1952, gold_1956, gold_1960, gold_1964, gold_1968, gold_1972, gold_1976, gold_1980, gold_1984, gold_1988, gold_1992, gold_1994, gold_1998, gold_2002, gold_2006, gold_2010, gold_2014]
silvermedals = [silver_1924, silver_1928, silver_1932, silver_1936, silver_1940, silver_1944, silver_1948, silver_1952, silver_1956, silver_1960, silver_1964, silver_1968, silver_1972, silver_1976, silver_1980, silver_1984, silver_1988, silver_1992, silver_1994, silver_1998, silver_2002, silver_2006, silver_2010, silver_2014]
bronzemedals = [bronze_1924, bronze_1928, bronze_1932, bronze_1936, bronze_1940, bronze_1944, bronze_1948, bronze_1952, bronze_1956, bronze_1960, bronze_1964, bronze_1968, bronze_1972, bronze_1976, bronze_1980, bronze_1984, bronze_1988, bronze_1992, bronze_1994, bronze_1998, bronze_2002, bronze_2006, bronze_2010, bronze_2014]
titles = [1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

plt.plot(titles, goldmedals,  color="#f8a488", linewidth=2.0, label='Gold')
plt.plot(titles, silvermedals, color="#5aa897", linewidth=2.0, label='Silver')
plt.plot(titles, bronzemedals, color="#8fd6e1", linewidth=2.0, label='Bronze')
plt.title("Canada Medals over time")
plt.ylabel("Total Medals of kind")
plt.xlabel("Olympic Winter Year")
plt.show()
