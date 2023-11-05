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
base = 100

# add more fidelity around the millions
mills = [list(range((i-1)*base, i*base)) for i in range(1,1000)]

#billions will break ram and other specs for sure dont do it
# unless you got superpc or smth
#base = base * 1000
# bills = [list(range(i * base)) for i in range(1,100)]

print("starting with square sumsets: we know 2 should tend to 0, 3 uses legendre")
print("for 1-(1/8 + 1/32 + ... + 1/8*4^n) = 1-1/4(sum 1/2^k) = 3/4 supposedly")

print("so lets run the tests:")
p = 2
dof = 2

# Try 2: Dynamic Programming Approach:
# don't want to waste compute resources.
# idea: only add to the set, don't just redefine everything
# makes life so much easier for the computer at least

# all the squares go in sqs
sqs = []
# sum of square set in S
S = set()

for b in range(len(mills)):
    sqs.extend([c**2 for c in mills[b]])
    for i in range(len(sqs)):
        for j in range(b*base, (b+1)*base):
            S.add(sqs[i]+sqs[j])
    print("total found" , len(S), "for", b*base)
    print("real ratio:", len(S)/ (((b+1)*base)**2) )

# cubes, if i get there

'''
for count in mills:
    sqs = [c**3 for c in count]
    S = set()
    for a in sqs:
        for b in sqs:
            for c in sqs:
                S.add(i+j+c)
    print("total found", len(S), "for", len(count))
    print("ratio:", len(S)/len(count))
'''
