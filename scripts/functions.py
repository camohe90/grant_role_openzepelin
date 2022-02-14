
from brownie import Contract, config, accounts

def mint():
    account = accounts.add(config["wallets"]["from_key"])
    token = Contract('0x49e04434fd8668703eeba1409761677e039DaB90')
    address_recieve = "0x9f4CA7F3BbF23f4Df191c7E1A7E96c22F706AD36"
    signer_details = {
        'from' : account
    }
    guess_number_tx = token.mint(address_recieve, 10*10**18, signer_details)
    return guess_number_tx

def burn():
    account = accounts.add(config["wallets"]["from_key"])
    token = Contract('0x49e04434fd8668703eeba1409761677e039DaB90')
    signer_details = {
        'from' : account
    }
    guess_number_tx = token.burn(10**18, signer_details)
    return guess_number_tx