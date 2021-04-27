def maxi(m_list): # max 하자.
    temp = m_list[0]
    for (i,x) in enumerate(m_list):
        if temp <= m_list[i]:
            temp = m_list[i]
    return temp

def mini(m_list): # min  
    temp = m_list[0]
    for (i,x) in enumerate(m_list):
        if temp >= m_list[i]:
            temp = m_list[i]
    return temp

#-> SORT를 사용해보자
