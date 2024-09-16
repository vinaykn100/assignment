### Prerequisites
1. Install Python, node.js
2. ``` npm i -g serverless ```
3. cd to monty-assignment directory. ``` npm install ``` (to install dependencies)
4. Install virtual env ``` pip install virtualenv ```


## Commands
    1. virtualenv monty-assignment
    2. source monty-assignment/bin/activate  (to activate)
    3. pip install -r requirements.txt
    4. serverless s3 start  (start aws s3 service locally, possibly in a new terminal)
    5. export PYTHONPATH=$PWD && python app/main.py  (to start the uvicorn service)
    6. deactivate (come out of virtualenv)

## Testing

 1. Open ``` http://localhost:8000/docs ``` in browser and test


### NOTE: 
    I was facing an issue with my docker daemon in my workstation, so had to resort to serverless framework. Will leverage serverless with localstack framework once it is fixed. Also serverless dynamodb local plugin didnt seem to be compatible.