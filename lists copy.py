# [
# (lengtha,[ipi,..,ipk],[desci,..,desck],priority,preview,allow/deny),
# (lengthb,[ipl,..,ipm],[descl,..,descm],priority,preview,allow/deny)
# ]

# [([1, 2, 3], 1), ([2, 3, 4], 2), ([3, 4, 5], 3)]

listoflists = []
a_list = []
for i in range(0, 10):
    a_list.append(i)
    if len(a_list) > 3:
        a_list.remove(a_list[0])
        listoflists.append((list(a_list), a_list[0]))
print listoflists
