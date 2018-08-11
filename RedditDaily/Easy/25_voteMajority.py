voteBreakdown =[[90, "Paul"],
                [30, "David"],
                [30, "Robert"]
                ]

voteSum = 0
for pair in voteBreakdown:
    voteSum += pair[0] 

mostVotes = max(voteBreakdown)

if mostVotes[0] > (voteSum/2):
    print(mostVotes[1] + " Won")
else:
    print("No single candidate recieved a majority")
