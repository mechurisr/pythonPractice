
#완주하지 못한 선수
participant = ["leo", "kiki", "eden"], ["marina", "josipa", "nikola", "vinko", "filipa"], ["mislav", "stanko", "mislav", "ana"]
completion = ["eden", "kiki"], ["josipa", "filipa", "marina", "nikola"], ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participant = ["leo", "kiki", "eden"], ["marina", "josipa", "nikola", "vinko", "filipa"], ["mislav", "stanko",
                                                                                               "mislav", "ana"]
    completion = ["eden", "kiki"], ["josipa", "filipa", "marina", "nikola"], ["stanko", "ana", "mislav"]
    returned = []
    for i in participant:
        if i not in completion:
            returned.append(i)
    answer = returned[0]
    return answer