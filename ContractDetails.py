
#Check Contract Details

import json
import requests
import pandas as pd
from web3 import Web3

TokenAddress = '0xCBd8aECe0c920eEF3F215ad4e7319052Bd8eaa74'
BurnWallet = '0x000000000000000000000000000000000000dead'
AirdropWallet = '0xc148b9e8da1fd3d87b5f870c61b8cbfc5f57e7fa'
LPWallet = '0x3c3af41a28beacd86c2e46c5a54c71fb43ef0d12'
RWallet = '0xd8f262fd1c4d0e48a8b11fceb2bdd7d2c23b763b'
TWallet = '0xcbd8aece0c920eef3f215ad4e7319052bd8eaa74'

#- Get ABI from BSCscan
bsc = 'https://bsc-dataseed.binance.org/'
web3 = Web3(Web3.HTTPProvider(bsc))

url_eth = 'https://api.bscscan.com/api'
contract_address = web3.toChecksumAddress(TokenAddress)
print("contract_address",contract_address)
API_ENDPOINT = url_eth+'?module=contract&action=getabi&address='+str(contract_address)

r = requests.get(url = API_ENDPOINT)
response = r.json()
#response_df = pd.DataFrame([response])
#response_df.to_csv("response.csv")
#print (response)
#response_df.head()
abi=json.loads(response['result'])

#- Call contract
contract = web3.eth.contract(address=contract_address, abi=abi)
totalSupply = contract.functions.totalSupply().call()
print("Total Supply:","{:,}".format(totalSupply))
print("Contract Name:",contract.functions.name().call())
print("Contract Symbol:",contract.functions.symbol().call())
#Burnwallet Count
BurnWalletaddress = web3.toChecksumAddress(BurnWallet)
burnbalance=contract.functions.balanceOf(BurnWalletaddress).call()
print('Burn Wallet in ether:',web3.fromWei(burnbalance, 'ether'))
print('BurnWallet Balance:',"{:,}".format(burnbalance))
#Airdrop wallet balance
AirdropWalletaddress = web3.toChecksumAddress(AirdropWallet)
AirdropWalletbalance=contract.functions.balanceOf(AirdropWalletaddress).call()
print('Airdrop wallet Balance:',"{:,}".format(AirdropWalletbalance))
#LP wallet balance
LPWalletaddress = web3.toChecksumAddress(LPWallet)
LPWalletbalance=contract.functions.balanceOf(LPWalletaddress).call()
print('LP wallet Balance:',"{:,}".format(LPWalletbalance))
#Rewards wallet balance
RWalletaddress = web3.toChecksumAddress(RWallet)
RWalletbalance=contract.functions.balanceOf(RWalletaddress).call()
print('Rewards wallet Balance:',"{:,}".format(RWalletbalance))
#Token wallet balance
TWalletaddress = web3.toChecksumAddress(TWallet)
TWalletbalance=contract.functions.balanceOf(TWalletaddress).call()
print('Token wallet Balance:',"{:,}".format(TWalletbalance))

CirculatingSupply = totalSupply - burnbalance - AirdropWalletbalance #- LPWalletbalance - RWalletbalance - TWalletbalance
print('Circulating Supply:',"{:,}".format(CirculatingSupply))

rewardToken = contract.functions.rewardToken().call()

#Contract Info
print("***********Contract Info*****")
print ("rewardToken",rewardToken)
print ("autoBuybackAccumulator",contract.functions.autoBuybackAccumulator().call())
print ("liquidityFee",contract.functions.liquidityFee().call())
print ("buybackFee",contract.functions.buybackFee().call())
print ("reflectionFee",contract.functions.reflectionFee().call())
print ("marketingFee",contract.functions.marketingFee().call())
print ("feeDenominator",contract.functions.feeDenominator().call())

#result = web3.eth.get_transaction('0xc5e6539ae242209fee009069d7563ce92727c5ba5f096e758434cc0a03b336fa')
result = web3.eth.get_transaction_count('0xB7ccCC09863Cc97801955B2f1760eeCB5D4c34fD')
print("Transaction_count for wallet",result)
#walletlist = web3.eth.accounts(contract_address)
#print(walletlist)

