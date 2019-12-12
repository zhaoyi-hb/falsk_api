from flask import Flask,Response,json
from pymongo import MongoClient
app=Flask(__name__)

class MongoConn:
    def __init__(self):
        self.url=''
        self.client=self.get_client()

    def get_client(self):
        return MongoClient(self.url)

@app.route('/')
def get_one():
    mongoconn = MongoConn()
    db = mongoconn.client['wikipedia']
    # col = db['wikipedia']
    # x=col.find_one({},{"_id":0})
    col1=db['Evidence-Based_Complementary_and_Alternative_Medicine']
    y=col1.find({},{'_id':0}).sort('ts',-1).limit(1)
    for i in y:
        dd=i
    return Response(json.dumps(dd,ensure_ascii=False))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=6666)




