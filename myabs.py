def myabs(m_list): # myabs는 abs를 직접 구현 해보는 것. 
    temp = m_list[0]
    for (i,x) in enumerate(m_list): # 파이썬 for문과 리스트에 대해 잘 이해하기!.
        temp = m_list[i] # _list[i]
        if temp > 0: 
            print(m_list[i] ,"abs =>", temp)
        elif temp < 0:
            temp = temp * -1
            print(m_list[i] ,"abs =>", temp)
