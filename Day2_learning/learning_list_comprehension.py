# List comprehensions can include conditional statements to filter or modify items based on specific criteria. 

# l = [1,2,3,4,5,5,7,9,8] 
# evn_l = [i for i in l if i%2==0] 
# print(evn_l)        //[2,4,8] 

# creating a list from a range 
# evn = [i for i in range(10) ] 
# print(evn)      //[0,1,2,3,4,5,6,7,8,9] 

# evn = [i for i in range(10) if i%2==0] 
# print(evn)      //[2,4,6,8]

# simple 3×3 grid.
# Coords = [(x,y) for x in range(3) for y in range(3)]
# Print(coords)		[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# inn = [[1,2,3], [4,5,6], [7,8,9]]
# l = [out for mid in inn for out in mid]
# print(l)

# a = [1,2,3,4,5,6,7,8]
# res = [x*2 for x in a[1::2]]
# print(res)
