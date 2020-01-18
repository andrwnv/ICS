class IConfigurable:
    def sync(self) -> None:
        """ Method that should implements saving current config params. """
        raise NotImplementedError

    def set_value(self, category: str, field: str, value: str) -> None:
        """ Method that should implements saving some field to config. """
        raise NotImplementedError

    def value(self, category: str, field: str) -> str:
        """ Method that should implements getting some field from config. """
        raise NotImplementedError
