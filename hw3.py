import time

import math

import csv

import tempfile

def fizzbuzz():
	start = time.time()

	for number in range(1,101):
		out = ""

		if number % 3 == 0:
			out += "fizz"
		if number % 5 == 0:
			out += "buzz"

		if out == "":
			print(number)
		else:
			print(out)

	end = time.time()
	return end - start

def sphereVolume(radius):
	radius = radius*radius*radius
	radius = radius * math.pi
	radius = radius * 4 / 3

	print(radius)

#Used Tim Pietzcker's StackOverflow answer using zip https://stackoverflow.com/questions/23613426/write-dictionary-of-lists-to-a-csv-file
def dictToCsv(dic, filename):
	with open(filename, 'w') as file:
		writer = csv.writer(file)
		writer.writerow(dic.keys())
		writer.writerows(zip(*dic.values()))

def csvToDict(filename):
	dic = {}
	with open(filename, 'r') as file:
		read = csv.DictReader(file)

		for field in read.fieldnames:
			dic[field] = list()

		for row in read:
			for key in row:
				dic[key].append(row[key])
	return dic

def DictToCsvToDict(dic):
	temp = tempfile.NamedTemporaryFile()

	with open(temp.name, 'w') as file:
		writer = csv.writer(file)
		writer.writerow(dic.keys())
		writer.writerows(zip(*dic.values()))

	dic = {}
	with open(temp.name, 'r') as file:
		read = csv.DictReader(file)

		for field in read.fieldnames:
			dic[field] = list()

		for row in read:
			for key in row:
				dic[key].append(row[key])
	return dic

#Drivers
print(fizzbuzz())

sphereVolume(5)

newDict = {'Title': ['Animal Farm', '1984', 'Brave New World'], 'Author': ['George ORwell', 'GEEEORGE ORWELLLIO', 'ADLBUT BUTUBUT'], 'pages': [1,2,3]}
dictToCsv(newDict, 'out.csv')

print(csvToDict('out.csv'))

print(DictToCsvToDict(newDict))
