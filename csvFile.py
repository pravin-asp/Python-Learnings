import csv

def readCSV(fileName):
    table = []
    with open(fileName, "r", newline = '') as inputFile:
        rows = csv.reader(inputFile, skipinitialspace = True)
        for row in rows:
            table.append(row)
    #print(table)
    inputFile.close()
    return table

def writeCSV(content, fileName):
    with open(fileName, "w", newline = '') as outputFile:
        rows = csv.writer(outputFile, skipinitialspace = True)
        for row in content:
            rows.writerow(row)
    outputFile.close()

inputContent = readCSV('c://users//prasarav//desktop//inputFile.csv')
writeCSV(inputContent, 'c://users//prasarav//desktop//outputFile.csv')
