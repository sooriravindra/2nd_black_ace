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



count = [0]*52 #Used to store count for each position

for x in range(NUM_OF_SIM):
	pack=[0]*52
	i=0
	DECK = range(1,53)

	while(i<52):
		rand_pos = random.randint(0,51-i) # Give random number within the number of cards in deck
		card = DECK.pop(rand_pos)
		pack[i] = card
		i+=1

	pos = max(pack.index(BLACK_ACE1),pack.index(BLACK_ACE2)) # Choose index of 2nd black ace
	count[pos] = count[pos]+1
	if(x%STEPS == 0):			# For output purpose
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

final_prob=[0]*52

print "Successfully simulated ",x+1,"cases.\nThe probability according to theoretic case is compared against the simulated case at each position:\n"

print "\tPos\tSimulated\tTheoretic\tDifference"

for each in range(52):
	final_prob[each]=1.0*count[each]/NUM_OF_SIM
	print "\t",each,"\t"," %.5f"%final_prob[each], # Formatted output - pos,simulated probability
	theoretic = 2.0*each/52/51     #Theoretically at pos x probability is 2*x/(52*51)
	print "\t","%.5f"%theoretic,"\t %.5f"%abs(theoretic-final_prob[each]) # Formatted output theoretic probability
	

#print final_prob

