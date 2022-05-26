from brownie import MyLinkToken, OracleFacingFireConsumer, config, accounts

def sendRequest(fireConsumer, deployer_account):
    
    link = MyLinkToken.at("0xa36085F69e2889c224210F603D836748e7dC0088")
    link.transfer(fireConsumer, 1e18, {'from': deployer_account})

    fireConsumer.requestFireData("MODIS/006/MOD14A1", "MaxFRP", "1000", "2021-09-01", "2021-09-10", [[1, "[[[29.53125,19.642587534013032],[29.53125,27.059125784374068],[39.90234375,27.059125784374068],[39.90234375,19.642587534013032],[29.53125,19.642587534013032]]]"], [2, "[[[46.72947724367683,4.390228926463396],[46.679357886244986,3.8826857905457652],[46.530925872748305,3.394358826483646],[46.28988536222383,2.9440946050840657],[45.965499406313945,2.5492840567467825],[45.57023397538652,2.2251800570298523],[45.11927889828469,1.9843023404026605],[44.62996412572296,1.8359528461951848],[44.12109374999999,1.7858585217968768],[43.61222337427702,1.8359528461951848],[43.122908601715295,1.9843023404026605],[42.67195352461347,2.2251800570298523],[42.27668809368605,2.5492840567467825],[41.95230213777616,2.9440946050840657],[41.71126162725168,3.394358826483646],[41.562829613755,3.8826857905457652],[41.51271025632316,4.390228926463396],[41.562829613755,4.8974271245416965],[41.71126162725168,5.3847719120817565],[41.95230213777616,5.833566543422026],[42.27668809368605,6.22664411740961],[42.67195352461348,6.549015711120945],[43.12290860171531,6.788425209793004],[43.612223374277036,6.9357938995827375],[44.12109375,6.9855438544859965],[44.629964125722964,6.9357938995827375],[45.119278898284705,6.788425209792991],[45.57023397538653,6.549015711120945],[45.965499406313945,6.226644117409597],[46.28988536222384,5.833566543422026],[46.53092587274831,5.384771912081744],[46.679357886244986,4.897427124541672],[46.72947724367683,4.390228926463396]]]"]], {'from': deployer_account})
    

def main():
    deployer_account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    print(deployer_account.address)
    fireConsumer = OracleFacingFireConsumer[-1]
    sendRequest(fireConsumer, deployer_account)