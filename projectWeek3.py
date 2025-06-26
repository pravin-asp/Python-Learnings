"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    field_names = []
    with open(filename, encoding='utf-8') as open_file:
        read_file = csv.DictReader(open_file,
                                    delimiter = separator,
                                    quotechar = quote,
                                    quoting = csv.QUOTE_MINIMAL)
        field_names = read_file.fieldnames
    return field_names


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    list_dict = []
    with open(filename, encoding='utf-8') as open_file:
        read_file = csv.DictReader(open_file,
                                    delimiter = separator,
                                    quotechar = quote,
                                    quoting = csv.QUOTE_MINIMAL)
        list_dict = list(read_file)
    return list_dict


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    dict_dict = {}
    with open(filename, encoding='utf-8') as open_file:
        read_file = csv.DictReader(open_file,
                                    delimiter = separator,
                                    quotechar = quote,
                                    quoting = csv.QUOTE_MINIMAL)
        for lines in read_file:
            dict_dict[lines[keyfield]] = lines
    return dict_dict


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, "w", encoding='utf-8') as open_file:
        write_file = csv.DictWriter(open_file,
                                    fieldnames = fieldnames,
                                    delimiter = separator,
                                    quotechar = quote,
                                    quoting = csv.QUOTE_MINIMAL)
        write_file.writeheader()
        for lines in table:
            write_file.writerow(lines)
