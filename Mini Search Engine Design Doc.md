# Mini Search Engine Design

**Author:** Yucheng Liang

**Last Updated: **2019-12-18

I'm going to implement a mini  search engine based on python. Let's see what can I do.

---

## Tech Stack

+ Database: [sqlite3](<https://docs.python.org/3/library/sqlite3.html>)
+ Word Segmentation: [jieba](<https://pypi.org/project/jieba/>)

---

## File Structure

`DATA-UNICODE`: the directory to store source files, which are obtained from website.

`directory`: the directory to store all plain text files. We preprocess the source files and then we do word segmentation on these files.

`index.db3`: database files

`main.py`: Main function to run a search program

`paths.txt`: A txt file storing all the documents paths.

`Preprocess.py`: Pre-processing the source files.

`WordSegmentation.py`: Do segmentations and construct a dictionary, later for search use.

---

## Usage

Environment: Window10, Python3+, jieba

1. Make sure you have installed all the dependencies stated above.

2. Clone from this repository

   ```bash
   // Use http
   git clone https://github.com/leungyukshing/SearchEngine.git
   
   // Use ssh
   git clone git@github.com:leungyukshing/SearchEngine.git
   ```

3. Run `main.py`,  input a key word and you get the search results.

   ```bash
   python main.py
   ```

---

## Implementation

This Mini-Search-Engine is constructed based on the Vector-Space Model, behind which are is two tables in a database. We store the documents in TABLE `Doc`, and we store words in TABLE `Word`. By searching the `Word` table, we can get a list of document numbers, by which we can find the corresponding documents in `Doc` table. This is the basis of this project.

Additionally, in order to evaluate the performance of this engine, I use two metrics, TF and IDF.

TF is the frequency of a given word. The larger the TF is, the stronger ability of the given word has to represent a document. So we expect a large TF.

On the contrary, IDF refers to the frequency of documents for a given word. The larger the IDF is, the weaker is a word to distinguish one document from another. So we expect a smaller IDF.

TF * IDF framework allows us to evaluate such an engine efficiently. For a given word, we define its search score: score = TF * IDF

---

## Database Design

We have two tables in DB.

### Table Document

| Attr | id   | link    | length |
| ---- | ---- | ------- | ------ |
| Type | int  | varchar | int    |

We build a connection between document and its link. Link could be file path or website link.

### Table Word

| Attr | id   | term    |
| ---- | ---- | ------- |
| Type | int  | varchar |

We may save the word like a dictionary. Save Embeddings?

### Table word_doc_ref

| Attr | id   | word_id     | document_id | frequency |
| ---- | ---- | ----------- | ----------- | --------- |
| Type | int  | varchar(25) | int         | int       |

We save the relationship between words and documents.

---

## Segmentation

This is an offline step. We will segment all documents to construct a dictionary in local database. Here we need to remove stopwords and punctuations.

---

## Reference

1. [text_factory Usage](https://www.cnblogs.com/lightwind/p/4499193.html)
2. [Flask--Postman Debug for request and response](https://www.cnblogs.com/chaojiyingxiong/p/10283877.html)
3. [BM25-python](https://www.jianshu.com/p/1e498888f505)
4. [Tencent AI lab Embedding Dataset](https://ai.tencent.com/ailab/nlp/embedding.html)
5. [Word Embeddings in Python with Spacy and Gensim](https://www.shanelynn.ie/word-embeddings-in-python-with-spacy-and-gensim/)
6. [Flask SQLAlchemy](https://www.cnblogs.com/fu-yong/p/9183951.html)
7. [Gensim Usage](https://www.jianshu.com/p/bba1bf9518dc)

