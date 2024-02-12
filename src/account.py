import requests

class Wallet:
    def __init__(self, address, private_key, public_key):
        self.address = address
        self.private_key = private_key
        self.public_key = public_key

class Account:
    def __init__(self, address=None):
        self.address = address

    def get_balance(self):
        # Implementation to get balance of the account
        pass

    def create_wallet(self, number=1):
        """
        Create a wallet or multiple wallets.

        Args:
            number (int): Number of wallets to create. Defaults to 1.

        Returns:
            Wallet or list: If only one wallet is created, returns a Wallet object.
                            If multiple wallets are created, returns a list of Wallet objects.
        """
        url = "http://rpcapi.hacash.org/create?action=accounts&number=" + str(number)
        response = requests.get(url)
        if response.status_code == 200:
            wallet_info_list = response.json()["list"]
            if number == 1:
                wallet_info = wallet_info_list[0]
                return Wallet(wallet_info["address"], wallet_info["prikey"], wallet_info["pubkey"])
            else:
                wallets = []
                for wallet_info in wallet_info_list:
                    wallets.append(Wallet(wallet_info["address"], wallet_info["prikey"], wallet_info["pubkey"]))
                return wallets
        else:
            return None

    def create_wallets(self, count=1):
        """
        Create multiple wallets.

        Args:
            count (int): Number of wallets to create. Defaults to 1.

        Returns:
            list: List of Wallet objects.
        """
        return self.create_wallet(number=count)
