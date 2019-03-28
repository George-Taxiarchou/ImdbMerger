import numpy as np
import csv

tsvfile1 = open("title.basics.tsv","r")
tsvfile2 = open("title.akas.tsv","r")
mergedtsvfile = open("title.merged.tsv","w")
mergedoutput = csv.writer(mergedtsvfile,delimiter = '\t')

def yield_tsv(file):
    field = next(file).split("\t")
    field = [f.strip() for f in field]
    yield field

value = []
next(yield_tsv(tsvfile1))
next(yield_tsv(tsvfile2))

temparray = []
def mergeByID(file,ID):
    global temparray
    mergefilearray=[]
    pointer = ''
    value = next(yield_tsv(file))
    while value[0] == ID:
        temparray.append(value)
        value = next(yield_tsv(file))
    else:
        flag = 0
        for i in range(len(temparray)) :
            for j in range(len(temparray)):
                if(i!=j and temparray[i][2] == temparray[j][2] and flag==0):
                    flag = 1
                    temparray[i][3]+=","+temparray[j][3]
                if(i!=j and temparray[i][2] == temparray[j][2] and flag==1):
                    pointer = i

        for i in range(len(temparray)):
            if(i==pointer):
                continue
            else:
                mergefilearray.append(temparray[i][2]+"("+temparray[i][3]+")")
                print(temparray[i][2]+"("+temparray[i][3]+")")

        mergedoutput.writerow(mergefilearray)
        temparray = []
        temparray.append(value)



if __name__ == "__main__":
    with open('title.basics.tsv', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1].split("\t")
    f.close()

    outputarrayformat = ["titleId","primaryTitle","title(regions)"]
    mergedoutput.writerow(outputarrayformat)


    while value!=last_line:
            value = next(yield_tsv(tsvfile1))
            print("\t"+value[0])
            print(value[2]+"\t")
            mergedtsvfile.write(value[0]+"\t"+value[2]+"\t")
            mergeByID(tsvfile2,value[0])
            print("-----------------------------")

    tsvfile1.close()
    tsvfile2.close()
    mergedtsvfile.close()
