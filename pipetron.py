import numpy as np
import csv
import itertools
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
temparray3 = []
temparray4 = []
kappa = 0
keepo = 0
count = 0
mergearray1 = []
mergearray2 = []
finalarray=[]
def mj(scan1,scan2,list1,list2):

    global temparray1
    global kappa
    global temparray2
    global temparray3
    global temparray4
    global keepo
    global count
    global mergearray1
    global mergearray2
    global finalarray

    while True:
        if(len(list1)==1 and len(list2)==2):

            while(count!=0):
                count-=1
                for x in itertools.product(mergearray1,mergearray2):
                    # if(count != len(x)):
                    #     break
                    yield x
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


# def Tron(generator):
#     for i in generator:






if __name__ == "__main__":
    mygen = mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])
    print(next(mygen))
    print(next(mygen))
    print(next(mygen))
    print(next(mygen))
    print(next(mygen))
    print(next(mygen))

    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    # print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
