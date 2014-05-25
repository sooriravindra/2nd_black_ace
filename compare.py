import random
import sys

BLACK_ACE1 = random.randint(1,52)
BLACK_ACE2 = random.randint(1,52)
NUM_OF_SIM = 100000
STEPS = NUM_OF_SIM/20
DECK = range(1,53)

while(BLACK_ACE1 == BLACK_ACE2):
	BLACK_ACE2 = random.randint(1,52)


#-----------------------------------------------------------------------------------

print "Black aces are ", BLACK_ACE1 , BLACK_ACE2



prob = [0]*52

for x in range(NUM_OF_SIM):
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
	if(x%STEPS == 0):
		if(x%(STEPS*4)==0):
			print "\b\b\b\b\b\b\b\b\b---",
		elif(x%(STEPS*4)==STEPS):
			print "\b\b\b\b\b\b\b\b\b \\ ",
		elif(x%(STEPS*4)==2*STEPS):
			print "\b\b\b\b\b\b\b\b\b | ",
		else:
			print "\b\b\b\b\b\b\b\b\b / ",
		print "%3.0f"%(100*x/NUM_OF_SIM)+"%",
		sys.stdout.flush()
sum =0
for each in prob:
	sum+=each

final_prob=[0]*52

print "Successfully simulated ",x+1,"cases.\nThe probability according to theoretic case is compared against the simulated case at each position:\n"

print "\tPos\tSimulated\tTheoretic\tDifference"

for each in range(52):
	final_prob[each]=1.0*prob[each]/sum
	print "\t",each,"\t"," %.5f"%final_prob[each],
	theoretic = 2.0*each/52/51
	print "\t","%.5f"%theoretic,"\t %.5f"%abs(theoretic-final_prob[each])
	

#print final_prob

