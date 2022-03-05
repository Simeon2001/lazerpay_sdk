# Lazerpay sdk

## tutorial 

* first import the pacakage by:

-----------------
   from lazerpay import Lazerpay

----------------------------------------

* then you can call the class(Lazerpay) and add your secret key:

-------------------------------
    secret = "pk_test_.................."

    payment = Lazerpay(secret)

------------------------------------------------

* to initialize a transcation that generate crypto addresss and other info for payment in json format:
-----------------
    name = "sim"
    email = "jesusanyasimeon@gmail.com"
    coin = "DAI"
    currency = "USD"
    amount = "100"
    reference = "abdc" # it can be any random digit or alphabet
    partial_payment = False
    payment_address = payment.initialize(name,email,coin,currency,amount,reference,partial_payment)
    print(payment_address)
-------------------------------------------------

* to verify if your transaction is successful or not just add the address generated by lazerpay when you initialize:

----------------------------------
    addr = '0xEa250dc41851EE6Ee076e5941131754580e91e7a'
    check = payment.verify(addr)
    print(check)
------------------------------------------------

* to know coin rate to your fiat currency, put your fiat currency name in short form and coin name:

--------------------
    fiat = "NGN" # USD
    coin = "USDC"
    rate = payment.coin_rate(fiat,coin)
    print(rate)
--------------------------------