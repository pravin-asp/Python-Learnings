import csv

def readCSVReaderList(filename):
    csv_list = []
    with open(filename, "r") as opened_file:
        for lines in opened_file:
            csv_list.append(lines)
    return csv_list


def readCSVReader(filename, keyfield, separator, quotes, quotesMapping):
    csv_dict = []
    field_names = []
    with open(filename, "r", newline = '') as opened_file:
        csv_reader = csv.DictReader(opened_file,
                                    skipinitialspace = True,
                                    delimiter = separator,
                                    quotechar = quotes,
                                    quoting = quotesMapping)
        field_names = csv_reader.fieldnames
        csv_dict = list(csv_reader)
        #for dict_value in csv_reader:
        #    csv_dict[dict_value[keyfield]] = dict_value
    return csv_dict, field_names

def writeCSRWriter(csv_dict, filename, fieldnames, separator, quotes, quotesMapping):
    with open(filename, "w", newline = '') as opened_file:
        csv_writer = csv.DictWriter(opened_file,
                                    skipinitialspace = True,
                                    delimiter = separator,
                                    quotechar = quotes,
                                    quoting = quotesMapping,
                                    fieldnames = fieldnames)
        csv_writer.writeheader()
        for keys in csv_dict.keys():
            csv_writer.writerow(csv_dict[keys])


csv_dict, fieldnames = readCSVReader("C:/Users/prasarav/Downloads/hightemp2.csv", "City", ",", '"', csv.QUOTE_MINIMAL)
print(csv_dict)
#print()
#print(fieldnames)
#print()
# print()
# print(readCSVReaderList("C:/Users/prasarav/Downloads/hightemp2.csv"))
#writeCSRWriter(csv_dict, "C:/Users/prasarav/Downloads/pravin.csv", fieldnames, ",", '"', csv.QUOTE_MINIMAL)
