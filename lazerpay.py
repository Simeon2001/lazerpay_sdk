# from config import secret_key
import requests
from requests.structures import CaseInsensitiveDict
import json

# secret = secret_key
class Lazerpay:
    def __init__(self, public_key:str,secret_key:str) -> dict:
        """put your public_key,secret_key here example: Lazerpay("pk_test_.......................","sk_test............................")"""
        headers = CaseInsensitiveDict()
        self.headers = headers

        headers["Content-Type"] = "application/json"
        headers["x-api-key"] = "{0}".format(public_key)
        headers["Authorization"] = "Bearer {0}".format(secret_key)

    def initialize(
        self,
        customer_name:str,
        customer_email:str,
        coin:str,
        currency:str,
        amount:str,
        reference:str,
        accept_partial_payment:bool,
    ) -> dict:
        """to generate bsc address for your customer to pay you, you need to put the following details. example:initialize("sim","sim@sim.com","BUSD","USD","100","RE54646",False)"""
        url = "https://api.lazerpay.engineering/api/v1/transaction/initialize"
        info = {
            "customer_name": customer_name,
            "customer_email": customer_email,
            "amount": amount,
            "currency": currency,
            "coin": coin,
            "reference": reference,
            "accept_partial_payment": accept_partial_payment,
        }

        data = json.dumps(info, indent=2)

        res = requests.post(url, headers=self.headers, data=data)
        respond = res.json()
        return respond

    def verify(self, address:str) -> dict:
        """to verify if the transacation is successful you can do this with bsc address. example: verify("0X........")"""
        url = "https://api.lazerpay.engineering/api/v1/transaction/verify/{0}".format(
            address
        )
        res = requests.get(url, headers=self.headers)
        respond = res.json()
        return respond

    def accepted_coin(self) -> dict:
        """to get the coin accepted. example: accepted_coin()"""
        url = "https://api.lazerpay.engineering/api/v1/coins"
        res = requests.get(url, headers=self.headers)
        respond = res.json()
        return respond

    def transfer(self, amount:int, address:str, coin:str, blockchain:str) -> dict:
        """to transfer your stable coin to another address you can do. example: transfer(1000,"0X....","BUSD","BSC blockchain")"""
        url = "https://api.lazerpay.engineering/api/v1/transfer"
        info = {
            "amount": amount,
            "recipient": address,
            "coin": coin,
            "blockchain": blockchain,
        }

        data = json.dumps(info, indent=2)

        res = requests.post(url, headers=self.headers, data=data)
        respond = res.json()
        return respond

    def coin_rate(self, currency:str, coin:str) -> dict:
        """to get rate of coin to fiat. example: coin_rate("USD","DAI")"""
        url = (
            "https://api.lazerpay.engineering/api/v1/rate?coin={0}&currency={1}".format(
                coin, currency
            )
        )
        res = requests.get(url, headers=self.headers)
        respond = res.json()
        return respond

    def get_paylinks(self) -> dict:
        
        url = "https://api.lazerpay.engineering/api/v1/payment-links"
        res = requests.get(url, headers=self.headers)
        respond = res.json()
        return respond

    
