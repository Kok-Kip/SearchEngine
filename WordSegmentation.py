import jieba
import re
import chardet
from app.database import db
from app.database.document import *
from app.database.word import *
from app.database.wordDocRef import *
from app.database.models import *


def segmentation():
    for line in open('paths.txt'):
        line = line[22: -5]
        # print(line)
        line = 'data/directory/' + line + 'txt'
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
        fstop = open('data/stopwords_cn.txt', 'r', encoding='utf-8', errors='ignore')
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
            is_exist, word_id = is_word_existed(word)
            if not is_exist:
                # add record in Word
                word_id = create_word(word)
        
            # add record in WordDocRef
            is_exist, ref = is_word_doc_ref_existed(word_id, document_id)
            if not is_exist:
                create_word_doc_ref(word_id, document_id)
            else:
                update_word_doc_ref(word_id, document_id, ref.frequency+1)
        ''' 
        if len(result) == 0:
            doclist = str(num)
            c.execute('insert into word values(?,?)', (word, doclist))

        else:
            doclist = result[0][0]
            doclist += ' ' + str(num)
            c.execute('update word set list=? where term=?', (doclist, word))
        '''
