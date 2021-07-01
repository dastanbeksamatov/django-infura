import pytest
from decouple import config
from app.infuradj import __setup, get_tx_details, send_tx
from web3.eth import Account

NETWORK_IDS = {
    'mainnet': 1,
    'kovan': 42,
    'rinkeby': 4,
    'goerli': 5,
    'ropsten': 3,
    'polygon-mainnet': 137
}

TEST_PUBLIC_KEY = "0xe36bb1E4026314BD171D5F459f095F9A248f0122"
WRONG_PRIVATE_KEY = "0x454b8249f9d53d57d553d2f555149a47902257409c0789e6f2e45ada0b8cd793"
def test_fail_setup():
    with pytest.raises(RuntimeError, match = "Incorrect project Id or network name") as info:
        __setup('lol', "gc4295415e3f4a14a17e1769253cdef1")
    assert info.type is RuntimeError

def test_send_tx_fail():
    with pytest.raises(TypeError) as info:
        _tx_hash = send_tx(
            "0x121121214124asfgfa",
            "fail message",
            config('TEST_KOVAN_ID'),
            config('PRIVATE_KEY'),
            'kovan'
        )

def test_send_tx_fail_2():
    with pytest.raises(ValueError, match = "Incorrect tx details") as info:
        _tx_hash = send_tx(
            TEST_PUBLIC_KEY,
            "fail message 2",
            config('TEST_KOVAN_ID'),
            'invalid_key',
            'kovan'
        )

def test_kovan_setup():
    w3 = __setup('kovan', config('TEST_KOVAN_ID'))
    assert w3.isConnected() is True
    assert w3.eth.chain_id is NETWORK_IDS['kovan']

def test_polygon_setup():
    w3 = __setup('polygon-mainnet', config('TEST_POLYGON_ID'))
    assert w3.isConnected() is True
    assert w3.eth.chain_id is NETWORK_IDS['polygon-mainnet']

def test_send_tx_kovan():
    tx_hash = send_tx(
        TEST_PUBLIC_KEY, 
        "some message", 
        config('TEST_KOVAN_ID'), 
        config('PRIVATE_KEY'),
        'kovan'
        )
    assert tx_hash is not None

def test_get_tx_details():
    tx_hash = "0x23abda4c69680d057576aca7c35ee696fbda9ac0fd78003614e00d3082cb7d87"
    details = get_tx_details(tx_hash, 'kovan', config('TEST_KOVAN_ID'))
    assert details is not {}
    data = bytes.fromhex(details.get('input')[2:]).decode()
    assert (data == "some message") is True

def test_invalid_tx():
    tx_hash = "0x23dbda4c69680d057576aca7c35ee696fbda9ac0fd78003614e00d3082cb7d87"
    with pytest.raises(RuntimeError, match="Transaction has not been mined yet: {}".format(tx_hash)) as info:
        _details = get_tx_details(tx_hash, 'kovan', config('TEST_KOVAN_ID'))
    assert info.type is RuntimeError
