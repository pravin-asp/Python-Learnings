import csv

def parseCSVfile(fileName, keyField, separator, quote, quoteMapping):
    table = {}
    with open(fileName, "rt", newline = "") as csvfile:
        rows = csv.DictReader(csvfile,
                            skipinitialspace = True,
                            delimiter = separator,
                            quotechar = quote,
                            quoting = quoteMapping)
        #print(list(rows))
        for row in rows:
            #print(row)
            table[row[keyField]] = row
    csvfile.close()
    return table, rows.fieldnames

def printFormettedSCVfile(table, fieldnames):
    print("{:<19}".format(fieldnames[0]), end = "")
    for month in fieldnames[1:]:
        print("{:>6}".format(month), end = "")
    print()
    for keys, values in table.items():
        print("{:<19}".format(keys), end = "")
        for value in fieldnames[1:]:
            print("{:>6}".format(values[value]), end = "")
        print()

table, fieldnames = parseCSVfile('C:/Users/prasarav/Downloads/hightemp.csv', "City", ",", '"', csv.QUOTE_MINIMAL)
#print(table, fieldnames)
printFormettedSCVfile(table, fieldnames)

print()
print()
table, fieldnames = parseCSVfile('C:/Users/prasarav/Downloads/hightemp2.csv', "City", ",", '"', csv.QUOTE_NONNUMERIC)
#print(table, fieldnames)
printFormettedSCVfile(table, fieldnames)

print()
print()
table, fieldnames = parseCSVfile('C:/Users/prasarav/Downloads/hightemp3.csv', "City", " ", "'", csv.QUOTE_NONNUMERIC)
#print(table, fieldnames)
printFormettedSCVfile(table, fieldnames)
