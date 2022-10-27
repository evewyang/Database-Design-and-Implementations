# Place code below to do the munging part of this assignment.
# Group member: Yingying Mao, Hao Huang, Xiao Lu, Wenhan Yang



my_file = open('data/raw_data.txt', 'r')
raw_data = []
for line in my_file:
    if line[0].isdigit():
        new_line=line.strip().split()
        raw_data.append([int(item) if "*" not in item else item for item in new_line])
for line in raw_data:
    print(line)
with open('data/raw_data.txt','r') as my_file:
    lines=my_file.readlines()
    for line in lines:
        if line[0:4]=='Year':
            title=line.strip().split()
            break
raw_data.insert(0,title)
#1) strip all lines without numbers heading(e.g. title, ending, blanks)

for i in range(1, len(raw_data)):
    for j in range(1, 13):
        if type(raw_data[i][j])==str:
            total_sum=0
            for x in range(1, i):
                total_sum+=raw_data[x][j]
            raw_data[i][j] = round(total_sum/(i-1))
#2) from col[Jan] to col[Dec], replace *** with the column average

# let Dec 1879 = Dec 1880 = -16
dec_1879=-16
raw_data[1][14]=raw_data[1][13]
raw_data[1][15] = int((dec_1879+raw_data[1][1]+raw_data[1][2])/3)

for i in range(2, len(raw_data)):
    for j in range(13,len(raw_data[0])):
        if type(raw_data[i][j])==str:
            if j==13:
                total_sum1=0
                for x in range(1,13):
                   total_sum1+=raw_data[i][x]
                raw_data[i][j]=round(total_sum1/12)
            elif j==14:
                total_sum2=0
                for x in range(1, 12):
                    total_sum2+=raw_data[i][x]
                total_sum2+=raw_data[i-1][12]
                raw_data[i][j]=int(total_sum2/12)
            elif j==15:
                total_sum3=0
                for x in range(1, 3):
                    total_sum3+=raw_data[i][x]
                total_sum3+=raw_data[i-1][12]
                raw_data[i][j]=int(total_sum3/3)
            elif j==16:
                total_sum4=0
                for x in range(3, 6):
                    total_sum4+=raw_data[i][x]
                raw_data[i][j]=int(total_sum4/3)
            elif j==17:
                total_sum5=0
                for x in range(6, 9):
                    total_sum5+=raw_data[i][x]
                raw_data[i][j]=int(total_sum5/3)
            elif j==18:
                total_sum6=0
                for x in range(9, 12):
                    total_sum6+=raw_data[i][x]
                raw_data[i][j]=int(total_sum6/3)
for i,n in enumerate(raw_data):
    print(i,n)           
for i in range(1, len(raw_data)):
    for j in range(1, len(raw_data[0])-1):
        raw_data[i][j]=float((format((raw_data[i][j]/100)*1.8,".1f")))
print(raw_data)

with open("data/clean_data.csv", "w") as csvfile:
    for line in raw_data:
        str_line=[str(x) for x in line]
        csvfile.write(",".join(str_line))
        csvfile.write('\n')
    