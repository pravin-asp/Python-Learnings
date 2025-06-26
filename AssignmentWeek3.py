"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists
"""


import csv



#########################################################
# Part 1 - Week 3



def print_table(table):
    """
    Echo a nested listto the console
    """
    for row in table:
        print(row)


def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
    cancer_risk_table = []
    with open(file_name, "r", newline = '') as readFile:
        contents = csv.reader(readFile, skipinitialspace = True, delimiter = ',', quoting = csv.QUOTE_ALL)
        for lines in contents:
            cancer_risk_table.append(lines)
    readFile.close()
    return cancer_risk_table



def write_csv_file(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """

    with open(file_name, "w", newline = '') as writeFile:
        contents = csv.writer(writeFile, skipinitialspace = True, delimiter = ',', quoting = csv.QUOTE_ALL)
        for lines in csv_table:
            contents.writerow(lines)
    writeFile.close()


def test_part1_code():
    """
    Run examples that test the functions for part 1
    """

    # Simple test for reader
    test_table = read_csv_file("C:/Users/prasarav/Downloads/test_case.csv")  # create a small CSV for this test
    print_table(test_table)
    print()

    # Test the writer
    cancer_risk_table = read_csv_file("C:/Users/prasarav/Downloads/cancer_risk05_v4_county.csv")
    #write_csv_file(cancer_risk_table, "C:/Users/prasarav/Downloads/cancer_risk05_v4_county_copy.csv")
    cancer_risk_copy = read_csv_file("C:/Users/prasarav/Downloads/cancer_risk05_v4_county_copy.csv")

    # Test whether two tables are the same
    for lines, copyLines in zip(cancer_risk_table, cancer_risk_copy):
        if lines != copyLines:
            print("Values that have difference \nOriginal Table : {}\nCopy Table : {}".format(lines, copyLines))

test_part1_code()
