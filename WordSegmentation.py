import jieba
import re
import chardet
from database import db, create_app
from database.document import *
from database.word import *
from database.wordDocRef import *
from database.models import *

def segmentation():
  # num = 0
  for line in open('paths.txt'):
    path = line
    # num += 1
    line = line[17: -5]
    # print(line)
    line = 'directory/' + line + 'txt'
    path = line
    fb = open(path, 'rb')
    data = fb.read()
    encoding = chardet.detect(data)['encoding']

    if encoding == 'UTF-16':
      data = data.decode('UTF-16')
      data = data.encode('utf-8')
    data = data.decode('utf-8')

    # get stopwords dict
    stopwords = {}
    fstop = open('stopwords_cn.txt', 'r', encoding='utf-8', errors='ignore')
    for w in fstop:
      stopwords[w.strip()] = w.strip()
    fstop.close()
    stopwords[' '] = ' '

    # remove punctuations
    data = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", " ", data)

    # divide text into words
    word = jieba.cut_for_search(data)
    seglist = list(word)

    # remove stopwords
    segListSanitized = []
    for word in seglist:
      if word not in stopwords:
        segListSanitized.append(word)
    print(segListSanitized)

    # conn = sqlite3.connect('index.db3')
    # c = conn.cursor()
    # construct doc table
    # c.execute('insert into doc values(?,?)', (num, path))

    print(path)
    # create document record
    document_id = create_document(path, len(segListSanitized))

    # Word Table
    for word in segListSanitized:
      # c.execute('select list from word where term=?', (word,))
      # result = c.fetchall()
      is_exist, word_id = isWordExisted(word)
      if not is_exist:
        # add record in Word
        word_id = create_word(word)
        
      # add record in WordDocRef
      is_exist, ref = isWordDocRefExisted(word_id, document_id)
      if not is_exist:
        create_wordDocRef(word_id, document_id)
      else:
        update_wordDocRef(word_id, document_id, ref.frequency+1)
      ''' 
      if len(result) == 0:
        doclist = str(num)
        c.execute('insert into word values(?,?)', (word, doclist))

      else:
        doclist = result[0][0]
        doclist += ' ' + str(num)
        c.execute('update word set list=? where term=?', (doclist, word))
      '''
