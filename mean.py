import csv

with open('Graph.csv', newline='') as f:
    reader=csv.reader(f)
    #reads row, returns current row,moves on to next

    file_data=list(reader)
#removng list of titles using pop
file_data.pop(0)
#used to remove first list using pop
#create empty list
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

n=len(new_data)
total=0

for x in new_data:
    total=total+x

mean=total/n

print("Mean/Average"+str(mean))
    

    