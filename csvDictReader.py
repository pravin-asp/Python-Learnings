import csv

MONTH = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

def parseCSVfile(fileName, key):
    table = {}
    with open(fileName, "rt", newline = '') as csvfile:
        lines = csv.DictReader(csvfile, skipinitialspace = True)
        #print(list(lines))
        for line in lines:
            table[line[key]] = line
    csvfile.close()
    return table

def printFormettedSCVfile(table):
    print("{:15}".format('City'), end = ' ')
    for month in MONTH:
        print("{:5}".format(month), end = ' ')
    print()
    for key, value in table.items():
        print("{:15}".format(key), end = ' ')
        for month in MONTH:
            print("{:5}".format(value[month]), end = ' ')
        print()

table = parseCSVfile('C:/Users/prasarav/Downloads/hightemp.csv', "City")
#print(table)
printFormettedSCVfile(table)
