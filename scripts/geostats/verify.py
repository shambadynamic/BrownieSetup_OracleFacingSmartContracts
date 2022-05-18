from brownie import accounts, OracleFacingGeoConsumer

def main():
    deployer_account = accounts.load('deployer_account')
    print(deployer_account.address)
    fireConsumer = OracleFacingGeoConsumer.at("0x7F61c4d2bCCEfd3F33d8864616aA6363F4E44C57")
    OracleFacingGeoConsumer.publish_source(fireConsumer)