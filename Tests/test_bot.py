from bot import BasicBot

def test_order_type_validation():
    bot = Basicbot("fake_key","Fake_secret")
    try:
        bot.place_order("BTCUSDT","BUY",0.01,order_type="INVALID")
    except ValueError:
        assert True
        