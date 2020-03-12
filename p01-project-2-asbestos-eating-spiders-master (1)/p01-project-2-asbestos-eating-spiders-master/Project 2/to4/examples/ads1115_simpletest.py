import csv
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)
# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)
print("{:>5}\t{:>5}".format('raw', 'v'))
def first_print():
    data = ("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))    
    print(data) # prints the data for the user.
    data = [data] # sets the data into an array
    with open('CO_scan_2.csv', 'w') as csvFile: # opens a csv file. If one does not exist it makes one.
        writer = csv.writer(csvFile)
        writer.writerow(data) # writes the rray data to the csv.
    csvFile.close()
def main():
    first_print() # runs to make a csv fie if one dowes not exist. If one does it accomplishes one run of the while True.
    while True:
        data = ("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))    
        print(data) # print data for user.
        data = [data] # sets data to array.
        with open('CO_scan_2.csv', 'a') as csvFile: # opens the csv file to append
            writer = csv.writer(csvFile)
            writer.writerow(data) # appends array to the csv.
        csvFile.close()
        time.sleep(2) # waits a half second until it scan again.
main()