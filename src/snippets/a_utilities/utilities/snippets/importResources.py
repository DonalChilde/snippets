# https://realpython.com/python37-new-features/#importing-data-files-with-importlibresources
# python >= 3.7 required, backport available
from importlib import resources


def example():
    with resources.open_text("data", "alice_in_wonderland.txt") as fid:
        alice = fid.readlines()
    return alice


# Does not work as expected
def pathToExample():
    filePath = resources.path("data", "alice_in_wonderland.txt")
