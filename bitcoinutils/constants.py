# TODO organise constants in sections

NETWORK_WIF_PREFIXES = { 'mainnet': b'\x80',
                         'testnet': b'\xef' }

NETWORK_P2PKH_PREFIXES = { 'mainnet': b'\x00',
                           'testnet': b'\x6f' }

NETWORK_P2SH_PREFIXES = { 'mainnet': b'\x05',
                          'testnet': b'\xc4' }

NETWORK_SEGWIT_PREFIXES = { 'mainnet' : 'bc',  # b'\x03\x03\x00\x02\x03',
                            'testnet' : 'tb' } #b'\x03\x03\x00\x14\x02' }

P2PKH_ADDRESS = "p2pkh"
P2SH_ADDRESS = "p2sh"
P2WPKH_ADDRESS_V0 = "p2wpkhv0"
P2WSH_ADDRESS_V0 = "p2wshv0"
SEGWIT_VERSION = 0

SIGHASH_ALL = 0x01
SIGHASH_NONE = 0x02
SIGHASH_SINGLE = 0x03
SIGHASH_ANYONECANPAY = 0x80

DEFAULT_TX_SEQUENCE = b'\xff\xff\xff\xff'
EMPTY_TX_SEQUENCE = b'\x00\x00\x00\x00'
DEFAULT_TX_LOCKTIME = b'\x00\x00\x00\x00'
#ABSOLUTE_TIMELOCK_SEQUENCE = b'\xff\xff\xff\xfe'
#RELATIVE_TIMELOCK_SEQUENCE = b'\xef\xff\xff\xff'

# TX version 2 was introduced in BIP-68 with relative locktime -- tx v1
# does not support relative locktime
DEFAULT_TX_VERSION  = b'\x02\x00\x00\x00'

SATOSHIS_PER_BITCOIN = 100000000
NEGATIVE_SATOSHI = -0.00000001
