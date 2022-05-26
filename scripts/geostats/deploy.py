from brownie import OracleFacingGeoConsumer, config, accounts
def main():
    deployer_account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    print(deployer_account.address)
    contract = OracleFacingGeoConsumer.deploy({'from': deployer_account})
    print("Deployed at: ", contract.address)
