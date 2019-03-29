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

value2=next(scan(tsvfile1))
value1=next(scan(tsvfile2))

temparray1 = []
temparray2 = []

nextval = []
kappa = 0
def mj(scan1,scan2,list1,list2):

    global temparray1
    global kappa
    global temparray2

    while True:
        if(len(list1)==1 and len(list2)==2):
            if(len(temparray1)==0 and kappa==0):
                val = next(scan1)
                temparray1.append(val)
            if(len(temparray1)==0 and len(temparray2)!=0):
                temparray1.append(temparray2[0])
                temparray2 = []

            val = next(scan1)
            while(temparray1[0][0]==val[0]):
                temparray1.append(val)
                val = next(scan1)
            else:
                temparray2.append(val)

            # print val
            # val = next(scan1)

        print temparray1
        kappa+=1
        if(kappa == 6):
            exit(0)
        temparray1=[]









if __name__ == "__main__":
    print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
