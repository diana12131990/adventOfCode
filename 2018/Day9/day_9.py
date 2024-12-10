from collections import deque, defaultdict

num_players = 411
last_marble = 7117000

scores = defaultdict(int)
circle = deque([0])
for marble in range(1, last_marble + 1):
    if marble % 23 == 0:
        circle.rotate(7)
        scores[marble % num_players] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)
        
print(max(scores.values()))