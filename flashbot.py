from web3 import Web3
from web3.providers import HTTPProvider
from threading import Thread
from decimal import Decimal
import time

# Sniper 类
class Sniper():
    # 参数初始化
    def __init__(self):
        # 主网地址
        self.mainnet_url = 'https://bsc-dataseed.binance.org/'
        # 构造 web3 实例
        self.web3 = Web3(HTTPProvider(self.mainnet_url))

        # PancakeSwap: Route v2: 买入, 卖出, 获取 BNB 对 USDT 单价
        # PancakeSwap: Route v2 Address
        self.pancake_route_address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
        # PancakeSwap: Route v2 ABI
        self.pancake_route_abi = '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
        # 智能合约地址
        self.pancake_route_check_sum_address = Web3.toChecksumAddress(self.pancake_route_address)
        # 智能合约实例
        self.pancake_route_check_sum_instance = self.web3.eth.contract(address=self.pancake_route_check_sum_address, abi=self.pancake_route_abi)

        # PancakeSwap: Factory v2: 根据 BNB/USDT 地址, 代币地址 查询 交易对地址
        # PancakeSwap: Factory v2 Address
        self.pancake_factory_address = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
        # PancakeSwap: Factory v2 ABI
        self.pancake_factory_abi = '[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
        # 智能合约地址
        self.pancake_factory_check_sum_address = Web3.toChecksumAddress(self.pancake_factory_address)
        # 智能合约实例
        self.pancake_factory_check_sum_instance = self.web3.eth.contract(address=self.pancake_factory_check_sum_address, abi=self.pancake_factory_abi)

        # PancakeSwap: Pair: 检测池子 BNB/USDT 数量, 代币数量, 从而判断是否开盘, 作为流动性检测
        # PancakeSwap: Pair Address
        self.pancake_pair_address = '0x0eD7e52944161450477ee417DE9Cd3a859b14fD0'
        # PancakeSwap: Pair ABI
        self.pancake_pair_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
        # 智能合约地址
        self.pancake_pair_check_sum_address = Web3.toChecksumAddress(self.pancake_pair_address)
        # 智能合约实例
        self.pancake_pair_check_sum_instance = self.web3.eth.contract(address=self.pancake_pair_check_sum_address, abi=self.pancake_pair_abi)

        # WBNB: 获取钱包 BNB 和 代币 余额
        # WBNB Address
        self.wbnb_address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
        # WBNB ABI
        self.wbnb_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]'
        # 智能合约地址
        self.wbnb_check_sum_address = Web3.toChecksumAddress(self.wbnb_address)
        # 智能合约实例
        self.wbnb_check_sum_instance = self.web3.eth.contract(address=self.wbnb_check_sum_address, abi=self.wbnb_abi)

        # BUSDT: 获取钱包 USDT 和 代币余额
        # BUSDT Address
        self.busdt_address = '0x55d398326f99059ff775485246999027b3197955'
        # BUSDT ABI
        self.busdt_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"_decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
        # 智能合约地址
        self.busdt_check_sum_address = Web3.toChecksumAddress(self.busdt_address)
        # 智能合约实例
        self.busdt_check_sum_instance = self.web3.eth.contract(address=self.busdt_check_sum_address, abi=self.busdt_abi)

        # 交易对由 [address_1, address_2] 获取, 前者常为 BNB/USDT, 后者为 新币地址
        # 交易起始地址: 默认为 BNB/USDT 地址
        self.address_1 = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
        # BNB/USDT
        self.token_1_check_sum_address = Web3.toChecksumAddress(self.wbnb_address)
        # 交易结束地址: 新币地址, 需要用户输入
        self.address_2 = '0xE02dF9e3e622DeBdD69fb838bB799E3F168902c5'
        # 新币
        self.token_2_check_sum_address = Web3.toChecksumAddress(self.address_2)
        # 地址列表
        self.addresses_buy = []
        self.addresses_sell = []

        # 购买货币
        self.money_type = 'bnb'

        # 交易对地址
        self.swap_pair_address = ''

        # 区块 ID
        self.chain_id = 56

        # 矿工费计算: gas_price * gas_limit
        # 买入矿工价格
        self.buy_gas_price = 5
        # 买入矿工数目
        self.buy_gas_limit = 700000
        # 卖出矿工价格
        self.sell_gas_price = 5
        # 卖出矿工数目
        self.sell_gas_limit = 700000
        # 授权矿工价格
        self.gas_price_auth = 5
        # 授权矿工数目
        self.gas_limit_auth = 700000

        # 滑点
        # 购买滑点百分比
        self.slippage_buy = 15

        # 小数位数
        # BNB/USDT 小数位数
        self.decimal_1 = 18
        # 新货币小数位数
        self.decimal_2 = 18

        # 订单持续时间
        self.time_period = 99999999
        # 截止时间
        self.deadline = int(time.mktime(time.localtime()) + self.time_period)

        # 进出总量
        # 购买时 BNB/USDT 总量
        self.count_token_1 = 0.01
        # 出售 token 百分比
        self.per_token_2 = 100
        # USDT 授权数量
        self.count_auth_usdt = 99999999999999999999999999999
        # Token 授权数量
        self.count_auth_token = 99999999999999999999999999999

        # 检测池子是否开盘
        # 交易池子 BNB/USDT 数量检测阈值
        self.token_1_min = 60000
        
        # 交易池子 代币 数量检测阈值
        self.token_2_min = 9999999999999999999999999999

        # 新币流动性状态
        self.liquid_flag = False

        # 购买结果状态
        self.buy_flag = False

        # 止盈模式
        self.control_prof_model = True
        # 止盈模式触发价格
        self.control_prof_price = 9.99
        # 止盈百分比
        self.control_prof_per = 50
        # 止损模式
        self.control_loss_model = True
        # 止损模式触发价格
        self.control_loss_price = 3.33
        # 止损百分比
        self.control_loss_per = 50

        # 实时 新币 价格
        self.real_time_price = 999999.99
        # 实时 BNB 价格
        self.real_time_bnb_price = 999999.99

        # 显示小数点位数
        self.round_min = 18

        # 钱包信息
        # 钱包地址
        self.my_address = '0xe0E18e09BFc4622879AA1994441E4078A51B00bc'
        # 汇款地址
        self.my_check_sum_address = Web3.toChecksumAddress(self.my_address)
        # 钱包私钥
        self.my_private_key = ''

        # 线程管理
        self.price_thread_flag = True
        self.buy_thread_flag = True
        self.loss_thread_flag = True
        self.prof_thread_flag = True

        # 间隔时间
        self.sleep_time = 0.01

        # 打印次数
        self.print_interval = 30000000000

        # 实际消耗BNB/USDT及获取Token币数
        self.act_count_in = 0
        self.act_count_out = 0

        # 买入价格
        self.act_price = 0

    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    
    # 精度转换
    def decimal_change(self, decimal_int):
        decimal_int = int(decimal_int)
        if decimal_int == 0:
            return 'wei'
        elif decimal_int == 3:
            return 'kwei'
        elif decimal_int == 6:
            return 'mwei'
        elif decimal_int == 9:
            return 'gwei'
        elif decimal_int == 12:
            return 'microether'
        elif decimal_int == 15:
            return 'milliether'
        elif decimal_int == 18:
            return 'ether'
        elif decimal_int == 21:
            return 'kether'
        elif decimal_int == 24:
            return 'mether'
        elif decimal_int == 27:
            return 'gether'
        elif decimal_int == 30:
            return 'tether'
        else:
            return 'ether'
    
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    
    # 发送请求
    def send_txn(self, txn):
        # 账户
        signed_txn = self.web3.eth.account.signTransaction(txn, private_key=self.my_private_key)
        # 转十六进制
        res = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction.hex())
        # 交易凭据
        txn_receipt = self.web3.eth.waitForTransactionReceipt(res)
        # 返回凭据
        return txn_receipt

    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    
    # USDT: 授权交易
    def approve_usdt(self):
        # 授权给路由地址
        pancake_route_address = self.pancake_route_check_sum_address

        # 交易数额
        amount_in = self.web3.toWei(self.count_auth_usdt, 'ether')
        
        # 授权
        tx = self.busdt_check_sum_instance.functions.approve(pancake_route_address, amount_in).buildTransaction(
            {
                'chainId': self.chain_id,
                'nonce': self.web3.eth.getTransactionCount(self.my_check_sum_address),
                'gas': self.gas_limit_auth,
                'gasPrice': self.web3.toWei(self.gas_price_auth, "gwei"),
                'value': self.web3.toWei(0, 'ether')
            }
        )

        # 广播授权
        th = self.send_txn(tx)

        # 打印结果
        print("[普通显示]授权结果: {0}".format(th))

        # 返回
        return
    
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    
    # Token: 授权交易
    def approve_token(self):
        # 代币合约实例化
        token_instance = self.web3.eth.contract(address=self.token_2_check_sum_address, abi=self.wbnb_abi)
        
        # 授权给路由地址
        pancake_route_address = self.pancake_route_check_sum_address

        # 交易数额
        amount_in = self.web3.toWei(self.count_auth_token, self.decimal_change(decimal_int=self.decimal_2))
        
        # 授权
        tx = token_instance.functions.approve(pancake_route_address, amount_in).buildTransaction(
            {
                'chainId': self.chain_id,
                'nonce': self.web3.eth.getTransactionCount(self.my_check_sum_address),
                'gas': self.gas_limit_auth,
                'gasPrice': self.web3.toWei(self.gas_price_auth, "gwei"),
                'value': self.web3.toWei(0, 'ether')
            }
        )

        # 广播授权
        th = self.send_txn(tx)

        # 打印结果
        print("[普通显示]授权结果: {0}".format(th))
                
        # 返回
        return

    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    
    # BNB: 市价买入
    def buy_market_bnb(self):
        # 购买
        tx = self.pancake_route_check_sum_instance.functions.swapExactETHForTokens(0, self.addresses_buy, self.my_check_sum_address, self.deadline).buildTransaction(
            {
                'chainId': self.chain_id,
                'nonce': self.web3.eth.getTransactionCount(self.my_check_sum_address),
                'gas': self.buy_gas_limit,
                'gasPrice': self.web3.toWei(self.buy_gas_price, "gwei"),
                'value': self.web3.toWei(self.count_token_1, 'ether')
            }
        )

        # 广播交易
        th = self.send_txn(tx)

        # 修改购买结果
        bnb_balance, token_balance = self.query_balance()
        if token_balance > 0:
            print("[成功显示]交易成功")
            # 设置购买状态
            self.buy_flag = True
        else:
            print("[错误显示]交易失败")

        # 打印结果
        print("[普通显示]市价买入: {0}".format(th))
        
        # 获取数量
        logs_1 = th['logs'][0]['data']
        logs_2 = th['logs'][1]['data']
        logs_3 = th['logs'][2]['data']
        # print("[普通显示]16进制数据: In: {0}; Out: {1};".format(logs_1, logs_3))

        # 16 进制转 10 进制
        logs_1 = int(logs_1, 16)
        logs_3 = int(logs_3, 16)
        # print("[普通显示]10进制数据: In: {0}; Out: {1};".format(logs_1, logs_3))

        # 数量转换
        self.act_count_in = self.web3.fromWei(logs_1, 'ether')
        self.act_count_out = self.web3.fromWei(logs_3, self.decimal_change(decimal_int=self.decimal_2))
        print("[普通显示]实际数据: In: {0}; Out: {1};".format(self.act_count_in, self.act_count_out))

        # 交易单价
        self.act_price = self.act_count_in / self.act_count_out * self.real_time_bnb_price
        print("[普通显示]买入单价: {0} USDT".format(self.act_price))
    
        # 返回
        return
    
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    
    # USDT: 市价买入
    def buy_market_usdt(self):
        # 小数点处理后数据
        amount_in = self.web3.toWei(self.count_token_1, 'ether')

        # 购买
        tx = self.pancake_route_check_sum_instance.functions.swapExactTokensForTokens(amount_in, 0, self.addresses_buy, self.my_check_sum_address, self.deadline).buildTransaction(
            {
                'chainId': self.chain_id,
                'nonce': self.web3.eth.getTransactionCount(self.my_check_sum_address),
                'gas': self.buy_gas_limit,
                'gasPrice': self.web3.toWei(self.buy_gas_price, "gwei"),
                'value': self.web3.toWei(0, 'ether')
            }
        )

        # 广播交易
        th = self.send_txn(tx)

        # 修改购买结果
        bnb_balance, token_balance = self.query_balance()
        if token_balance > 0:
            print("[成功显示]交易成功")
            # 设置购买状态
            self.buy_flag = True
        else:
            print("[错误显示]交易失败")

        # 打印结果
        print("[普通显示]市价买入: {0}".format(th))

        # 获取数量
        logs_1 = th['logs'][0]['data']
        logs_2 = th['logs'][1]['data']
        logs_3 = th['logs'][2]['data']
        # print("[普通显示]16进制数据: In: {0}; Out: {1};".format(logs_1, logs_3))

        # 16 进制转 10 进制
        logs_1 = int(logs_1, 16)
        logs_3 = int(logs_3, 16)
        # print("[普通显示]10进制数据: In: {0}; Out: {1};".format(logs_1, logs_3))

        # 数量转换
        self.act_count_in = self.web3.fromWei(logs_1, 'ether')
        self.act_count_out = self.web3.fromWei(logs_3, self.decimal_change(decimal_int=self.decimal_2))
        print("[普通显示]实际数据: In: {0}; Out: {1};".format(self.act_count_in, self.act_count_out))

        # 交易单价
        self.act_price = self.act_count_in / self.act_count_out
        print("[普通显示]买入单价: {0} USDT".format(self.act_price))

        # 返回
        return
    
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    
    # 市价卖出
    def sell_market(self, count_in_s):
        # 小数点处理后数据
        amount_in = self.web3.toWei(count_in_s, self.decimal_change(decimal_int=self.decimal_2))

        # 出售
        tx = self.pancake_route_check_sum_instance.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(amount_in, 0, self.addresses_sell, self.my_check_sum_address, self.deadline).buildTransaction(
            {
                'chainId': self.chain_id,
                'nonce': self.web3.eth.getTransactionCount(self.my_check_sum_address),
                'gas': self.sell_gas_limit,
                'gasPrice': self.web3.toWei(self.sell_gas_price, "gwei"),
                'value': self.web3.toWei(0, 'ether')
            }
        )

        # 广播交易
        th = self.send_txn(tx)

        # 打印结果
        print("[普通显示]市价卖出: {0}".format(th))

        # 返回
        return

    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    
    # 获取账户余额
    def query_balance(self):
        # 代币合约实例化
        token_instance = self.web3.eth.contract(address=self.token_2_check_sum_address, abi=self.wbnb_abi)

        # 获取 token 名称
        token_name = token_instance.functions.name().call()

        # 获取钱包的 token 余额
        token_balance = self.web3.fromWei(token_instance.functions.balanceOf(self.my_check_sum_address).call(), self.decimal_change(decimal_int=self.decimal_2))

        # 获取 BNB 余额
        bnb_balance = self.web3.fromWei(self.web3.eth.getBalance(self.my_check_sum_address), 'ether')

        # 打印余额
        print("[普通显示]BNB 余额: {0}; {1} 余额: {2}".format(bnb_balance, token_name, token_balance))

        # 返回余额
        return bnb_balance, token_balance

    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################

    # 根据 (BNB地址/USDT地址, 代币地址) 查询 交易对地址
    def find_pair_addr(self):
        # 查询交易对地址
        pair_address = self.pancake_factory_check_sum_instance.functions.getPair(self.token_1_check_sum_address, self.token_2_check_sum_address).call()

        # 交易对地址
        print("[普通显示]合约地址: {0}; 交易对地址: {1}".format(self.token_2_check_sum_address, pair_address))

        # 流动性地址
        self.swap_pair_address = Web3.toChecksumAddress(pair_address)

        # self.print_all_para()
        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

    # BNB/USDT: 检测池子大小
    def getReserveOfToken(self):
        # 未检测到流动性变化则一直循环
        while self.liquid_flag == False:
            # 线程跳出
            if self.buy_thread_flag == False:
                break
    
            # 代币合约实例化
            token_instance = self.web3.eth.contract(address=self.token_2_check_sum_address, abi=self.wbnb_abi)
            # BNB/USDT 数量
            if self.money_type == 'bnb':
                reserve1 = self.web3.fromWei(self.wbnb_check_sum_instance.functions.balanceOf(self.swap_pair_address).call(), 'ether')
            else:
                reserve1 = self.web3.fromWei(self.busdt_check_sum_instance.functions.balanceOf(self.swap_pair_address).call(), 'ether')
            # 代币 数量
            reserve2 = self.web3.fromWei(token_instance.functions.balanceOf(self.swap_pair_address).call(), self.decimal_change(decimal_int=self.decimal_2))

            # 打印池子数据
            print("[普通显示]池子大小: BNB 数: {0}, Token 数: {1}".format(reserve1, reserve2))
            
            # BNB 和 Token 数量只需要满足一个就开始抢
            # 检测 BNB 数量
            if reserve1 >= self.token_1_min:
                # 流动性修改
                #LIQUL_FLAG = True
                self.liquid_flag = True

                # 开始抢币
                print("[普通显示]BNB 数量满足, 开始抢币!")

            # 检测 代币 数量
            elif reserve2 >= self.token_2_min:
                # 流动性修改
                # LIQUL_FLAG = True
                self.liquid_flag = True

                # 开始抢币
                print("[普通显示]Token 数量满足, 开始抢币!")

            # 等待时间
            time.sleep(self.sleep_time)

        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

    # 市价购买多线程
    def buy_market_thread(self):
        # 计数打印
        count_liqul = 0

        # 等待流动性
        while self.liquid_flag == False:
            # 线程跳出
            if self.buy_thread_flag == False:
                break
            count_liqul += 1
            if count_liqul % self.print_interval == 0:
                print("[普通显示]已搜寻 {0} 次, 仍未开盘".format(count_liqul))

        # 开始抢币
        while self.buy_flag == False:
            # 线程跳出
            if self.buy_thread_flag == False:
                break
            try:
                # 市价抢币
                if self.money_type == 'bnb':
                    self.buy_market_bnb()
                else:
                    self.buy_market_usdt()
            except:
                print("[错误显示]地址错误 或 BNB/USDT 余额不足")

        # 显示余额
        self.query_balance()
        
        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

    # 购买
    def buy_model_type(self):
        # 校验参数
        # self.print_all_para()
        
        # 流动性检测
        worker = Thread(target=self.getReserveOfToken)
        # 市价抢购
        buy_market_worker1 = Thread(target=self.buy_market_thread)

        # 启动线程
        worker.start()
        buy_market_worker1.start()
        
        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
        
    # 出售模式: 出售新币
    def sell_model_type(self):
        # 校验参数
        # self.print_all_para()

        # 背包余量
        bnb_balance_bag, token_balance_bag = self.query_balance()

        # 若背包中代币数量为 0, 停止出售
        if token_balance_bag <= 0:
            print("[普通显示]背包中代币数量为 0, 不进行出售")
        else:
            # 出售数目
            token_balance = Decimal(self.per_token_2 / 100) * token_balance_bag
            # 市价出售
            try:
                # 市价出售
                self.sell_market(token_balance)
            except:
                print("[普通显示]手续费不足 或 余额不足")

            # 显示余额
            self.query_balance()
        
        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

    # 获取价格
    def get_price_real_time_bnb(self):
        # 1 个 WBNB
        wbnb_one = self.web3.toWei(1, 'ether')

        while True:
            # 线程跳出
            if self.price_thread_flag == False:
                # 价格显示
                print("[普通显示]当前价格: 0.0")
                break

            # 计算 1 个 WBNB 能换多少 USDT
            self.real_time_bnb_price = self.web3.fromWei(self.pancake_route_check_sum_instance.functions.getAmountsOut(wbnb_one, [self.wbnb_check_sum_address, self.busdt_check_sum_address]).call()[1], 'ether')

            # 代币合约实例化
            token_instance = self.web3.eth.contract(address=self.token_2_check_sum_address, abi=self.wbnb_abi)
            # BNB/USDT 数量
            reserve1 = self.web3.fromWei(self.wbnb_check_sum_instance.functions.balanceOf(self.swap_pair_address).call(), 'ether')
            # 代币 数量
            reserve2 = self.web3.fromWei(token_instance.functions.balanceOf(self.swap_pair_address).call(), self.decimal_change(decimal_int=self.decimal_2))
            # 防止出现 Token 为 0, 除法无法进行
            if reserve2 == 0:
                reserve2 = self.web3.fromWei(1000000000000000000, 'ether')
            
            # 价格计算
            self.real_time_price = reserve1 / reserve2 * self.real_time_bnb_price
            # 小数位数
            self.real_time_price = round(self.real_time_price, self.round_min)
            # 价格显示
            print('[普通显示]当前 Token 价格为: %.20f USDT' % self.real_time_price)

            # 等待时间
            time.sleep(self.sleep_time)
        
        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

     # 获取价格
    def get_price_real_time_usdt(self):
        while True:
            # 线程跳出
            if self.price_thread_flag == False:
                # 价格显示
                print("[普通显示]当前价格: 0.0")
                break

            # 代币合约实例化
            token_instance = self.web3.eth.contract(address=self.token_2_check_sum_address, abi=self.wbnb_abi)
            # BNB/USDT 数量
            reserve1 = self.web3.fromWei(self.busdt_check_sum_instance.functions.balanceOf(self.swap_pair_address).call(), 'ether')
            # 代币 数量
            reserve2 = self.web3.fromWei(token_instance.functions.balanceOf(self.swap_pair_address).call(), self.decimal_change(decimal_int=self.decimal_2))
            
            # 防止出现 Token 为 0, 除法无法进行
            if reserve2 == 0:
                reserve2 = self.web3.fromWei(1000000000000000000, 'ether')

            # 价格计算
            self.real_time_price = reserve1 / reserve2
            # 小数位数
            self.real_time_price = round(self.real_time_price, self.round_min)
            # 价格显示
            print('[普通显示]当前 Token 价格为: %.20f USDT' % self.real_time_price)

            # 等待时间
            time.sleep(self.sleep_time)
        
        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

    # 获取实时价格
    def get_price(self):
        # BNB
        if self.money_type == 'bnb':
            # 实时价格
            price_work = Thread(target=self.get_price_real_time_bnb)
            # 启动线程
            price_work.start()
        # USDT
        else:
            # 实时价格
            price_work = Thread(target=self.get_price_real_time_usdt)
            # 启动线程
            price_work.start()
        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    
    # 获取 Token 精度
    def get_token_decimal(self):
        # 代币合约实例化
        token_instance = self.web3.eth.contract(address=self.token_2_check_sum_address, abi=self.wbnb_abi)
        # 获取精度
        self.decimal_2 = token_instance.functions.decimals().call()
        # 显示精度
        print("[普通显示]Token 精度为: {0};".format(self.decimal_2))
        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    
    # 止盈
    def prof_sell(self):
        # 校验参数
        # self.print_all_para()

        # 背包余量
        bnb_balance_bag, token_balance_bag = self.query_balance()
        if token_balance_bag <= 0:
            print("[普通显示]背包中代币数量为 0, 不进行止盈")
            return

        # 设置止盈价格
        self.control_prof_price = self.act_price * Decimal(1 + self.control_prof_per / 100)
        print('[普通显示]止盈触发价格: {0} USDT'.format(self.control_prof_price))
         
        # 止盈模式
        while self.control_prof_model == True:
            # 线程跳出
            if self.prof_thread_flag == False:
                break
           
            # 判定价格
            if self.real_time_price >= self.control_prof_price:
                # 市价出售 全部Token
                try:
                    # 市价出售
                    self.sell_market(token_balance_bag)
                except:
                    print("[错误显示]手续费不足 或 余额不足")

                # 显示余额
                self.query_balance()

                # 退出循环
                break
            
            # 等待时间
            time.sleep(self.sleep_time)

        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

    # 止损
    def loss_sell(self):
        # 校验参数
        # self.print_all_para()

        # 背包余量
        bnb_balance_bag, token_balance_bag = self.query_balance()
        if token_balance_bag <= 0:
            print("[错误显示]背包中代币数量为 0, 不进行止损")
            return

        # 设置止损价格
        self.control_loss_price = self.act_price * Decimal(1 - self.control_loss_per / 100)
        print('[普通显示]止损触发价格: {0} USDT'.format(self.control_loss_price))
         
        # 止损模式
        while self.control_loss_model == True:
            # 线程跳出
            if self.loss_thread_flag == False:
                break
           
            # 判定价格
            if self.real_time_price <= self.control_loss_price:
                # 市价出售 全部Token
                try:
                    # 市价出售
                    self.sell_market(token_balance_bag)
                except:
                    print("[错误显示]手续费不足 或 余额不足")

                # 显示余额
                self.query_balance()

                # 退出循环
                break
            
            # 等待时间
            time.sleep(self.sleep_time)

        # 返回
        return

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

    # 止盈
    def control_prof(self):
        # 止盈模式
        prof_work = Thread(target=self.prof_sell)
        # 启动线程
        prof_work.start()

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

    # 止损
    def control_loss(self):
        # 止损模式
        loss_work = Thread(target=self.loss_sell)
        # 启动线程
        loss_work.start()

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

    # 按钮一: 确认
    def initial_run(self):
        # 获取 Token 精度
        self.get_token_decimal()
        # 获取交易对地址
        self.find_pair_addr()
        # 价格获取
        self.get_price()
    
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    
    # 打印所有参数
    def print_all_para(self):
        print("[普通显示]BNB/USDT: {0};".format(self.money_type))
        print("[普通显示]合约地址: {0}; 新币精度: {1};".format(self.token_2_check_sum_address, self.decimal_2))
        print("[普通显示]钱包地址: {0}; 钱包私钥: {1};".format(self.my_check_sum_address, self.my_private_key))
        print("[普通显示]截止时间: {0}; 买入滑点: {1}; Buy Gas Price: {2}; Buy Gas Limit: {3}; Sell Gas Price: {4}; Sell Gas Limit: {5}; BNB/USDT_MIN: {6}; TOKEN_MIN: {7};".format(self.deadline, self.slippage_buy, self.buy_gas_price, self.buy_gas_limit, self.sell_gas_price, self.sell_gas_limit, self.token_1_min, self.token_2_min))
        print("[普通显示]买入花费金额: {0};".format(self.count_token_1))
        print("[普通显示]买入单价: {0}; 消耗 BNB/USDT: {1}; 获取 Token: {2};".format(self.act_price, self.act_count_in, self.act_count_out))
        print("[普通显示]卖出百分比: {0};".format(self.per_token_2))
        print("[普通显示]止损百分比: {0}; 止损价格: {1};".format(self.control_loss_per, self.control_loss_price))
        print("[普通显示]止盈百分比: {0}; 止盈价格: {1};".format(self.control_prof_per, self.control_prof_price))

        # 返回
        return
    
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    
    # 设置消耗货币类型 BNB/USDT
    def set_consume_token_type(self, type):
        self.money_type = type
        if self.money_type == 'bnb':
            self.address_1 = self.wbnb_address
            self.token_1_check_sum_address = self.wbnb_check_sum_address
        else:
            self.address_1 = self.busdt_address
            self.token_1_check_sum_address = self.busdt_check_sum_address
    
    # 设置新币地址
    def set_buy_token_address(self, address):
        # Token 地址
        self.address_2 = address
        try:
            self.token_2_check_sum_address = Web3.toChecksumAddress(self.address_2)
        except:
            print("[错误显示]买入token地址不合法")
            return False
        return True

    # 保存配置
    def set_para(self, address, private_key, time_period, slippage_buy, gas_price_buy, gas_limit_buy, gas_price_sell, gas_limit_sell, token_1_min, token_2_min):
        self.my_address = address
        self.my_private_key = private_key
        self.time_period = float(time_period) if time_period != "" else 0
        self.slippage_buy = float(slippage_buy) if slippage_buy != "" else 0
        self.buy_gas_price = float(gas_price_buy) if gas_price_buy != "" else 0
        self.buy_gas_limit = int(gas_limit_buy) if gas_limit_buy != "" else 0
        self.sell_gas_price = float(gas_price_sell) if gas_price_sell != "" else 0
        self.sell_gas_limit = int(gas_limit_sell) if gas_limit_sell != "" else 0
        self.token_1_min = float(token_1_min) if token_1_min != "" else 0
        self.token_2_min = float(token_2_min) if token_2_min != "" else 0
        try:
            self.my_check_sum_address = Web3.toChecksumAddress(self.my_address)
        except:
            print("[错误显示]钱包地址不合法")
            return False
        print("[成功显示]信息保存成功")
        return True
    
    # 设置买入卖出交易对
    def set_token_pair(self):
        self.addresses_buy = [self.token_1_check_sum_address, self.token_2_check_sum_address]
        self.addresses_sell = [self.token_2_check_sum_address, self.token_1_check_sum_address]

    # 设置买入总量
    def set_buy_amount(self, amount):
        self.count_token_1 = eval(amount)
    
    # 设置卖出百分比
    def set_sell_per(self, amount):
        self.per_token_2 = eval(amount)
    
    # 设置止损百分比
    def set_loss_per(self, amount):
        self.control_loss_per = eval(amount)
        pass

    # 设置止盈百分比
    def set_profit_per(self, amount):
        self.control_prof_per = eval(amount)
        pass

    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################
    ##########################################################################################################################################################

