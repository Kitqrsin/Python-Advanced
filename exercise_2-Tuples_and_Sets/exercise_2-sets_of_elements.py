n, m = input().split()
n_set = set()
m_set = set()

for _ in range(int(n)):
    n_set.add(int(input()))

for _ in range(int(m)):
    m_set.add(int(input()))
subtotal = n_set.intersection(m_set)
print(*subtotal, sep='\n')
