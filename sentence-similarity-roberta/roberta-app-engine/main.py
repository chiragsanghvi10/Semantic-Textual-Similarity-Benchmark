#!/usr/bin/env python
# coding: utf-8

from flask import Flask
from flask import request
from flask import jsonify
import json
import os
import time
from fairseq.models.roberta import RobertaModel
from google.cloud import storage
app = Flask(__name__)
import cloudstorage
from google.cloud import storage
import tarfile
import wget
print("DONE IMPORTING ALL LIBRARIES ###################")

CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']
print("CLOUD STORAGE BUCKET IS ###################", CLOUD_STORAGE_BUCKET)

o = os.getcwd()
print("O #################################################",o)

url1 = 'https://storage.googleapis.com/salesken-models/ROBERTa-STS-B/checkpoint_best.pt'
filename1 = wget.download(url1)

url2 = 'https://storage.googleapis.com/salesken-models/ROBERTa-STS-B/STS-B-bin.tar.gz'
filename2 = wget.download(url2)
with tarfile.open(filename2) as f:
    f.extractall('.')

l = os.listdir()
print("ALL FILES in this dir ##########", l)

print("STARTING ROBERTA ###################")
roberta = RobertaModel.from_pretrained(o,
    checkpoint_file='checkpoint_best.pt',
    data_name_or_path= o+'/STS-B-bin'
)
print("DONE ##############")

@app.route("/sentence_similarity_roberta",methods=["POST","GET"])
def sentence_similarity_roberta():
    r = []
    result = []
    
    list1=request.form.getlist('sentence1')
    list2=request.form.getlist('sentence2')
    print("LIST1 ###############", list1)
    print("LIST2 ###############", list2)
    list1 = list1[0].replace("\"",'').replace("[",'').replace("]",'')
    s1 = list1.split(",")
    list2 = list2[0].replace("\"",'').replace("[",'').replace("]",'')
    s2 = list2.split(",")
    print("S1 ###############", s1)
    print("S2 ###############", s2)
    for i in s1:
        for j in s2:
            print("i ###############", i)
            print("j ###############", j)
            tokens = roberta.encode(i, j)
            features = roberta.extract_features(tokens)
            predictions = roberta.model.classification_heads['sentence_classification_head'](features)
            print('PREDCITIONS ################', predictions)
            r.append({"sentence1":i, 'sentence2':j, 'roberta_score':str(predictions.item())})
            print("R ###################", r)
        result.append(r)
        print("RESULT ##################", result)
        r = []
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
