#!/usr/bin/env python
# coding: utf-8

# In[5]:


N=5
scare=[2,3,1,2,2]
count=0
group=0
scare.sort(reverse=True)
print(scare)

for member in scare:
    if group>=N:
        break
    group+=member
    count+=1
print(count)


# - 위의 방식은 내림차순으로 정렬함으로써 가장 많은 인원이 한 그룹에 들어가므로 최대 그룹수를 정하는 것에는 적합하지 않다.
# - 오름차순으로 정렬하여 문제를 풀어보자.

# - 최종 풀이과정
# 1. 공포도 하나씩 체크
# 2. 체크하면 인원수에 포함
# 3. 현재 공포도가 인원수랑 같으면 그룹 수 올림, 현재 그룹인원 수 0으로 조정
# 4. 안같으면 continue

# In[6]:


N=5
scare=[2,3,1,2,2]
count=0
group=0
scare.sort()
print(scare)

for member in scare:
    group+=1
    if group>=member:
        count+=1
        group=0    
print(count)


# ### 02 곱하기 혹은 더하기

# In[15]:


input='21984'
result=0
for num in input:
    if int(num)<=1 or result<=1:
        result+=int(num)
    else:
        result*=int(num)
print(result)


# - 최종 풀이과정
# 1. 확인한 숫자가 0이면, 1이면? 원래수에 더한다
# 2. 아니면? 원래수에 곱한다
# 3. 현재까지 result가 0이나 1이면 원래수에 더한다

# ### 03 문자열 뒤집기

# In[19]:


input='0001100'
group0=0
group1=0
currentG=-1
for item in input:
    if currentG==int(item):
        continue
    elif item=='0':
        group0+=1
        currentG=0
    elif item=='1':
        group1+=1
        currentG=1        
result=min(group0,group1)
print(result)


# - 최종 풀이과정
# 1. 0의 묶음을 세고, 1의 묶음을 센 뒤, 작은 묶음 개수가 답이다

# ### 04 만들 수 없는 금액

# In[2]:


from itertools import combinations
input=[3,2,1,1,9]
library=set()
for i in range(2,len(input)):
    library.update(set(combinations(input,i)))
for item in library:
    input.append(sum(item))
n=1
while True:
    if n in input:
        n+=1
    else:
        print(n)
        break


# ### 05 볼링공 고르기

# In[14]:


N=5
M=3
input=[1,5,4,3,2,4,5,2]
temp=0
result=0
for i in range(len(input)):
    result+=len(input)-(i+1)-input[i+1:].count(input[i])
print(result)


# - 최종풀이과정
# 1. i 번째 공 뒤에 i와 같은 무게를 가진 개수를 빼고 
# 2. 다 더한다

# ### 무지의 먹방 라이브

# In[16]:


def solution(food_times, k):
    answer = 0
    current=0
    time=0
    while True:
        if food_times[current] !=0: #먹을 수 있으면
            food_times[current]-=1 #먹고
            time+=1 #시간 올려
            if time==k:
                break
            nextfood(current)
        else: #먹을 게 없으면 다음걸로
            nextfood(current)
    return answer

def nextfood(current):
    current+=1
    if current==3:
        current=0


# In[57]:


import heapq
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    print(q)
    length=len(food_times)
    temp=0
    previous=0
    print(k)
    while k-length*(q[0][0]-previous)>=0:
        now=heapq.heappop(q)[0]
        temp=k
        k-=length*(now-previous)
        length-=1
        previous=now
        print(k)
    result=sorted(q,key=lambda x:x[1])
    return result[temp%length][1]


# In[58]:


solution([1,5,6,7],16)

