from tx.models import Transaction
from 
NETWORK_IDS = {
    'mainnet': 1,
    'kovan': 42,
    'rinkeby': 4,
    'goerli': 5,
    'ropsten': 3,
    'polygon-mainnet': 2
}

def send_tx(to, message, project_id, access_key, network):
    url = "https://{}.infura.io/v3/{}".format(network, project_id)

def sign_tx(access_key, to, message, network):
    web3.sing_transaction()
id: "6872e87746174c819fcca0b3ffdb1272"