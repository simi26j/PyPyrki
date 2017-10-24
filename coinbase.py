__author__ = 'szji'

from pprint import pprint as pp
import gdax

public_client = gdax.PublicClient()

# Get the order book at the default level.
eth = public_client.get_product_ticker(product_id='ETH-EUR')
ethbtc = public_client.get_product_ticker(product_id='ETH-BTC')
btc = public_client.get_product_ticker(product_id='BTC-EUR')

# pp(public_client.get_products())
# print(c["price"])
# print(c)
# pp(ethbtc)

f = open('ethbtc.csv', mode='at', encoding='utf-8')
dataline = "{0};{1};{2};{3}\n".format(ethbtc["time"], ethbtc["price"], eth["price"], btc["price"])
pp(dataline)
f.write(dataline)
f.close()
