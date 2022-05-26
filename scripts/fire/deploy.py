from brownie import OracleFacingFireConsumer, config, accounts
def main():
    deployer_account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    print(deployer_account.address)
    contract = OracleFacingFireConsumer.deploy({'from': deployer_account})
    print("Deployed at: ", contract.address)
