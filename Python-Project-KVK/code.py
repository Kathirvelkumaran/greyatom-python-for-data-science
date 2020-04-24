# --------------
# Code starts here
class_1= ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
#a=type(class_1)
print(class_1)
#print(a)
class_2= ['Hilary Mason','Carla Gentry','Corinna Cortes']
print(class_2)

new_class=class_1+class_2
print(new_class)

new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)







# Code ends here


# --------------
# Code starts here
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60 }
print(courses)
a=type(courses)
print(a)

total=sum(courses.values())
print(total)

percentage=total/len(courses.values())
print(percentage)
# Code ends here


# --------------
# Code starts here
mathematics= {'Geoffrey Hinton':78 ,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

print(mathematics)
topper1=max(mathematics.values())
print(topper1)
topper=max(mathematics,key=mathematics.get)
print(topper)






# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
print(topper)
first_name = topper.split()[0]
last_name = topper.split()[1]
print(first_name)
print(last_name)
full_name= last_name+ " " + first_name
print(full_name)
# Code starts here
certificate_name=full_name.upper()
print(certificate_name)


# Code ends here


