def solution(sizes):
    max_w = 0
    max_h = 0
    for size in sizes:
        #지갑에 들어가는지 체크
        w = max(size[0], size[1])
        h = min(size[0], size[1])
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    answer = max_w * max_h
        
    return answer