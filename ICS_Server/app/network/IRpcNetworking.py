class IRpcNetworking:
    """
        Class that describe interface for RPC networking.
    """
    
    def run(self) -> None:
        """ Method that should implements starting RPC networking. """
        raise NotImplementedError

    def stop(self) -> None:
        """ Method that should implements the stop RPC networking. """
        raise NotImplementedError

    def bind(self, address: str) -> None:
        """ Method that should implements binding network address for RPC networking. """
        raise NotImplementedError
