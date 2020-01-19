[![codecov](https://codecov.io/gh/Kok-Kip/backend/branch/master/graph/badge.svg)](https://codecov.io/gh/Kok-Kip/backend)

# Mini Search Engine Backend

## Intro

This is the backend project of Mini Search Engine. We are so sorry about not deploying this service on remote server now, we promise this is our priority in the next few weeks.

## Environment

- Python 3.6

## How to run

1. clone this project from Github, and enter the work directory.

   ```bash
   git clone https://github.com/Kok-Kip/backend.git
   cd backend
   ```

2. Download data and unzip it. Rename this folder as `data` , and move it in project. 

   Google Drive: [Here](https://drive.google.com/open?id=1Y72TnaaSDWhSPBSQmMD4TjNzgO3JNf-f)

   BaiduYun: [Here](https://pan.baidu.com/s/1UcqWrrHqSU7azxWdeviJjg)

3. Install all dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. If this is the first time you run this project on your machine, **please((:

   - create a MySQL database named `search_engine`. 
   - Edit `config.py` in `app/database/`, use your`USERNAME` and `PASSWORD` in local database.
   - And run a script to create tables in your database and parse txt files.

   ```bash
   python Preprocess.py
   ```

   By running this command, we will initialize a dictionary on you local database, which can provide query information when searching.

5. run this server by:

   ```bash
   python server.py
   ```

------

## Documents

1. [Mini Search Engine Design Doc](https://github.com/Kok-Kip/backend/blob/master/Mini%20Search%20Engine%20Design%20Doc.md)

