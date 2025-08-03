import yfinance as yf  # importing the yfinance library to get stock data

# function to get the latest stock price
def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)  # create a ticker object using the stock symbol

        # get historical data for the last 1 day
        data = stock.history(period="1d")

        # if data is empty, the symbol might be invalid or not supported
        if data.empty:
            print(f"No data found for '{symbol}'. The symbol may be incorrect, delisted, or not supported.")
        else:
            # get the latest closing price (last row of the 'Close' column)
            price = data['Close'].iloc[-1]
            print(f"{symbol} current price: ${price:.2f}")
    except Exception as e:
        # catch any errors (e.g. internet issues, wrong format)
        print(f"An error occurred: {e}")

# main block to take user input and run the function
if __name__ == "__main__":
    # ask the user to enter the stock symbol (like AAPL or TSLA)
    symbol = input("Enter stock symbol (e.g., AAPL, MSFT): ").upper()
    get_stock_price(symbol)  # call the function with the input symbol
