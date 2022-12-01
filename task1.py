import csv


data  = csv.reader (open ("task.csv" , "r"))

mydict ={}

for i in data :
	mydict [i[0]] = {'clk' : i [1], 'type' : i [2]}	
#print (mydict)	




mylist = list (mydict.items())
#print (mylist)



f1 = open ("task.csv" , "r")
f2 = open ("mytaskcsv.csv", 'w')
f3 = csv.writer (f2)

for i in mylist:
	f3.writerow (i)





#f2 دا اسم الفايل ال هنكتب فيه او م الاخر اسم المتغير ال هستخدمه للتعبير عن اسم الفايل ال هنكتب فيه
#f3  دا اسم المتغير ال شايل الميثود ال بترايت ال هو غالبا كدا يعني الميثود دي ال امبلمنتشن بتاعها بيرتنرن حاجة
