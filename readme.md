# HacashRPC Python Wrapper

This Python package provides a convenient interface for interacting with Hacash blockchain via its RPC API. It includes classes for handling accounts, queries, transactions, and mining operations.

## Installation

You can install the HacashRPC package using pip:

```bash
pip install hacashrpc
```

## Usage

### Account

The `Account` class allows you to manage Hacash accounts. It provides methods for generating new accounts, importing existing ones, and querying balance information.

Available methods:

- `generate_new_account()`: Generates a new Hacash account.
- `import_account(private_key)`: Imports an existing Hacash account using its private key.
- `get_balance(address)`: Retrieves the balance of a given Hacash account.

Example usage:

```python
from hacashrpc import Account

# Generate a new account
new_account = Account.generate_new_account()

# Import an existing account
private_key = "your_private_key_here"
imported_account = Account.import_account(private_key)

# Get balance
address = "your_address_here"
balance = Account.get_balance(address)
print(balance)
```

### Query

The `Query` class allows you to query various information from the Hacash blockchain, such as block details, transaction information, and total supply.

Available methods:

- `query_balances(address_list, unitmei, kind)`: Query the balances of one or more accounts.
- `query_diamond(name=None, number=None, unitmei=False)`: Query detailed information about a diamond.
- `query_last_block()`: Query information about the latest valid block.
- `query_block_intro(height=None, hash=None, unitmei=False)`: Query information about a specified block.
- `scan_value_transfers(height=None, txhash=None, txposi=0, kind='hsd', unitmei=False)`: Scan transactions for transfer information.
- `total_supply()`: Query total supply information.

Example usage:

```python
from hacashrpc import Query

# Query account balances
address_list = "address1,address2,address3"
balances = Query.query_balances(address_list, unitmei=True, kind='h')
print(balances)

# Query information about the last block
last_block = Query.query_last_block()
print(last_block)
```

### Transaction

The `Transaction` class allows you to create and broadcast transactions on the Hacash blockchain.

Available methods:

- `create_transaction(sender_address, recipient_address, amount, fee, fee_prikey, unitmei=False)`: Create a new transaction.
- `broadcast_transaction(txbody)`: Broadcast a transaction to the Hacash network.

Example usage:

```python
from hacashrpc import Transaction

# Create a new transaction
sender_address = "sender_address"
recipient_address = "recipient_address"
amount = 10
fee = 1
fee_prikey = "fee_private_key"
transaction = Transaction.create_transaction(sender_address, recipient_address, amount, fee, fee_prikey)
print(transaction)

# Broadcast the transaction
txbody = transaction["txbody"]
result = Transaction.broadcast_transaction(txbody)
print(result)
```

### Miner

The `Miner` class allows you to perform mining operations, such as increasing transaction fees for confirmation.

Available methods:

- `raise_transaction_fee(txhash, fee, fee_prikey, unitmei=False, txbody=None)`: Increase transaction fee for confirmation.

Example usage:

```python
from hacashrpc import Miner

# Increase transaction fee
txhash = "transaction_hash"
fee = "new_fee_amount"
fee_prikey = "fee_private_key"
result = Miner.raise_transaction_fee(txhash, fee, fee_prikey)
print(result)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

