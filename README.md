# 🚀 Simplified Trading Bot

**Build a safe and beginner-friendly crypto trading bot in Python!**  
Test fake buys/sells on Binance Futures Testnet with simple commands, detailed logs, and robust error handling.  
Perfect for learning, experimenting, or kickstarting your journey into automated trading! ✨

---

## 🌟 Key Features
- **Market & Limit Orders**: Seamlessly place both market and limit orders on Binance Futures Testnet.
- **Buy & Sell Support**: Execute trades on both sides with ease.
- **Command-Line Control**: Flexible and intuitive CLI for real-time trading.
- **Real-Time Logging**: Track every action with detailed logs for debugging and monitoring.
- **Secure API Management**: Keep your API keys safe using `.env` files.
- **Modular Design**: Clean, reusable, and testable code structure.
- **Error Handling**: Robust error tracking to ensure smooth operation.

---

## 🛠️ Tech Stack
- **Python 3.10+**: The core programming language.
- **[python-binance](https://github.com/sammchardy/python-binance)**: For seamless Binance API integration.
- **[requests](https://docs.python-requests.org/)**: For RESTful API calls.
- **[colorama](https://pypi.org/project/colorama/)**: Add colors to your terminal for better readability.
- **[logging](https://docs.python.org/3/library/logging.html)**: For structured event tracking.
- **[pytest](https://docs.pytest.org/)**: For unit testing and ensuring code reliability.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: For secure environment variable management.

---

## 📖 How It Works
1. **Connect to Binance Testnet**: Use the Binance Futures Testnet API to simulate trades without real money.
2. **Place Orders**: Execute market or limit orders with simple CLI commands.
3. **Track Logs**: Monitor every action in real-time with detailed logs.
4. **Test Safely**: Experiment with fake trades to learn and refine your strategies.

---

## 🧰 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Binance Testnet account ([Sign up here](https://testnet.binancefuture.com/))

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Rahul-rathva/Simplified_trading_Bot.git
   cd Simplified_trading_bot
```

### Configuration
- Create a `.env` file in the project directory with your Binance API keys:
  ```bash
  API_KEY=your_api_key
  API_SECRET=your_api_secret
  ```

### Usage
- Run the bot:
  ```bash
  python main.py
  ```

- Place a market order:
  ```bash
  python main.py market BTCUSDT buy 0.001
  ```

- Place a limit order:
  ```bash
  python main.py limit BTCUSDT sell 0.001 10000
  ```

- View logs:
  ```bash
  python main.py --logs
  ```

---

## 🧪 Testing
- Run tests with:
  ```bash
  pytest
  ```

---

## 📚 Documentation
- Read the [README.md](README.md) for more details.

---

## 🚨 Important Notes
- This bot is for educational and experimental purposes only.
- Do not use it with real money without proper risk management.
- Always test and validate your strategies on the testnet before deploying to live markets.

---

## 🌟 Future Enhancements
- Add support for more trading pairs.
- Implement advanced order types (e.g., stop-loss, take-profit).
- Add real-time market data visualization.

---

## 🧩 Example Code
- See the `bot.py` file for a complete example.

---

## 📝 License
- This project is licensed under the MIT License.

---

## 🚀 Get Started
- Run the bot and start trading!



