word='man'
word=word.upper()
word_show="_"*len(word)
try_num=0
ok_list=[]
no_list=[]
while True:
    ans=input().upper()
    result = word.find(ans)
    if result == -1 :
        print('오답')
        try_num += 1
        no_list.append(ans)
    else:
        print('정답')
        ok_list.append(ans)
        for i in range(len(word)):
            if word[i] == ans:
                word_show = word_show[:i] + ans + word_show[i+1]
        print(word_show)
    if try_num == 7 : break

    if word_show.find(" ")==-1: break
    
