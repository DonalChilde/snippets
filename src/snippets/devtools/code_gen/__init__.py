# TODO make a repr generator, include f-string format examples in docstring. Limit size
#   of attribute repr? f"{foo:<10}"
# https://saralgyaan.com/posts/f-string-in-python-usage-guide/
# TODO make a str generator

# make example of use in pytest, and interpreter, decorator.
# option output to log, stderr

# https://www.delftstack.com/howto/python/python-print-to-stderr/
# print("Error", file = sys.stderr )
# sys.stderr.write("Error!")

# check for previous generation. only output one time.
# add class name to beginning of __repr__,
# https://stackoverflow.com/questions/2020014/get-fully-qualified-class-name-of-an-object-in-python
# to support output multiple classes to file at one time. This would enable adding
# decorators to live code, and generating repr all at once on run.

# use one func to generate str and repr, allow creation of singleton class that will track
# class names, and generation status.
