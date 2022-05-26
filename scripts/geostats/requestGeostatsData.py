from brownie import MyLinkToken, OracleFacingGeoConsumer, config, accounts

def sendRequest(geoConsumer, deployer_account):

    link = MyLinkToken.at("0xa36085F69e2889c224210F603D836748e7dC0088")
    link.transfer(geoConsumer, 1e18, {'from': deployer_account})

    geoConsumer.requestGeostatsData("agg_min", "COPERNICUS/S2_SR", "NDVI", "250", "2021-09-01", "2021-09-10", [[1, "[[[19.51171875,4.214943141390651],[18.28125,-4.740675384778361],[26.894531249999996,-4.565473550710278],[27.24609375,1.2303741774326145],[19.51171875,4.214943141390651]]]"]], {'from': deployer_account})
    

def main():
    deployer_account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    print(deployer_account.address)
    geoConsumer = OracleFacingGeoConsumer[-1]
    sendRequest(geoConsumer, deployer_account)