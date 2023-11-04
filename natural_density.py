# Natural Density Approximations for Power Sumsets
# given a power p, consider the set of \N^p = {n^p | n \in \N} and their sumsets
# e.g \N^2 = {0,1,4,9,16...}, 3*\N^2 = {a+b+c | a,b,c \in \N^2}
# and we want to consider for

# Considerations: Waring's problem says there's only have a finite number of
# vars for each number to check, and so we could even have one just saying
# "well if it isnt decreasing *that* quickly we're fine"


# Quick code notes: we know that because of the commutativity of addition,
# for entries (c1,c2,c3...) in N, that in N^p. all permutations of the cs are
# equivalent: the code structure should ignore what was covered
# okay lemme just do the problem and to the talking later

# lets start with 1 k and go up:
base = 1000

onem = list(range(base))
tenm = list(range(10*base))
hunm = list(range(100*base))

# add more fidelity around the millions
base = base * 1000
mills = [list(range(i*base)) for i in range(1,1000)]

base = base * 1000
bills = [list(range(i * base)) for i in range(1,100)]

dofs = list(range(1000))

print("starting with square sumsets: we know 2 should tend to 0, 3 uses legendre")
print("for 1-(1/8 + 1/32 + ... + 1/8*4^n) = 1-1/4(\sum 1/2^k) = 3/4 supposedly")

print("so lets run the tests:")
p = 2
dof = 2

for b in mills:
    sqs = [c**2 for c in b]
    S = set()
    for i in sqs:
        for j in sqs:
            set.add(i+j)
    print("total found" , len(set), "for", b)
    print("ratio:", len(set)/b)

for count in bills:
    sqs = [c**2 for c in count]
    S = set()
    for a in sqs:
        for b in sqs:
            for c in sqs:
                set.add(i+j+c)
    print("total found" , len(set), "for", count)
    print("ratio:", len(set)/count)
            
    




p = int(input("power?\n"))


