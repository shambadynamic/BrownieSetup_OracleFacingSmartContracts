from brownie import accounts, OracleFacingFireConsumer

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
    deployer_account = accounts.load('deployer_account')
    print(deployer_account.address)
    fireConsumer = OracleFacingFireConsumer.at("0x627051FDC98e9436Ea0cB1F32C5DBE5Dd9b75D27")

    printFireData(fireConsumer, 2)
    printCids(fireConsumer)