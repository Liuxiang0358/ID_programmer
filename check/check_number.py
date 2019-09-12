t = []
w = []
for i in range(0,18):
    t1 = i + 1
    t.append(t1)
    w1 = (2 ** (t1-1)) % 11
    w.append(w1)
#队列w要做一个反序
w = w[::-1]  

# 根据前17位的余数，计算第18位校验位的值
def for_check(n):
    # t = 0
    for i in range(0,12):
        if (n + i) % 11 == 1:
            t = i % 11
    if t == 10:
        t = 'X'
    return t
    
# 根据身份证的前17位，求和取余，返回余数
def for_mod(id):
    sum = 0
    for i in range(0,17):
        sum += int(id[i]) * int(w[i])
        # print(int(id[i]),int(w[i]),sum)
    sum = sum % 11
    # print(sum)
    return sum

# 验证身份证有效性
def check_true(id):
    # print(for_check(for_mod(id[:-1])))
    if id[-1] == 'X':
        if for_check(for_mod(id[:-1])) == 'X':
            return True
        else:
            return False
    else:
        if for_check(for_mod(id[:-1])) == int(id[-1]):
            return True
        else:
           return False# -*- coding: utf-8 -*-

def number(number):
  return(check_true(number))