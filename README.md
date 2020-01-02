[![codecov](https://codecov.io/gh/Kok-Kip/backend/branch/master/graph/badge.svg)](https://codecov.io/gh/Kok-Kip/backend)
# Mini Search Engine Backend

## Intro

This is the backend project of Mini Search Engine

## Environment

+ Python 3.6

## How to run

1. clone this project from Github, and enter the work directory.

   ```bash
   git clone https://github.com/Kok-Kip/backend.git
   cd backend
   ```
   
2. If this is the first time you run this project on your machine, please create a MySQL database named `search_engine`, and run a script to create tables.

   ```bash
   python Preprocess.py
   ```

   By running this command, we will initialize a dictionary on you local database, which can provide query information when a searching is required!

3. run this server by:

   ```bash
   python server.py
   ```

   

---

## Documents

1. [Mini Search Engine Design Doc](https://github.com/leungyukshing/SearchEngine/blob/master/backend/Mini%20Search%20Engine%20Design%20Doc.md)
