import os
def tryfiles(pathfile):
    try:
        files=os.listdir(pathfile)
        print(files)
        fname=""
        size=0
        file1=[]
        size1=[]
        d={}

        for f in files:
            if(f.endswith(".pdf") or f.endswith(".jpg") or f.endswith(".docx")):
                print(f)
                file1.append(f)
                print(os.path.getsize(pathfile+f))
                temp=os.path.getsize(pathfile+f)
                sizeinmyb=temp/(1024*1024)
                size1.append(sizeinmyb)
                d[f]=sizeinmyb
                # d.append(f,)
                if(size<temp):
                    fname=f
                    size=temp
                # os.system("D:\\"+f)
                alldata=list(zip(file1,size1))
                print("Max file name and size is ")
                print(fname,size)
                print(alldata)
                sizeinmb=size/(1024*1024)
                print(sizeinmb)
                print(sorted(d))

                alldata.sort(key=lambda x:x[1])
                print(alldata)
        
    except FileNotFoundError:
            print("File not found ")

    except ImportError:
        print("Import kar")

while True:
    user=input("Enter path ")
    tryfiles(user)
