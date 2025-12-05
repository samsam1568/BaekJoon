from itertools import permutations

n = int(input())
k = int(input())
card = []
int_list = []

for _ in range(n):
    card.append(input())

for i in permutations(card, k):
    int_list.append(int(''.join(i)))
print(len(set(int_list)))