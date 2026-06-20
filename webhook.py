import os
from flask import Flask, request
from delta_rest_client import DeltaRestClient, OrderType
from flask import Flask, request
from dotenv import load_dotenv


load_dotenv()

delta_client = DeltaRestClient(
    base_url='https://cdn-ind.testnet.deltaex.org',
    api_key=os.getenv("DELTA_API_KEY"),
    api_secret=os.getenv("DELTA_API_SECRET")
)


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    print("\n====================")
    print("ALERT RECEIVED")
    print(data)
    print("====================\n")

    signal = data["signal"]

    print("SIGNAL =", signal)

    # POSITION CHECK
    position = delta_client.get_position(84)
    size = position["size"]

    if position["size"] == 0:
        order_size = 5
    else:
        order_size = 10

    print("CURRENT POSITION =", position)
    print("ORDER SIZE =", order_size)

    # Already Long
    if signal == "BUY" and size > 0:
     print("Already Long, Skipping")
     return "OK", 200
    


# Already Short
    if signal == "SELL" and size < 0:
      print("Already Short, Skipping")
      return "OK", 200


# BUY ORDER
    if signal == "BUY":
       

        order_response = delta_client.place_order(
            product_id=84,
            size=order_size,
            side='buy',
            order_type=OrderType.MARKET
        )
        print("BUY ORDER SENT")
        print("ORDER ID =", order_response["id"])
        print("PRICE =", order_response["average_fill_price"])

    elif signal == "SELL":
        order_response = delta_client.place_order(
            product_id=84,
            size=order_size,
            side='sell',
            order_type=OrderType.MARKET
        )

        print("SELL ORDER SENT")
        print("ORDER ID =", order_response["id"])
        print("PRICE =", order_response["average_fill_price"])

    return "OK", 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5001))
    )






# ngrok http 5001% 
# python check.py
# python webhook.py
