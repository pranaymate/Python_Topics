# # Coding Exceptions Classes
# c_ General ? p..
# c_ Specific1 G.. p..
# c_ Specific2 G.. p..
#
# ___ raiser0 r____ G...
# ___ raiser1 r____ S.1
# ___ raiser2 r____ S.2
#
# ___ func i_ _0 _1 _2
#     t__
#         ?
#     e___ G.. a_ X                     # X is the raised instance
#         print('caught:' X. -c        # Same as sys.exc_info()[0]