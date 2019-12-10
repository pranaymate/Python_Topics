# c_ tracer
#     ___ - ____ func
#         ____.calls _ 0
#         ____.func  _ f..
#     ___ -c ____ 0a..
#         ____.ca.. +_ 1
#         print('call /_ to /_' / ____.c... ____.f__. -n
#         ____.f... 0a..
#
# 0t..                      # Same as spam = tracer(spam)
# ___ spam(a, b, c):            # Wrap spam in a decorator object
#     print(a, b, c)
#
# spam(1, 2, 3)                 # Really calls the tracer wrapper object
# spam('a', 'b', 'c')           # Invokes __call__ in class
# spam(4, 5, 6)                 # __call__ adds logic and runs original object
