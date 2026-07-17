import json
from pathlib import Path
from typing import Dict, List

from .base import BaseConnector

DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "meeting_notes"


class MockNotesConnector(BaseConnector):
    def __init__(self, data_dir: Path = DATA_DIR):
        self._data_dir = data_dir

    def fetch(self, client_id: str) -> List[Dict]:
        notes_file = self._data_dir / f"{client_id}.json"
        if not notes_file.exists():
            return []
        return json.loads(notes_file.read_text())
