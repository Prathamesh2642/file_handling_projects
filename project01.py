import os

# files=os.listdir("D:\\")
# print(files)
# fname=""
# size=0
# file1=[]
# size1=[]
# d={}

# for f in files:
#     if(f.endswith(".pdf") or f.endswith(".jpg") or f.endswith(".docx")):
#         print(f)
#         file1.append(f)
#         print(os.path.getsize("D:\\"+f))
#         temp=os.path.getsize("D:\\"+f)
#         sizeinmyb=temp/(1024*1024)
#         size1.append(sizeinmyb)
#         d[f]=sizeinmyb
#         # d.append(f,)
#         if(size<temp):
#             fname=f
#             size=temp
#         os.system("D:\\"+f)
# alldata=list(zip(file1,size1))
# print("Max file name and size is ")
# print(fname,size)
# print(alldata)
# sizeinmb=size/(1024*1024)
# print(sizeinmb)
# print(sorted(d))

# alldata.sort(key=lambda x:x[1])
# print(alldata)

# import os
# os.system("D:\\Prathamesh Patil_Studentinfo.docx")


# def filestry(pathoffile):
#     try:
#         files=os.system(pathoffile)
#     except FileNotFoundError:
#         print("File not present in the s ystem")

# pathoffile=input("Enter the path of file: ")
# filestry(pathoffile)
