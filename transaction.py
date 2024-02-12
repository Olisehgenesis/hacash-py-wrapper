import requests

class Transaction:
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount

    def send(self):
        # Implementation to send transaction
        pass

    @staticmethod
    def create_hacash_transfer_transaction(main_prikey, fee, amount, to_address, timestamp=None, unitmei=True):
        """
        Create HAC transfer transaction.

        Args:
            main_prikey (str): The private key hex string of the main address/handling fee address.
            fee (str): The fee value to be given for the transaction.
            amount (str): The transfer amount.
            to_address (str): Counter (receiving) account address.
            timestamp (int, optional): The timestamp of the transaction.
            unitmei (bool, optional): Whether to use the unit "mei" floating point number form to analyze the passed amount parameter.

        Returns:
            dict: Dictionary containing transaction information.
        """
        url = "http://rpcapi.hacash.org/create?action=value_transfer_tx&main_prikey=" + main_prikey + \
              "&fee=" + fee + "&unitmei=" + str(unitmei) + "&transfer_kind=hacash&amount=" + amount + \
              "&to_address=" + to_address
        if timestamp:
            url += "&timestamp=" + str(timestamp)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def create_btc_transfer_transaction(main_prikey, fee, amount, to_address, timestamp=None, unitmei=True):
        """
        Create BTC transfer transaction.

        Args:
            main_prikey (str): The private key hex string of the main address/handling fee address.
            fee (str): The fee value to be given for the transaction.
            amount (int): The amount of bitcoins to be paid, in units of "satoshi".
            to_address (str): Counter (receiving) account address.
            timestamp (int, optional): The timestamp of the transaction.
            unitmei (bool, optional): Whether to use the unit "mei" floating point number form to analyze the passed amount parameter.

        Returns:
            dict: Dictionary containing transaction information.
        """
        url = "http://rpcapi.hacash.org/create?action=value_transfer_tx&main_prikey=" + main_prikey + \
              "&fee=" + fee + "&unitmei=" + str(unitmei) + "&transfer_kind=satoshi&amount=" + str(amount) + \
              "&to_address=" + to_address
        if timestamp:
            url += "&timestamp=" + str(timestamp)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def create_block_diamond_transfer_transaction(main_prikey, fee, diamonds, to_address, diamond_owner_prikey=None, timestamp=None, unitmei=True):
        """
        Create block diamond transfer transaction.

        Args:
            main_prikey (str): The private key hex string of the main address/handling fee address.
            fee (str): The fee value to be given for the transaction.
            diamonds (str): The literal value of diamonds separated by commas.
            to_address (str): The account address of the other party (receiving diamonds).
            diamond_owner_prikey (str, optional): The account private key of the payment (payment of diamonds, diamond owner).
            timestamp (int, optional): The timestamp of the transaction.
            unitmei (bool, optional): Whether to use the unit "mei" floating point number form to analyze the passed amount parameter.

        Returns:
            dict: Dictionary containing transaction information.
        """
        url = "http://rpcapi.hacash.org/create?action=value_transfer_tx&main_prikey=" + main_prikey + \
              "&fee=" + fee + "&unitmei=" + str(unitmei) + "&transfer_kind=diamond&diamonds=" + diamonds + \
              "&to_address=" + to_address
        if diamond_owner_prikey:
            url += "&diamond_owner_prikey=" + diamond_owner_prikey
        if timestamp:
            url += "&timestamp=" + str(timestamp)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def submit_transaction(hexbody):
        """
        Submit a transaction to the transaction pool.

        Args:
            hexbody (str): The transaction body and content in the form of hex string.

        Returns:
            dict: Response from the server containing transaction submission status.
        """
        url = "http://rpcapi.hacash.org/submit?action=transaction&hexbody=" + hexbody
        response = requests.post(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
