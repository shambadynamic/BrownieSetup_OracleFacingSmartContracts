from brownie import accounts, OracleFacingFireConsumer

def main():
    deployer_account = accounts.load('deployer_account')
    print(deployer_account.address)
    fireConsumer = OracleFacingFireConsumer.at("0x627051FDC98e9436Ea0cB1F32C5DBE5Dd9b75D27")
    OracleFacingFireConsumer.publish_source(fireConsumer)