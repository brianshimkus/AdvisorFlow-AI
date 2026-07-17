import json
from pathlib import Path
from typing import Dict

from .base import BaseConnector, ConnectorDataNotFoundError

DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "clients.json"


class MockCRMConnector(BaseConnector):
    def __init__(self, data_path: Path = DATA_PATH):
        self._data_path = data_path

    def fetch(self, client_id: str) -> Dict:
        clients = json.loads(self._data_path.read_text())
        for client in clients:
            if client["client_id"] == client_id:
                return client
        raise ConnectorDataNotFoundError(
            f"No CRM profile found for client_id={client_id!r}"
        )
