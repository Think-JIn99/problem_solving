m = 0
texts = "ABC ABCDAB ABCDABCDABDE"
pat = "ABCDABD"
p = [0 for _ in range(len(texts))]

for i in range(1,len(pat)):
    while(m > 0 and pat[i] != pat[m]):
        #p는 접두사와 접미사가 일치하는 최대 길이를 저장하는 배열
        #일치하지 않을 경우 이미 알고있는 만큼은 점프한 뒤 비교한다.
        #p는 결국 이미 알고 있는 크기를 저장하는 배열이다.
        #i가 증가하고 m이 증가하므로 다음에 검사하는 
        #요소에선 이미 알고 있는 p[m-1]만큼은 검사를 건너 뛴다.
        m = p[m - 1]           

    if pat[m] == pat[i]:
        m += 1
        p[i] = m

j = 0
cnt = 0  
loc = ""                         
for i in range(len(texts)):
    while(j > 0 and texts[i] != pat[j]):
        j = p[j-1]
        # 다음글자를 비교할 때는 이미 아는 부분은 점프한다. 
    if(texts[i] == pat[j]):
        if(j== len(pat)-1):
            cnt += 1
            loc += str(i+1 - len(pat) + 1) + " " # 패턴이 처음으로 등장하는 위치
            j = p[j] # 전부 찾고 나면 j의 값을 다시금 초기화 해준다.
        else:
            j += 1
print(cnt)
print(loc)


