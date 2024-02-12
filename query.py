import requests


class Query:
    @staticmethod
    def query_balances(address_list, unitmei, kind):
        """
        Query the balances of one or more accounts.

        Args:
            address_list (str): Comma-separated list of account addresses.
            unitmei (bool): Whether to return balances in units of "mei".
            kind (str): Type of return. Options: 'h', 'hs', 'hsd'.

        Returns:
            dict: Dictionary containing balance information.
        """
        url = f"http://rpcapi.hacash.org/query?action=balances&address_list={address_list}&unitmei={unitmei}&kind={kind}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def query_diamond(name=None, number=None, unitmei=False):
        """
        Query detailed information about a diamond.

        Args:
            name (str): Diamond literal value.
            number (int): Diamond label.
            unitmei (bool): Whether to return values in units of "mei".

        Returns:
            dict: Dictionary containing diamond information.
        """
        if name:
            url = f"http://rpcapi.hacash.org/query?action=diamond&name={name}&unitmei={unitmei}"
        elif number:
            url = f"http://rpcapi.hacash.org/query?action=diamond&number={number}&unitmei={unitmei}"
        else:
            return None

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def query_last_block():
        """
        Query information about the latest valid block.

        Returns:
            dict: Dictionary containing information about the latest block.
        """
        url = "http://rpcapi.hacash.org/query?action=last_block"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def query_block_intro(height=None, hash=None, unitmei=False):
        """
        Query information about a specified block.

        Args:
            height (int): Block height.
            hash (str): Block hash.
            unitmei (bool): Whether to return values in units of "mei".

        Returns:
            dict: Dictionary containing information about the block.
        """
        if height:
            url = f"http://rpcapi.hacash.org/query?action=block_intro&height={height}&unitmei={unitmei}"
        elif hash:
            url = f"http://rpcapi.hacash.org/query?action=block_intro&hash={hash}&unitmei={unitmei}"
        else:
            return None

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def scan_value_transfers(height=None, txhash=None, txposi=0, kind='hsd', unitmei=False):
        """
        Scan transactions for transfer information.

        Args:
            height (int): Block height to scan.
            txhash (str): Transaction hash.
            txposi (int): Index of the transaction in the block.
            kind (str): Type of return. Options: 'h', 'hs', 'hsd'.
            unitmei (bool): Whether to return values in units of "mei".

        Returns:
            dict: Dictionary containing transaction transfer information.
        """
        if txhash:
            url = f"http://rpcapi.hacash.org/query?action=scan_value_transfers&txhash={txhash}&unitmei={unitmei}"
        elif height is not None:
            url = f"http://rpcapi.hacash.org/query?action=scan_value_transfers&height={height}&txposi={txposi}&kind={kind}&unitmei={unitmei}"
        else:
            return None

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def total_supply():
        """
        Query total supply information.

        Returns:
            dict: Dictionary containing total supply information.
        """
        url = "http://rpcapi.hacash.org/query?action=total_supply"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
