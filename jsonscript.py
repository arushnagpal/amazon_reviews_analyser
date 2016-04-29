#!/usr/bin/python
import numpy
import json 


'''
This will create a file op.txt that will have the summary part of all JSON reviews extracted into a file

'''

out=open('op.txt','w')
sentence=[]
json1_file = open('data.json')
json1_str = json1_file.read().split('\n')
#json1_str = json1_str.split('`')
for c in json1_str:
	print c
	json1_data = json.loads(c)
	sentence.append(json1_data["summary"])
	out.write(json1_data["summary"]+"\n")
print sentence
json1_file.close()

out.close()