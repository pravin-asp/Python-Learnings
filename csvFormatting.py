def parseCSVfile(fileName):
    table = []
    with open(fileName, "r") as csvfile:
        for line in csvfile:
            formet = line.rstrip()
            table.append(formet.split(","))
    return table

def printFormettedSCVfile(table):
    for row in table:
        print("{:17}".format(row[0]), end = " ")
        for col in row[1:]:
            print("{:5}".format(col), end = " ")
        print()

table = parseCSVfile('C:/Users/prasarav/Downloads/hightemp.csv')
printFormettedSCVfile(table)
print()
print()
table = parseCSVfile('C:/Users/prasarav/Downloads/hightemp2.csv')
printFormettedSCVfile(table)
