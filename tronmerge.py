import csv

mergedtsvfile = open("title.merged.tsv","w")
mergedoutput = csv.writer(mergedtsvfile,delimiter = '\t')

def yield_tsv(file):
    field = next(file).split("\t")
    field = [f.strip() for f in field]
    yield field

def mergeByID(tsvfile1value,file,ID):
    temparray = []
    mergefilearray=[]
    pointer = ''
    tsvfile1value = next(yield_tsv(file))
    while tsvfile1value[0] == ID:
        temparray.append(tsvfile1value)
        tsvfile1value = next(yield_tsv(file))
    else:
        flag = 0
        for i in range(len(temparray)) :
            for j in range(len(temparray)):
                if(i!=j and temparray[i][2] == temparray[j][2] and flag==0):
                    flag = 1
                    temparray[i][3]+=","+temparray[j][3]
                if(i!=j and temparray[i][2] == temparray[j][2] and flag==1):
                    pointer = i
                    #pointer to not print joined items second time in array

        for i in range(len(temparray)):
            if(i==pointer):
                continue
            else:
                mergefilearray.append(temparray[i][2]+"("+temparray[i][3]+")")
                print(temparray[i][2]+"("+temparray[i][3]+")")

        mergedoutput.writerow(mergefilearray)
        temparray = []
        temparray.append(tsvfile1value)

def main():
    tsvfile1 = open("title.basics.tsv","r")
    tsvfile2 = open("title.akas.tsv","r")
    #skip first line of files with names
    next(yield_tsv(tsvfile1))
    next(yield_tsv(tsvfile2))
    tsvfile1value = [] #value that is being read in file 1 at the moment (primaryTitle)

    with open('title.basics.tsv', 'r') as f:
        lines = f.read().splitlines()     #hold the last line of file to exit()
        last_line = lines[-1].split("\t")   #when we yield the last result
    f.close()

    outputarrayformat = ["titleId","primaryTitle","title(regions)"]
    mergedoutput.writerow(outputarrayformat)

    while tsvfile1value!=last_line:
            tsvfile1value = next(yield_tsv(tsvfile1))
            print("\t"+tsvfile1value[0])
            print(tsvfile1value[2]+"\t")
            mergedtsvfile.write(tsvfile1value[0]+"\t"+tsvfile1value[2]+"\t")
            mergeByID(tsvfile1value,tsvfile2,tsvfile1value[0])
            print("-----------------------------")

    tsvfile1.close()
    tsvfile2.close()
    mergedtsvfile.close()

if __name__ == "__main__":
    main()
