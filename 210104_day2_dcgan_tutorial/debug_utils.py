import humanize

# # Way 1
# def _ns(size):
#     return humanize.naturalsize(size, binary=True)

# # Way 2
# _ns = lambda size: humanize.naturalsize(size)

# Way 3
from functools import partial

_ns = partial(humanize.naturalsize, binary=True)