from web3 import Web3
import time
rpc_url = 'https://binance.llamarpc.com'
web3 = Web3(Web3.HTTPProvider(rpc_url))

contract_address = '0x4306b223ee8edb91f0a38f958c611a2896a46149'
contract_abi = [
    {
        "constant": True,
        "inputs": [{"name": "player", "type": "address"}],
        "name": "player",
        "outputs": [{"name": "", "type": "uint256[3]"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

player_addresses = [
    'addr1', # TODO: set your address
    'addr2', # TODO: set your address
]
contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)

for player_address in player_addresses: 
    player_data = contract.functions.player(player_address).call()
    energy_cela = player_data[0] / 1e18 / 163.5 # 163.5 is the ratio of energy to CELA
    airdrop_cela = player_data[1] / 1e18
    life_cela = player_data[2] / 1e18 / 4.36 # 4.36 is the ratio of life to energy

    energy_cela_50_percent = energy_cela * 0.5
    airdrop_cela_10_percent = airdrop_cela * 0.1
    life_cela_10_percent = life_cela * 0.1


    print(f'{player_address}: {energy_cela}, {airdrop_cela}, {life_cela}, '
          f'total: {energy_cela + airdrop_cela + life_cela}, '
          f'first airdrop CELA: {energy_cela_50_percent + airdrop_cela_10_percent + life_cela_10_percent}')
    time.sleep(0.1)
