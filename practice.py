#num =[1,2,3,4,5] 
#total=0
#print(num)
#for i in num:
    
    #total=total+i
#print(total)
#num=[1,5,3,7,8,12,6]
#for i in num:
 #if i % 2 ==0:
  #print(i)
#num=[8,3,5,7.8]
#largestnum = num[0]
#for i in num:
    #if largestnum>i:
        #largestnum = i
#print(largestnum)
#num = (1,2,3,4,5,6,7,8,9,10)
#for i in range(10,0,-1):
   # print(i)
num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

length = 0

# list ki length find krna (loop se)
for i in num:
    length += 1

middle = length // 2

count = 0
for i in num:
    if count == middle:
        print("Middle number:", i)
        break
    count += 1
     

        
        
    
    
       

   




            

