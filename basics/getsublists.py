def get_sub_lists(lst):

    sublist = []

    for i in range(len(lst)):

        for j in range(i+1,len(lst)+1):
            sub = lst[i:j]
            sublist.append(sub)

    return sublist


print(get_sub_lists([1]))
