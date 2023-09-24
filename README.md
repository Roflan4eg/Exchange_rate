# Exchange_rate
Exchange rate app on Fast API with docker.
Docker: docker pull roflan4eg/exchange_rate:latest (80 port)
Documentation:
# Add your api key in conf.py

# Functional
The conversion takes plase on request: api/rates?from={from}&to={to}&value={value}

# currency_converter
def currency_converter takes 3 values (from, to, amount) and returns the finished result.
The conversion takes place through a third-party service. You can use a ready-made key or get your own at https://apilayer.com/marketplace/exchangerates_data-api.

# check_valid
def check_valid takes two values (from, to) and checks the correctness of the currencies by searching for correspondences in symblos.json. Returns a boolean value.
