from flask import Flask
from opengateway_sandbox_sdk import Simswap

phone_number = "+3466655555"
client_id = "eb8932ec-7864-4b16-b6af-5e0fcda6fe0e"
client_secret = "2420a577-b799-420f-9e06-1a68be3d727d"

# Usa Simswap (heredada), no SimSwap
simswap_client = Simswap(client_id, client_secret, phone_number)

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)