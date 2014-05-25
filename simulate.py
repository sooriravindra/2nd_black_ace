import random


BLACK_ACE1 = random.randint(1,52)
BLACK_ACE2 = random.randint(1,52)

DECK = range(1,53)

while(BLACK_ACE1 == BLACK_ACE2):
	BLACK_ACE2 = random.randint(1,52)


#-----------------------------------------------------------------------------------

print "Black aces are ", BLACK_ACE1 , BLACK_ACE2



prob = [0]*52

for x in range(99999):
	pack=[0]*52
	i=0
	DECK = range(1,53)

	while(i<52):
		rand_pos = random.randint(0,51-i) # Give random number within the number of cards in deck
		card = DECK.pop(rand_pos)
		pack[i] = card
		i+=1

	pos = max(pack.index(BLACK_ACE1),pack.index(BLACK_ACE2))
	prob[pos] = prob[pos]+1
	if(x%5000 == 0):
		print "."


print prob

sum =0
for each in prob:
	sum+=each

final_prob=[0]*52

print "\tPos\tProbability"

for each in range(52):
	final_prob[each]=1.0*prob[each]/sum
	print "\t",each,"\t","%.5f"%final_prob[each]

#print final_prob

