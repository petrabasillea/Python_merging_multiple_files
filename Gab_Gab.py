import os
import csv

directory_name = '.\Raw'
filewrite = "outoput.csv"


for file_name in os.listdir(directory_name):
    i = os.path.join(directory_name, file_name)
    if os.path.isfile(i):
        print(i)
        fileread = i

        with open(fileread) as file_obj:

            heading = next(file_obj)
            reader_obj = csv.reader(file_obj)

            for row in reader_obj:
                #print(row)
                data = [row] 
        
                with open(filewrite, 'a+', newline ='') as file:   
                        csvwriter = csv.writer(file)
                        csvwriter.writerows(data)