import random
import heapq

chance_cards = [
	lambda p:  0,	 #advance to GO
	lambda p: 10,	 #go to JAIL
	lambda p: 11,	 #go to C1
	lambda p: 24,	 #go to E3
	lambda p: 39,	 #go to H2
	lambda p:  5,	 #go to R1
	lambda p: 28 if 12 <= p < 28 else 12,	#next U
	lambda p: p - 3	 #go back 3 sqs
	] + 2 * [lambda p: ((p+5)//10)*10 + 5	 #next R (2x)
		] + 6 * [int]	 #don't move (6x)

community_chest_cards = [
	lambda p: 0,	 #advance to GO
	lambda p: 10,	 #go to JAIL
	] + 14 * [int]	 #don't move (14x)

times_visited = [0 for _ in range(40)]

pos = 0
community_idx = chance_idx = 0
doubles_in_a_row = 0
random.shuffle(chance_cards)
random.shuffle(community_chest_cards)

def goto(n):
	global chance_idx
	global community_idx
	global pos

	pos = n % 40
	if pos == 30:
		pos = 10
	elif pos == 7 or pos == 22 or pos == 36:
		pos = chance_cards[chance_idx%16](pos)
		chance_idx += 1
	elif pos == 2 or pos == 17 or pos == 33:
		pos = community_chest_cards[community_idx%16](pos)
		community_idx += 1

	times_visited[pos%40] += 1

def move():
	global doubles_in_a_row
	x, y = random.randrange(1,5), random.randrange(1,5)
	if x == y:
		doubles_in_a_row += 1
	else:
		doubles_in_a_row = 0

	if doubles_in_a_row == 3:
		goto(10)
	else:
		goto(pos+x+y)

for i in range(1000000):
	move()

most_visited = heapq.nlargest(3, range(40), key=times_visited.__getitem__)

print(''.join(map(str, most_visited)))