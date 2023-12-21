# Reverse the elements of a sequence S from start to end position
# S = [1, 2, 3, 4, 5, 6, 7]
# start = 1
# end = 4
# output:: S = [1, 5, 4, 3, 2, 6, 7]

def reverse(S, start, end):
    if start < end:
        S[start], S[end] = S[end], S[start] # swap elements
        reverse(S, start + 1, end - 1) # recursive call 


S = [1, 2, 3, 4, 5, 6, 7]
start = 1
end = 4

reverse(S, start, end)
print(S)
    