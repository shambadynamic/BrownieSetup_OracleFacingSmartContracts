from brownie import OracleFacingGeoConsumer

def main():
    geoConsumer = OracleFacingGeoConsumer[-1]
    OracleFacingGeoConsumer.publish_source(geoConsumer)