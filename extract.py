import math

log = open("transact_class.csv", "r")
db = open("database_class.csv", "w")

def variance(population):
	if len(population) == 0: return 0
	mean = math.fsum(population)/len(population)
	return math.fsum([math.pow(x-mean, 2) for x in population])/len(population)


lines = log.readlines()
lines.pop(0)
dbLines = []
cCount = []
cSumPrice = []
bCount = []
bMinPrice = []
bMaxPrice = []
bSumPrice = []
for (index, line) in enumerate(lines):
	line = line.replace('\n', '')
	line = line.split('|')
	cCount.append(int(line[4]) if line[4] != '?' else '?')
	cSumPrice.append(float(line[7]) if line[7] != '?' else '?')
	bCount.append(int(line[8]) if line[8] != '?' else '?')
	bMinPrice.append(float(line[9]) if line[9] != '?' else '?')
	bMaxPrice.append(float(line[10]) if line[10] != '?' else '?')
	bSumPrice.append(float(line[11]) if line[11] != '?' else '?')
	if line[0] != lines[index+1].split('|')[0]:
		cMean = [
					(
						cs/cCount[i] 
						if cs != '?' and cCount[i] != '?' 
						else '?'
					) 
					for (i,cs) in enumerate(cSumPrice)
				]
		bMean = [
					(
						bs/bCount[i] 
						if bs != '?' and bCount[i] != '?' 
						else '?'
					) 
					for (i,bs) in enumerate(bSumPrice)
				]
		rCount = 0
		for (i, x) in enumerate(bCount):
			if bCount[i-1]:
				if x < bCount[i-1]: rCount += 1
		total = len(bMinPrice)
		bMinPrice = list(filter(lambda a: a != '?', bMinPrice))
		bMaxPrice = list(filter(lambda a: a != '?', bMinPrice))
		cMean = list(filter(lambda a: a != '?', bMinPrice))
		bMean = list(filter(lambda a: a != '?', bMinPrice))
		line.append(rCount)
		line.append(variance(bMinPrice))
		line.append(variance(bMaxPrice))
		line.append(variance(bMean))
		line.append(variance(cMean))
		db.write('|'.join([str(item) for item in line])+'\n')
		cCount = []
		cSumPrice = []
		bCount = []
		bMinPrice = []
		bMaxPrice = []
		bSumPrice = []
		
