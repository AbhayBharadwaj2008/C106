import csv 
import numpy as np 

def getDataSource(data_path):
    Marks_per = []
    days_present = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader: 
            Marks_per.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return{"x": Marks_per, "y": days_present}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("corelation: ",corelation[0,1])

def setup():
    data_path = "./Marks.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

setup()