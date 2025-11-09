from binance.client import Client
from dotenv import load_dotenv
import os
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        if testnet:
            self.client = Client(api_key,api_secret, testnet=True)
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com' 
        else:
            self.client = Client(api_key, api_secret)

        self.logger=logging.getLogger("TradingBot")
        self.logger.info("Connected to Binanace Testnet")

    def place_order(self, symbol, side, quantity, order_type="MARKET", price= None):
        try:
            if order_type.upper() == "MARKET":
                order=self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="MARKET",
                    quantity=quantity
                )

            elif order_type.upper() == "LIMIT":
                order=self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            else:
                raise ValueError("Unsupported order type")

            self.logger.info(f"order placed successfully: {order}")
            return order

        except Exception as e:
            self.logger.error(f"Failed to place order: {e}")
            return None
