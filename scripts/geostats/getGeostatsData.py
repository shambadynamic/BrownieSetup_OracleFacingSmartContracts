from brownie import accounts, OracleFacingGeoConsumer

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
    deployer_account = accounts.load('deployer_account')
    print(deployer_account.address)
    geoConsumer = OracleFacingGeoConsumer.at("0x7F61c4d2bCCEfd3F33d8864616aA6363F4E44C57")

    printGeoData(geoConsumer)
    printCids(geoConsumer)