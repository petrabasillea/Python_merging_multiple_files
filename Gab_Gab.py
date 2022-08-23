import os
import csv
import datetime

dt = datetime.datetime.now()
dtstr = dt.strftime("%Y-%m-%w_%H.%M.%S")

directory_name  = '.\Raw'
filewrite       = "output_"+dtstr+".csv"
x = 1


for file_name in os.listdir(directory_name):
    i = os.path.join(directory_name, file_name)
    if os.path.isfile(i):
        print("File ke-",x," : ", file_name)

        fileread = i        

        with open(fileread) as file_obj:
            
            if x>1:
                heading = next(file_obj)
                reader_obj = csv.reader(file_obj)
            else:
                #heading = next(file_obj)
                reader_obj = csv.reader(file_obj)

            for row in reader_obj:
                data = [row] 
        
                with open(filewrite, 'a+', newline ='') as file:   
                        csvwriter = csv.writer(file)
                        csvwriter.writerows(data)
        
        x = x+1
        