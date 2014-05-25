import random

def shuffle(pk,card,index):
	if(pk.count(card)<1):
		pk[index]=card
	else:
		card=(card)%52+1
		shuffle(pk,card,index)

BLACK_ACE1 = random.randint(1,52)
BLACK_ACE2 = random.randint(1,52)

#print "Black aces are ", BLACK_ACE1 , BLACK_ACE2

while(BLACK_ACE1 == BLACK_ACE2):
	BLACK_ACE2 = random.randint(1,52)

print "Black aces are ", BLACK_ACE1 , BLACK_ACE2



prob = [0]*52

for x in range(999999):
	pack=[0]*52
	i=0
	while(i<52):
		val = random.randint(0,51)
		shuffle(pack,val,i)
		i+=1

	pos = max(pack.index(BLACK_ACE1),pack.index(BLACK_ACE2))
	prob[pos] = prob[pos]+1
	if(x%5000 == 0):
		print prob


print prob

sum =0
for each in prob:
	sum+=each

final_prob=[0]*52

print "Tan-Tana"
for each in range(52):
	final_prob[each]=prob[each]/sum


print final_prob

