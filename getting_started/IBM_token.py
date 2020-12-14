"""
    Setup IBM quantum experience account, this will allow
    the qiskit env to send real quantum computers at IBM.
    The token is found under My account on the webpage.
"""

from qiskit import IBMQ

IBMQ.save_account('MyToken')