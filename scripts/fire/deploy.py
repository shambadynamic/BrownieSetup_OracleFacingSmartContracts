from brownie import accounts, OracleFacingFireConsumer
def main():
    deployer_account = accounts.load('deployer_account')
    print(deployer_account.address)
    greeter = OracleFacingFireConsumer.deploy({'from': deployer_account})
    print("Deployed at: ", greeter.address)
