from brownie import accounts, OracleFacingGeoConsumer
def main():
    deployer_account = accounts.load('deployer_account')
    print(deployer_account.address)
    greeter = OracleFacingGeoConsumer.deploy({'from': deployer_account})
    print("Deployed at: ", greeter.address)
