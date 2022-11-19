from collections import *
def ways(durations):
    hashmap = Counter(durations)
    answer = 0
    # 60 60 60 10 50
    for song in durations:
        hashmap[song] -= 1
        answer += hashmap[song]
        song = 60 - song 
        while song + 60 <= max(durations):
            answer += hashmap[song]
            song += 60 
    return answer 
    