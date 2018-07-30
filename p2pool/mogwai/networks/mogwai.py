import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '9170caca'.decode('hex')
P2P_PORT = 17777
ADDRESS_VERSION =50
SCRIPT_ADDRESS_VERSION = 16
RPC_PORT = 17710
RPC_CHECK = defer.inlineCallbacks(lambda mogwaid: defer.returnValue(
            'mogwaiaddress' in (yield mogwaid.rpc_help()) and
            not (yield mogwaid.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('mogwai_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('mogwai_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'MOG'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'MogwaiCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/MogwaiCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.mogwaicore'), 'mogwai.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.mogwai.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.mogwai.org/address/'
TX_EXPLORER_URL_PREFIX = 'https://explorer.mogwai.org/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