if __name__ == '__main__':
    # 创建实例
    sni = Sniper()
    
    # 购买货币类型选择
    sni.money_type = 'bnb'
    if sni.money_type == 'bnb':
        sni.address_1 = sni.wbnb_address
        sni.token_1_check_sum_address = sni.wbnb_check_sum_address
    else:
        sni.address_1 = sni.busdt_address
        sni.token_1_check_sum_address = sni.busdt_check_sum_address

    # Token 地址: Bake
    sni.address_2 = '0xE02dF9e3e622DeBdD69fb838bB799E3F168902c5'
    sni.token_2_check_sum_address = Web3.toChecksumAddress(sni.address_2)

    # 初始化买入卖出路径
    sni.addresses_buy = [sni.token_1_check_sum_address, sni.token_2_check_sum_address]
    sni.addresses_sell = [sni.token_2_check_sum_address, sni.token_1_check_sum_address]
    
    # 显示结果
    sni.print_all_para()
    
    # 获取余额
    sni.query_balance()

    # 初始化三步
    sni.initial_run()

    # # 设置钱包信息
    # sni.my_address = ""
    # sni.my_check_sum_address = Web3.toChecksumAddress(sni.my_address)
    # sni.my_private_key = ""

    # # USDT 授权
    # sni.approve_usdt()

    # 市价买入
    sni.buy_model_type()

    # # Token 授权
    # sni.approve_token()
    
    # # 卖出数量
    # sni.per_token_2 = 80
    # # 市价卖出
    # sni.sell_model_type()

    # # 等待
    # time.sleep(10)

    # # 止盈模式开启
    # sni.control_prof_per = 100
    # sni.control_prof()

    # # 止损模式开启
    # sni.control_loss_per = 5
    # sni.control_loss()