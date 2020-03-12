#this example reads and prints CO2 equiv. measurement, TVOC measurement, and temp every 2 seconds
import csv
from time import sleep
from Adafruit_CCS811 import Adafruit_CCS811

def file_setup():
    with open('CO2.csv', 'w') as csvFile: #opens the csv file
        data = "start, writing"
        writer = csv.writer(csvFile)
        writer.writerow(data) # writes the starting data so you know it started
    csvFile.close() # closes the file
def write(data):
    data=[data] # makes the data an area.
    with open('CO2.csv', 'a') as csvFile: # opens the csv file to append
            writer = csv.writer(csvFile)
            writer.writerow(data) # appends array to the csv.
    csvFile.close()
def main():
    file_setup() # runs the first file setup.
    ccs =  Adafruit_CCS811()
    while not ccs.available():
        pass
    temp = ccs.calculateTemperature() # runs the temperature calculation
    ccs.tempOffset = temp - 25.0
    while(1):
        if ccs.available():
            temp = ccs.calculateTemperature() # runs the temperature calculation again.
            if not ccs.readData():
                data="CO2: ", ccs.geteCO2(), "ppm, TVOC: ", ccs.getTVOC(), " temp: ", temp
                print(data) # prints data so you can see what you are recording to the csv.
                write(data) # sends the data into the right function so it can be logged.
            else:
                print("ERROR!")
                while(1):
                    pass
            sleep(600) # makes it rest for 10 minutes before it hits anther scan.
main()