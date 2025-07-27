import yfinance as yf

def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if data.empty:
            print(f"No data found for '{symbol}'. The symbol may be incorrect, delisted, or not supported.")
        else:
            price = data['Close'].iloc[-1]
            print(f"{symbol} current price: ${price:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g., AAPL, MSFT): ").upper()
    get_stock_price(symbol)
