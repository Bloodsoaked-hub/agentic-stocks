import yfinance as yf
from langchain_core.tools import tool


@tool
def get_stock_data(ticker: str) -> dict:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "symbol": ticker,
            "current_price": info.get("currentPrice"),
            "currency": info.get("currency"),
            "market_cap": info.get("marketCap"),
            "sector": info.get("sector"),
            "short_summary": info.get("LongBusinessSummary", "")[:200] + "...",
        }
    except Exception as e:
        return {"error": f"Failed to fetch data for {ticker}. Details: {str(e)}"}
