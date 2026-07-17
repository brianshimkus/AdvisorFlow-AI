import re
from pathlib import Path
from typing import Dict, List

from .base import BaseConnector

DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "playbooks"

FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


class MockPlaybookConnector(BaseConnector):
    def __init__(self, data_dir: Path = DATA_DIR):
        self._data_dir = data_dir

    def fetch(self, client_id: str) -> List[Dict]:
        # Playbooks are general internal guidance, not tied to a specific
        # client, so client_id is accepted for interface consistency with
        # the other connectors but isn't used to filter results.
        snippets = []
        for path in sorted(self._data_dir.glob("*.md")):
            match = FRONTMATTER_PATTERN.match(path.read_text())
            if not match:
                continue
            frontmatter, body = match.groups()
            fields = dict(
                line.split(":", 1) for line in frontmatter.strip().splitlines()
            )
            snippets.append(
                {
                    "source_id": fields["source_id"].strip(),
                    "source_type": fields["source_type"].strip(),
                    "snippet": body.strip(),
                }
            )
        return snippets
