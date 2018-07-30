import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '9270cbcb'.decode('hex')
P2P_PORT = 17888
ADDRESS_VERSION = 127
SCRIPT_ADDRESS_VERSION = 19
RPC_PORT = 17810
RPC_CHECK = defer.inlineCallbacks(lambda mogwaid: defer.returnValue(
            'mogwaiaddress' in (yield mogwaid.rpc_help()) and
            (yield mogwaid.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('mogwai_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('mogwai_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'tMOG'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'MogwaiCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/MogwaiCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.mogwaicore'), 'mogwai.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://test.explorer.mogwai.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://test.explorer.mogwai.org/address/'
TX_EXPLORER_URL_PREFIX = 'https://test.explorer.mogwai.org/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**20 - 1)
DUST_THRESHOLD = 0.001e8
