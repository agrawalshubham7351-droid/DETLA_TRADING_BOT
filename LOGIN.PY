api_key = 'JVZeR2ohMtPJlgaYej3djrYafpD5Vx'
secret_key ='GbyBHI6BYaf5Osa5AMwSx6Drb583b5uCCafNtQah1ibMgvzXs3cwkCXyXhzG'


from delta_rest_client import DeltaRestClient,OrderType

delta_client = DeltaRestClient(
  base_url='https://cdn-ind.testnet.deltaex.org',
  api_key='JVZeR2ohMtPJlgaYej3djrYafpD5Vx',
  api_secret='GbyBHI6BYaf5Osa5AMwSx6Drb583b5uCCafNtQah1ibMgvzXs3cwkCXyXhzG'
)
response = delta_client.get_assets()
print(response)


order_response = delta_client.place_order(
        product_id= 84,
        size=1,
        side='buy',
				limit_price='7800',
        order_type=OrderType.MARKET
)


# response = delta_client.get_ticker('BTCUSD')
# print(response)