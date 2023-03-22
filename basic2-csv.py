import csv

def writecsv(datalist):
    with open('data2.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['eraser','drink','cigarette']
        

def readcsv():
    with open('data2.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data2 = list(fr)
    return data2    

data2 = readcsv()
print(data2)









data2 = ['ขนมเยลลี่',20,'7.00 น.']
writecsv(data2)


	
        
