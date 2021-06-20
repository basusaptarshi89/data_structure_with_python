import linked_list

llist = linked_list.LinkedList()

llist.add(10)
llist.add(10)
llist.add(11)
llist.add(12)
llist.add(13)
llist.add(13)
llist.add(13)
llist.add(14)
llist.add(14)

print(f'List: {llist}')
llist.remove_duplicate()
print('Removed duplicates')
print(f'List: {llist}')
