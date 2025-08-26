import yfinance as yf
import pandas as pd
import os

# SP500, NASDAQ, QQQ

wd = os.getcwd()
print(wd)

def get_historical_stock_data(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        df = ticker.history(period="50y")

        if df.empty:
            print(f"❌ No data found for ticker symbol '{ticker_symbol}'. Check the symbol and try again.")
            return

        # Keep only the Close column
        df = df[['Close']]

        # Resample to year-end closing prices
        yearly_data = df.resample('Y').last()

        # Reset index to turn DateTime index into a column
        yearly_data.reset_index(inplace=True)

        # Save to CSV
        filename = f"{ticker_symbol}_history.csv"
        yearly_data.to_csv(filename, index=False)

        print(f"✅ Saved historical year-end data to '{filename}'")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    ticker_input = input("Enter a stock ticker symbol (e.g., AAPL, TSLA): ").upper()
    get_historical_stock_data(ticker_input)
