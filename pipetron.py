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
next1 = []
next2 = []
kappa=0
def mj(scan1,scan2,list1,list2):
    global kappa
    global value1
    global value2
    global temparray1,temparray2

    while 1:

        if(len(list1)==1 and len(list2)==2):
            if(len(temparray1)==0):
                val = next(scan1)
                temparray1.append(val)
            val = next(scan1)
            while(temparray1[0][0]==val[0]):
                temparray1.append(val)
                val = next(scan1)

            # if(len(temparray2)==0):
            #     val2 = next(scan2)
            #     temparray2.append(val2)
            # val2 = next(scan2)
            # while(temparray2[0][0]==val2[0]):
            #     temparray2.append(val2)
            #     val2 = next(scan2)
            # else:
            #     if(temparray1[0][0]==temparray2[0][0]):
            #         print temparray1
            #         print "\n"
            #         print temparray2
            #         temparray2 = []
            #         temparray2.append(val2)
            #
            # temparray1 = []
            # temparray1.append(val)
            # exit(0)
            yield temparray1
            # temparray1 = []







if __name__ == "__main__":
    # mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])
    print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
    print(next(mj(scan(tsvfile2),scan(tsvfile1),[2],[1,2])))
