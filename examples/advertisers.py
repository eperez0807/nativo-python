import nativo

nativo.api_key = '<api_key>'
nativo.api_secret = '<api_secret>'

response = nativo.Advertiser.list()
print(response)
