from bot import BasicBot

def test_order_type_validation():
    
    # Creating an instance of BasicBot with fake API credentials

    bot = BasicBot("fake_key", "fake_secret")

    try:
        # Attempting to place an order with an invalid order type

        bot.place_order("BTCUSDT", "BUY", 0.01, order_type="INVALID")
    except ValueError:
        
        # If a ValueError is raised, the test passes

        assert True
    else:

        # If no exception is raised, the test fails

        assert False, "Expected ValueError for invalid order type"
