import csv 
import numpy as np 

def getDataSource(data_path):
    size_TV = []
    average_timeSpent = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader: 
            size_TV.append(float(row["Size of TV"]))
            average_timeSpent.append(float(row["Average"]))
    return{"x": size_TV, "y": average_timeSpent}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("corelation: ",corelation[0,1])

def setup():
    data_path = "tv.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

setup()