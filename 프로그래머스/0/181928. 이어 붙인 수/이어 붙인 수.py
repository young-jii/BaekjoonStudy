def solution(num_list):
    answer = 0
    odd = []
    even = []
    for i in num_list:
        if i % 2 == 0:
            even.append(str(i))
        else:
            odd.append(str(i))
    answer = int(''.join(odd)) + int(''.join(even))
    return answer