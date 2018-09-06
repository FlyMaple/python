# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                          type / isinstance                        #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class A:
    pass

class B(A):
    pass

print("==================")
print(A) # <class '__main__.A'>
print(B) # <class '__main__.B'>

print("==================")
print(type(A)) # <class 'type'>
print(type(B)) # <class 'type'>

print("==================")
print(type(A())) # <class 'type'>
print(type(B())) # <class 'type'>
print(type(A()) == A) # <class 'type'> == <class '__main__.A'> => True
print(type(B()) == A) # <class 'type'> == <class '__main__.A'> => False

print("==================")
print(isinstance(A(), A)) # True
print(isinstance(B(), A)) # True

# type() 不認為子類等於父類
# isinstance() 認為子類等於父類
