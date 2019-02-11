k=input("enter the matrixs of row1:")
l=input("enter the matrixs of row2:")
m=input("enter the matrixs of column1:")
n=input("enter the matrixs of column2:")
if(l!=m):
	print("we cannot do the matrixs multipliation")
else:
	A=[[0,0,0],[0,0,0]]
	B=[[0,0],[0,0],[0,0]]
	s=[[0,0],[0,0]]
	for i in range(0,k):
		A[i]=input("enter the matrix row in list form")
	for j in range(0,m):
		B[j]=input("enter the matrix2 row in list form")
	for i in range(0,len(A)):
		print A[i]
	for j in range(0,len(B)):
		print B[j]
	for p in range(len(A)):
		for q in range(len(B[0])):
			for r in range(len(B)):
				s[p][q]+=A[p][r]*B[r][q]
for x in range(0,len(s)):
		print s[x]
