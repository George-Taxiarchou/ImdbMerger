import numpy as np
import csv
import itertools
import numpy

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
value3 =next(scan(tsvfile3))

def mj(scan1,scan2,list1,list2):
    temparray1 = []
    temparray2 = []
    temparray3 = []
    temparray4 = []
    kappa = 0
    keepo = 0
    count = 0
    mergearray1 = []
    mergearray2 = []
    finalarray=[]

    while True:
        # if(len(list1)==1 and len(list2)==2):

        while(count!=0):
            count-=1
            for x in itertools.product(mergearray1,mergearray2):
                if(len(list1)==1 and len(list2)==1):
                    yield [x[0][0],x[0][list1[0]],x[0][list1[1]]]
                elif(len(list1)==1 and len(list2)==2):
                    yield [x[0][0],x[0][list1[0]],x[1][list2[0]],x[1][list2[1]]]
                elif(len(list1)==2 and len(list2)==1):
                    yield [x[0][0],x[0][list1[0]],x[0][list1[1]],x[1][list2[0]]]
                elif(len(list1)==2 and len(list2)==2):
                    yield [x[0][0],x[0][list1[0]],x[0][list1[1]],x[1][list2[0]],x[1][list2[1]]]
                else:
                    print("Error , wrong number of parameters")
                    exit(0)

            break

        #---------FIRST FILE-------------#
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
        # print temparray1


        #--------SECOND FILE----------#
        if(len(temparray3)==0 and keepo==0):
            val2 = next(scan2)
            temparray3.append(val2)
        if(len(temparray3)==0 and len(temparray4)!=0):
            temparray3.append(temparray4[0])
            temparray4 = []

        val2 = next(scan2)
        while(temparray3[0][0]==val2[0]):
            temparray3.append(val2)
            val2 = next(scan2)
        else:
            temparray4.append(val2)
        # print temparray3


        #----------------------------------#

        for i in temparray1:
            for j in temparray3:
                count += 1

        #-----EMPTY ARRAYZ--------#
        kappa+=1
        keepo+=1

        mergearray1 = temparray1
        mergearray2 = temparray3

        # yield temparray1,temparray3

        temparray1=[]
        temparray3 =[]

        #-----EMPTY ARRAYZ--------#



if __name__ == "__main__":
    # mygen=mj(mj(scan(tsvfile1),scan(tsvfile2),[2],[1,2]),scan(tsvfile3),[2],[1,2])
    mygen = mj(scan(tsvfile1),scan(tsvfile3),[2],[1,2])
    print(next(mygen))
    print(next(mygen))
    print(next(mygen))
    print(next(mygen))
    print(next(mygen))
    print(next(mygen))
    # print(next(mygen))
    # print(next(mygen))
    # print(next(mygen))
    # print(next(mygen))
    # print(next(mygen))
