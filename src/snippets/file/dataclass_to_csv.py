import csv
from dataclasses import asdict
from pathlib import Path
from typing import List, Literal, Optional


def dataclass_to_csv(
    file_out: Path,
    data: List,
    fields: Optional[str] = None,
    skip_fields: str = "",
):
    if fields is None:
        fieldnames = list(asdict(data[0]).keys())
    else:
        fieldnames = fields.split()
    skips = skip_fields.split()
    for skip in skips:
        fieldnames.remove(skip)
    if skips or fields is not None:
        extras: Literal["raise", "ignore"] = "ignore"
    else:
        extras = "raise"
    with open(file_out, "w", newline="", encoding="utf-8") as csv_file:
        print("in the open")
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction=extras)
        writer.writeheader()
        for row in data:
            writer.writerow(asdict(row))
