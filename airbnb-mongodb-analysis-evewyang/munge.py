## import the csv module
import csv

def get_csv_data(filepath):
    f = open(filepath, 'r') # open the file in read mode
    reader =csv.DictReader(f) #reads the data using the csv module's DictReader
    raw_data = [row for row in reader]
    return raw_data

def remove_mostly_empty_columns(data,column_name):
    filtered_data = []
    for row in data:
        row.pop(column_name)
        filtered_data.append(row)
    return filtered_data

def remove_rows_with_blank_fields(data):
    filtered_data = [row for row in data if ("N/A" not in row.values()) and ('' not in row.values())]
    return filtered_data

def save_csv_data(data, filepath):
    keys = data[0].keys()
    with open(filepath, 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    output_file.close()

def main():
    ## use the functions defined above to complete munging of the data file

    # get the data from the file
    data = get_csv_data('data/listings.csv')
    print(len(data))
    data = remove_mostly_empty_columns(data,'host_neighbourhood')
    data = remove_mostly_empty_columns(data,'license')
    data = remove_mostly_empty_columns(data,'calendar_updated')
    data = remove_mostly_empty_columns(data,'bathrooms')
    # munge it
    data = remove_rows_with_blank_fields(data)
    print(len(data))
    # save to the new csv file
    save_csv_data(data, 'data/listings_clean.csv')
if __name__ == "__main__":
    main()