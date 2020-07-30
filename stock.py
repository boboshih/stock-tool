import yfinance as yf
import csv

def inputData():
    x = input("Enter your stock: ")
    return x

def tickerData(x):
    tsla = yf.Ticker(x)
    hist = tsla.history(period="max")
    cal = tsla.calendar
    with open('stock.csv', 'w') as csvfile:
        csvfile.write(str(hist))
        csvfile.write(str(cal))

tickerData(inputData())
