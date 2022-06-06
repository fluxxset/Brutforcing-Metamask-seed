import threading
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
from  etherscan import Etherscan
import time
import os

keyli = ["UDZ9J7354TCFF21VDTU37U585E9FUKQUPG"]

def readdr():    
    MNEMONIC: str = generate_mnemonic(language="english", strength=128)
    PASSPHRASE: Optional[str] = None  # "meherett"
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
    bip44_hdwallet.from_mnemonic(
        mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE
    )
    bip44_hdwallet.clean_derivation()
    address_index=0
    bip44_derivation: BIP44Derivation = BIP44Derivation(
        cryptocurrency=EthereumMainnet, account=0, change=False, address=address_index
    )
    bip44_hdwallet.from_path(path=bip44_derivation)

    bip44_hdwallet.clean_derivation()
    return bip44_hdwallet.mnemonic(),bip44_hdwallet.address()


def getone(num):
    eth = Etherscan(num)
    while True:
        me,addr = readdr()
        
        bal = str(float(eth.get_eth_balance(addr))/10000000000000000000)
        if bal != '0.0':
            print(bal,me,addr)
            os.system(f'echo {bal} {me} {addr} >> valid.txt')
        else:
            print(bal,me,addr)
            pass
    
  
if __name__ == "__main__":
    # creating thread
 
    getone(keyli[0])
