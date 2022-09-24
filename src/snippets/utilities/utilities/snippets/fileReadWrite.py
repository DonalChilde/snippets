from pathlib import Path
from typing import List

# an example of how to get a path relative to the current file
RESOURCES_DIR = Path(__file__).parent / Path("resources")
TMP_DIR = Path(__file__).parent / Path("tmp")


def readLinesFromFile(path: Path) -> List[str]:
    """
    a few scenarios for strip, might want to only strip the newline,
    rstrip("\n")
    """
    lines: List[str] = []
    with open(path, "r") as inFile:
        lines = [line.strip() for line in inFile]
    return lines


# Note: writelines does NOT add a newline to each line
def saveLines(stringList: List[str], filePath: Path) -> bool:
    with open(filePath, "w") as fileOut:
        fileOut.writelines(stringList)
    return True


def saveString(data: str, path: Path) -> bool:
    with open(path, "w") as outFile:
        outFile.write(data)
    return True
