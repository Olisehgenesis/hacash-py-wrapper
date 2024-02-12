import requests


class Miner:
    @staticmethod
    def raise_transaction_fee(txhash, fee, fee_prikey, unitmei=False, txbody=None):
        """
        Increase transaction fee for confirmation.

        Args:
            txhash (str): The hash value of the transaction to increase the fee.
            fee (str): The target fee to be modified.
            fee_prikey (str): The private key of the fee address.
            unitmei (bool): Optional, whether to use the unit "piece" as the unit passed in the fee field.
            txbody (str): Optional, when the transaction does not exist in the transaction pool, modify the fee by using the submitted txbody, and broadcast the transaction to the whole network again.

        Returns:
            dict: Dictionary containing the result of the fee increase operation.
        """
        url = f"http://rpcapi.hacash.org/operate?action=raise_tx_fee&txhash={txhash}&fee={fee}&fee_prikey={fee_prikey}&unitmei={unitmei}"
        if txbody:
            url += f"&txbody={txbody}"

        response = requests.get(url)
        return response.json()
