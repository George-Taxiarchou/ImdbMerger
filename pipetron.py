import numpy as np
import csv

tsvfile1 = open("title.basics.tsv","r")
tsvfile2 = open("title.principals.tsv","r")
tsvfile3 = open("title.ratings.tsv","r")
mergedtsvfile = open("title.pipe.tsv","w")
mergedoutput = csv.writer(mergedtsvfile,delimiter = '\t')


def scan(file):
    while True:
        field = next(file).split("\t")
        field = [f.strip() for f in field]
        yield field

value1=next(scan(tsvfile1))
value2=next(scan(tsvfile2))

temparray1 = []
temparray2 = []
mergearray = []

def mj(scan1,scan2,list1,list2):
    # print "kek"
    global value1
    global value2
    global mergearray
    global temparray1,temparray2

    value2 = next(scan2)
    temparray2.append(value2)
    while True:
        if(len(list1)==1 and len(list2)==2):
            # print "lel"
            if(value1[0]==value2[0]):
                yield (value1[0]+"\t"+value1[list1[0]]+"\t"+value2[list2[0]]+"\t"+value2[list2[1]])
                # value2 = next(scan2)
            else:
                value1 = next(scan1)





if __name__ == "__main__":

    print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
