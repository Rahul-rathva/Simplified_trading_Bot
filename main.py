import os
import argparse
from dotenv import load_dotenv
from bot import BasicBot
from logger_config import setup_logger

def main():
    logger= setup_logger()

    load_dotenv()
    api_key = os.getenv("API_KEY")
    secret_key = os.getenv("API_SECRET")

    if not api_key or not secret_key:
        logger.error("API_KEY or API_SECRET is missing. Please check your .env file.")
        return

    parser = argparse.ArgumentParser(description="Simplified Binance Trading Bot")
    parser.add_argument("--symbol", type=str, required=True, help="trading pair e.g. BTCUSDT")
    parser.add_argument("--side", type=str, choices=["BUY","SELL"],required=True, help="order side")
    parser.add_argument("--quantity", type=float, required=True, help="order quantity")
    parser.add_argument("--type",type=str,default="MARKET",choices=["MARKET","LIMIT"],help="order type")
    parser.add_argument("--price",type=float,help="Price (for LIMIT orders only)")
    args = parser.parse_args()

    bot = BasicBot(api_key, secret_key)

    order = bot.place_order(
        symbol=args.symbol,
        side=args.side,
        quantity=args.quantity,
        order_type=args.type,
        price=args.price
    )

    if order:
        logger.info("Order placed Successfully!")
    else:
        logger.error("Order Execution Failed!")

if __name__ == "__main__":
    main()