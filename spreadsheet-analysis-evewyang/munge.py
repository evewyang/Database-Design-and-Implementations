# place your code to clean up the data file below.
f = open("data/raw_data.csv","r")
raw_data = []
clean_data = []
# title = f[0].strip().split(',')
for line in f:
    # split each line into a list object
    split_line = line.strip().split(',')
    # append to raw_data list
    raw_data.append(split_line)

#skip the title line, we do the cleaning
for split_line in raw_data[1:len(raw_data)]:
    # skip/throw away the line with missing values in it
    if None in split_line:
        continue
    # round all floats (to int) for clarity and simplicity, if is roundable
    new_line = []
    for item in split_line:
        try:
            item.isdigit()
            item = float(item)
            new_line.append(round(item))
        except:
            new_line.append(item)
    # turn the costal indicator from 0,1 to 'no','yes' for easier understanding
    if new_line[-3] == 0:
        new_line[-3] = 'no'
    else:
        new_line[-3] = 'yes'
    clean_data.append(new_line)
# sort clean data (alphabetical order) based on the name of city
clean_data.sort()
# preview the clean_data;
for line in clean_data:
    print(line)
# write to file
with open("data/clean_data.csv", "w") as csvfile:
    # write title
    csvfile.write(",".join([str(x) for x in raw_data[0]]))
    csvfile.write('\n')
    # write content lines
    for line in clean_data:
        str_line=[str(x) for x in line]
        csvfile.write(",".join(str_line))
        csvfile.write('\n')
    csvfile.close()
