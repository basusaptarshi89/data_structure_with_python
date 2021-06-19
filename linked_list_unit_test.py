import linked_list

llist = linked_list.LinkedList()

print('-'*50)
print('Adding items to list')
print('-'*50)

for i in range(10, 20):
    llist.add(i)
    print(f'Added Item: {i}')
    print(f'List: {llist}')
    print()


print('-'*50)
print('Adding item at beginning of list')
print('-'*50)

llist.add_at_beginning(9)
print(f'Added Item: {9}')
print(f'List: {llist}')
print()


print('-'*50)
print('Adding item at specific position of list')
print('-'*50)

llist.add_at_position(9.5, 1)
print(f'Added Item: {9.5}')
print(f'Position  : {1}')
print(f'List: {llist}')
print()

llist.add_at_position(18.5, 11)
print(f'Added Item: {18.5}')
print(f'Position  : {11}')
print(f'List: {llist}')
print()

llist.add_at_position(8.5, 0)
print(f'Added Item: {8.5}')
print(f'Position  : {0}')
print(f'List: {llist}')
print()

llist.add_at_position(20, 14)
print(f'Added Item: {20}')
print(f'Position  : {14}')
print(f'List: {llist}')
print()


print('-'*50)
print('Removing item from end of list')
print('-'*50)

for i in range(5):
    node = llist.remove()
    print(f'Removed node:\n{node}')
    print(f'List: {llist}')
    print()


print('-'*50)
print('Removing item from beginning of list')
print('-'*50)

for i in range(3):
    node = llist.remove_at_end()
    print(f'Removed node:\n{node}')
    print(f'List: {llist}')
    print()


print('-'*50)
print('Removing item from specific position of list')
print('-'*50)

node = llist.remove_at_position(0)
print(f'Position: {0}')
print(f'List: {llist}')
print(f'Removed node:\n{node}')
print()

node = llist.remove_at_position(0)
print(f'Position: {0}')
print(f'List: {llist}')
print(f'Removed node:\n{node}')
print()

node = llist.remove_at_position(4)
print(f'Position: {4}')
print(f'List: {llist}')
print(f'Removed node:\n{node}')
print()

node = llist.remove_at_position(2)
print(f'Position: {2}')
print(f'List: {llist}')
print(f'Removed node:\n{node}')
print()
