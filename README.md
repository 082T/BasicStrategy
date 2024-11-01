# Opis

Implementacija SMA i EMA cross strategije. Za scrapeanje koristi se yfinance. Za optimizaciju koristi se hyperopt. Prvih 250 dana povijesti podataka je preskočeno kako bi se dobili short i long window te kako bi optimizacija počela od istog trenutka za svaku testiranu kombinaciju parametara.

# Korištene biblioteke

hyperopt==0.2.7  
matplotlib==3.9.2  
numpy==2.1.2  
pandas==2.2.3  
yfinance==0.2.41  

# Upute za pokretanje

  --ticker TICKER       
  Ticker symbol  
  --start_date START_DATE  
  Backtesting start date  
  --end_date END_DATE   
  Backtesting end date  
  --short_window SHORT_WINDOW  
  SMA short window length  
  --long_window LONG_WINDOW  
  SMA long window length  
  --optimize            
  Optimize SMA parameters  
  --strategy STRATEGY   
  Strategy to test  (strategyEMA / strategySMA)

  # Primjeri pokretanja

  ### Naredba:
  python .\main.py --strategy strategySMA --optimize  
  ### Output:  
  Final Cumulative Return: 290.04%  
  Max Drawdown: -18.38%  
  Sharpe Ratio: 0.74  
  Strategy: strategySMA, with windows: 7/189    

  ### Naredba:  
  python .\main.py --strategy strategyEMA --short_window 12 --long_window 30 --ticker SPY --start_date 01-01-2018 --end_date 01-01-2023  
  ### Output:  
  Final Cumulative Return: 139.42%  
  Max Drawdown: -12.37%  
  Sharpe Ratio: 0.63  
  Strategy: strategyEMA, with windows: 12/30  

  Drawdown i Equity vs Benchmark grafovi se spreme u plots/analysis.png

![image](https://github.com/user-attachments/assets/dc162692-bc3f-4885-8db8-b30821dbbe83)

## QuantConnect implementacija nalazi se u fileu quant_connect_implementation.py

![image](https://github.com/user-attachments/assets/b2c33083-3a3d-4bd8-b180-c460de4329d0)

![image](https://github.com/user-attachments/assets/de3f950f-63a7-454c-a118-1c64e93f9a41)



