def solution(dartResult):
    n=''
    score=[]
    for i in dartResult:
        if i in '0123456789':
            n+=i
        elif i=='S':
            n=int(n)
            score.append(n)
            n=''
        elif i=='D':
            n=int(n)**2
            score.append(n)
            n=''
        elif i=='T':
            n=int(n)**3
            score.append(n)
            n=''
        elif i=='*':
            if len(score)>1:
                score[-2]=score[-2]*2
                score[-1]=score[-1]*2
            else:
                score[-1]=score[-1]*2
        elif i=='#':
            score[-1]=score[-1]*-1
    return sum(score)
