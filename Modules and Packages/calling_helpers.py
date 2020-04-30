# otherfile.py
# we can import file 3 type

# import specific items into current namespace
from helpers import display

# import all into current namespace
# * means all
from helpers import *

# import module as namespace
import helpers

helpers.display('Not a Warning')

display('Not a Warning', True)

display('Not a Warning')
