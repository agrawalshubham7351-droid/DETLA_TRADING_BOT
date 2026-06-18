from delta_rest_client import DeltaRestClient

delta_client = DeltaRestClient(
    base_url='https://cdn-ind.testnet.deltaex.org',
    api_key='JVZeR2ohMtPJlgaYej3djrYafpD5Vx',
    api_secret='GbyBHI6BYaf5Osa5AMwSx6Drb583b5uCCafNtQah1ibMgvzXs3cwkCXyXhzG'
)

print(delta_client.get_position(84))