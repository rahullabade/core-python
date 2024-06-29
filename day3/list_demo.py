"""
x = 21
#y = x
#x = y
print(id(x))
#print(id(y))
#print(id(x))


l = [1,2,3]
print(l)
print(id(l))
l.append("Raahul")
print(l)
print(id(l))

#print(id(l))   

for item in l:
    print(item)
    if item == "aman":
        print(f"{item}found")

#for index, item in enumerate(l):
    #print(index, item)
#list_of_subject = ["RTOS",'iot',"""EOS"""]
#print(list_of_subject.index("""EOS"""))


for index_of_subject, subject in enumerate(list_of_subject):
    print("{0} is at stored {1}".format(subject,index_of_subject))
    """



