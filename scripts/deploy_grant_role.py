
from brownie import  accounts, ContratoConRoles, config

# Basic_storage es el nombre del contrato inteligente y no del archivo .sol

def main():
    account = accounts.add(config["wallets"]["from_key"])
    deploy_details = {
        'from' : account
    }
    basic_storage_tx = ContratoConRoles.deploy(deploy_details)
    return basic_storage_tx

