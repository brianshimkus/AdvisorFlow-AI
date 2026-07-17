import json
from pathlib import Path
from typing import Dict, List

from .base import BaseConnector

DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "account_activity.json"


class MockAccountActivityConnector(BaseConnector):
    def __init__(self, data_path: Path = DATA_PATH):
        self._data_path = data_path

    def fetch(self, client_id: str) -> List[Dict]:
        activity = json.loads(self._data_path.read_text())
        return activity.get(client_id, [])
