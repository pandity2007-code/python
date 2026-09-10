l=[2,3,4,6]

squarelist=[]

# for i in l:
#     squarelist.append(i*i)
# print(squarelist)

squarelist=[i*i for i in l]  # this is done by list comprehension
print(squarelist)