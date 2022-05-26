from brownie import OracleFacingFireConsumer

def main():
    fireConsumer = OracleFacingFireConsumer[-1]
    OracleFacingFireConsumer.publish_source(fireConsumer)