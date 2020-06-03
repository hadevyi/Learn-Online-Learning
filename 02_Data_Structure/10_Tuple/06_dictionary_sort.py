(0, 1, 2) < (5, 1, 2)                       # True
(0, 1, 2000000) < (0, 3, 4)                 # True
( 'Jones', 'Sally' ) < ('Jones', 'Sam')     # True
( 'Jones', 'Sally') > ('Adams', 'Sam')      # True

tups = d.items()
print(tups)                                 # dict_items([('csev', 2), ('cwen', 4)])
                                            # only check "Key", not check values.
