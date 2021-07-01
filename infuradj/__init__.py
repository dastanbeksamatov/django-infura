"""Django infura
    >>> from django_infura import send_tx
    >>> send_tx()
"""
from infuradj.tx import NETWORK_IDS, __setup, get_tx_details, send_tx

__version__ = "1.0.0"
