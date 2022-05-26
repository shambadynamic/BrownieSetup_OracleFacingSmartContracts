from brownie import OracleFacingGeoConsumer, config, accounts

def printGeoData(geoConsumer):

    if geoConsumer.getGeostatsData() != 0:
        print(geoConsumer.getGeostatsData())
    else:
        print("Data isn't available yet. Please check the job run in the oracle node.")
        
def printCids(geoConsumer):

    i = 0
    while True:
    
        if geoConsumer.getCid(i):
            print(geoConsumer.getCid(i))
        else:
            break
        i += 1

def main():
    deployer_account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    print(deployer_account.address)
    geoConsumer = OracleFacingGeoConsumer[-1]
    printGeoData(geoConsumer)
    printCids(geoConsumer)