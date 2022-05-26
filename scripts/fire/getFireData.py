from brownie import OracleFacingFireConsumer, config, accounts

def printFireData(fireConsumer, propertyId):

    if fireConsumer.getFireData(propertyId) != 0:
        print(fireConsumer.getFireData(propertyId))
    else:
        print("Property Id " + str(propertyId) + " does not exist.")
        
def printCids(fireConsumer):

    i = 0
    while True:
    
        if fireConsumer.getCid(i):
            print(fireConsumer.getCid(i))
        else:
            break
        i += 1

def main():
    deployer_account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    print(deployer_account.address)
    fireConsumer = OracleFacingFireConsumer[-1]
    printFireData(fireConsumer, 2)
    printCids(fireConsumer)