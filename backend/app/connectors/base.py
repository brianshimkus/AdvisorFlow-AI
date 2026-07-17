from abc import ABC, abstractmethod
from typing import Any


class ConnectorDataNotFoundError(Exception):
    """Raised when a connector cannot resolve the client_id itself.

    Not raised for a known client with no records of a given type (e.g. a
    client with zero meeting notes) - that's a normal, expected result the
    caller should treat as a missing-data signal, not an error.
    """


class BaseConnector(ABC):
    @abstractmethod
    def fetch(self, client_id: str) -> Any:
        raise NotImplementedError
