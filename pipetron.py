import csv
import itertools

def scan(file):
    while True:
        field = next(file).split("\t")
        field = [f.strip() for f in field]
        yield field

def mj(scan1,scan2,list1,list2):
    temparray1 = [] #holds the same 'tconst' items of first file
    temparray2 = [] #temporarily holds the next 'tconst' item to put in temparray1
    temparray3 = [] #holds the same 'tconst' items of second file
    temparray4 = [] #temporarily holds the next 'tconst' item to put in temparray3
    emptyflag1 = 0
    emptyflag2 = 0
    count = 0 #counter of combinations between first and second items of the same 'tconst'
    mergearray1 = []
    mergearray2 = []

    while True:
        #--------------YIELD RESULTS-------------------#
        while(count!=0):
            count-=1
            for x in itertools.product(mergearray1,mergearray2):
                if(len(list1)==1 and len(list2)==1):
                    yield [x[0][0],x[0][list1[0]],x[1][list1[0]]]
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
        #--------------YIELD RESULTS-------------------#

        #---------PARSE FIRST FILE-------------#
        if(len(temparray1)==0 and emptyflag1==0):
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

        #--------PARSE SECOND FILE----------#
        if(len(temparray3)==0 and emptyflag2==0):
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
        #----------------------------------#

        for i in temparray1:
            for j in temparray3:
                count += 1
        #-----EMPTY ARRAYS--------#
        emptyflag1+=1
        emptyflag2+=1
#hold the result to yield it before emptying temparrays
        mergearray1 = temparray1
        mergearray2 = temparray3
#----------------------------------------------------#
        temparray1=[]
        temparray3 =[]
#----------------------------------------------------#

def main():
    tsvfile1 = open("title.basics.tsv","r")
    tsvfile2 = open("title.principals.tsv","r")
    tsvfile3 = open("title.ratings.tsv","r")
    FIRSTROWPRINT = 0 #flag for first print
#----------------------------------------------------------------#
    # a)
    mygen = mj(scan(tsvfile1),scan(tsvfile3),[2],[1,2])

    # b)
    # mygen = mj(scan(tsvfile1),scan(tsvfile2),[2],[2])

    # c)
    # mygen = mj(mj(scan(tsvfile1),scan(tsvfile2),[2],[2]),scan(tsvfile3),[1,2],[1])
#----------------------------------------------------------------#
    if(FIRSTROWPRINT==0):
        print("------------------------------------------------------------")
        print(next(mygen))  #prints first merged row names 'tconst' etc.
        print("------------------------------------------------------------")
        FIRSTROWPRINT = 1

    while True:
    # for i in range(0,10):
        print(next(mygen))

    tsvfile1.close()
    tsvfile2.close()
    tsvfile3.close()
if __name__ == "__main__":
    main()
