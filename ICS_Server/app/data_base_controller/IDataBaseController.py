class IDataBaseController:
    """
        Class that describe interface for Data Base.
    """

    def connect(self) -> bool:
        """ Method that should implements database connections. """
        raise NotImplementedError

    def disconnect(self) -> bool:
        """ Method that should implements database disconnections. """
        raise NotImplementedError

    def fetch(self) -> []:
        """ Method that should implements obtaining data from database. """
        raise NotImplementedError

    def commit(self) -> bool:
        """ Method that should implements saving data to database. """
        raise NotImplementedError
