from collections import Counter

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
scores = [0] * N 

for _ in range(M):
    max_value = -1
    round_winners = []

    for player_idx in range(N):
        if arr[player_idx]:  
            best_card = max(arr[player_idx])
            if best_card > max_value:
                max_value = best_card
                round_winners = [player_idx]
            elif best_card == max_value:
                round_winners.append(player_idx)
            arr[player_idx].remove(best_card)  


    for winner in round_winners:
        scores[winner] += 1


max_score = max(scores)
winners = [i + 1 for i, score in enumerate(scores) if score == max_score]
print(" ".join(map(str, winners)))
