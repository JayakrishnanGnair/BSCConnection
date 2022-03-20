#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:48:15 2022

@author: jayakrishnangopalakrishnannair
"""

from web3 import Web3
import time, json
bsc = 'https://bsc-dataseed.binance.org/'
web3 = Web3(Web3.HTTPProvider(bsc))

print(web3.isConnected())

address = input("Enter your wallet address")


if((web3.isAddress(address)) == "False"):
    input("The address is not valid, enter a valid addres ")

balance = web3.eth.getBalance(address)
print(balance)

result = web3.fromWei(balance, 'ether')
print(result)
 