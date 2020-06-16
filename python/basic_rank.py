import redis
import string
import random

r = redis.Redis(host= '127.0.0.1', port= '6379')

dataList = {}
scoreList = {}
table = 'hyun:20200616'

for i in range(20):
    dataList[string.ascii_lowercase[i:i+1]] = random.randint(1000, 10000)


dataList['me'] = random.randint(1000, 10000)

r.zadd(table, dataList)

scoreList = r.zrevrange(table, 0, -1, withscores=True)

rank = 1
for score in scoreList:
    print ('RANK {:2d} {:5s} {:5d}'.format(rank, score[0], int(score[1])))
    rank += 1

