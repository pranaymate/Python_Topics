# c_ Spam
#     numInstances = 0                         # Use static method for class data
#     ___ -  ____
#         S__.n.. +_ 1
#     ___ printNumInstances
#         print("Number of instances:", S_.n..
#     printNumInstances _ st... p...
#
# a = ?
# b = ?
# c = ?
# S_.p...                # Call as simple function
# a.p..                    # Instance argument not passed
#
#
# c_ Sub S..
#     ___ p...                 # Override a static method
#         print("Extra stuff...")              # But call back to original
#         S_.p..
#     printNumInstances = st... p..
#
# a = Su.
# b = Su.
# a.p...                    # Call from subclass instance
# # Number of instances: 2
# # Sub.printNumInstances()                  # Call from subclass itself
# # Number of instances: 2
# # Spam.printNumInstances()
# # Number of instances: 2
#
# c_ Other S..
#     p..                       # Inherit static method verbatim
#
# c _ O..
# ?.p...
# # Number of instances: 3
