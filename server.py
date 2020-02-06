from app import app


# Run on Remote Server with the following cmd:
# nohup python3 server.py > debug.log 2>&1

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
