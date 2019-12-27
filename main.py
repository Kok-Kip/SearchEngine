import sqlite3
import jieba
import math


conn = sqlite3.connect('index.db3')
c = conn.cursor()
c.execute('select count(*) from doc')
N = 1 + c.fetchall()[0][0]
query=input('Input Key Word: ')
seggen = jieba.cut_for_search(query)
score={}

for word in seggen:
  print('Key Word: ', word)

  tf = {}
  c.execute('select list from word where term=?', (word,))
  result = c.fetchall()
  if len(result) > 0:
    doclist = result[0][0]
    doclist = doclist.split(' ')
    doclist = [int(x) for x in doclist] # convert from string to int
    n = len(set(doclist))
    idf = math.log(N / n)
    print('idf: ', idf)
    print()
    for num in doclist:
      if num in tf:
        tf[num] = tf[num] + 1
      else:
        tf[num] = 1

    # compute score
    for num in tf:
      if num in score:
        score[num] = score[num] + tf[num] * idf
      else:
        score[num] = tf[num] * idf

# sort by score
sortedlist = sorted(score.items(), key=lambda d: d[1], reverse=True)

cnt = 0
print('------Search Result------')
for num, docscore in sortedlist:
  cnt += 1
  c.execute('select link from doc where id=?', (num,))
  url = c.fetchall()[0][0]
  print()
  print('Rank: ', cnt)
  print('File path: ', url, 'Match Degree: ', docscore)

  if cnt > 20:
    break

if cnt==0:
  print('No Match!')

        