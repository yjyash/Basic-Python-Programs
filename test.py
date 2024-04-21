import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

stock=input("Enter the symbol:")
stock=yf.Ticker(stock)
while True:
    choice=int(input('''Click To Know About:
    1.Company's Information
    2.Company's Elementary Information
    3.Dividends and Splits
    4.Holding Pattern
    5.Company History's Prices
    6.Exit
    '''))

    if choice==1:
      stockinfo=stock.info
      print("------------------------------------------------------------------------------------------------------------------------------------------------")
      print("Company's Information:")
      for key,value in stockinfo.items():
        print(key,":",value)
      print("------------------------------------------------------------------------------------------------------------------------------------------------")

    elif choice==2:
      summarizeshares=stock.info['longBusinessSummary']
      numshares=stock.info['sharesOutstanding']
      print("------------------------------------------------------------------------------------------------------------------------------------------------")
      print("Summary of the company=",summarizeshares)
      print("Total shares outstanding=",numshares)
      print("------------------------------------------------------------------------------------------------------------------------------------------------")

    elif choice==3:
      print("------------------------------------------------------------------------------------------------------------------------------------------------")
      print("Splits:")
      print(stock.splits)
      print("------------------------------------------------------------------------------------------------------------------------------------------------")
      df1=stock.splits
      plt.figure()
      plt.plot(df1)
      plt.show()
      
      print("Dividends:")
      print(stock.dividends)
      print("------------------------------------------------------------------------------------------------------------------------------------------------")
      df=stock.dividends
      plt.figure()
      plt.plot(df)
      plt.show()

    elif choice==4:
      print("------------------------------------------------------------------------------------------------------------------------------------------------")
      print("Major Holders:")
      print(stock.major_holders)
      print("------------------------------------------------------------------------------------------------------------------------------------------------")
      df=stock.major_holders
      plt.figure(figsize=(12,6))
      plt.bar(df[1],df[0],width=0.5)
      plt.show()
      
      print("Institutional Holders:")
      print(stock.institutional_holders)
      print("------------------------------------------------------------------------------------------------------------------------------------------------")
      df=stock.institutional_holders
      plt.figure(figsize=(10,6))
      plt.plot(df['Shares'],df['Holder'])
      plt.show()

    elif choice==5:
        while True:
          c1=int(input('''Click to see last:
          1. 5 years
          2. 1 year
          3. 6 months
          4. 1 month
          5. 1 week
          6. 1 day
          '''))

          if c1==1:
            print(stock.history(period="5y"))
            df=stock.history(period="5y")
            plt.figure(figsize=(12,6))
            plt.plot(df['Close'])
            plt.show()
          
          elif c1==2:
            print(stock.history(period="1y"))
            df=stock.history(period="1y")
            plt.figure(figsize=(12,6))
            plt.plot(df['Close'])
            plt.show()
          
          elif c1==3:
            print(stock.history(period="6mo"))
            df=stock.history(period="6mo")
            plt.figure(figsize=(12,6))
            plt.plot(df['Close'])
            plt.show()
          
          elif c1==4:
            print(stock.history(period="1mo"))
            df=stock.history(period="1mo")
            plt.figure(figsize=(12,6))
            plt.plot(df['Close'])
            plt.show()

          elif c1==5:
            print(stock.history(period="7d"))
            df=stock.history(period="7d")
            plt.figure(figsize=(12,6))
            plt.plot(df['Close'])
            plt.show()
          
          elif c1==6:
            print(stock.history(period="1d"))

          else:
              break

    elif choice==6:
      break   
    else:
      print("Enter Valid Choice")
