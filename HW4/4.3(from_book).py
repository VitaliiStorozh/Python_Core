my_bd = int(input('Year of your burn: '))
years_list = [my_bd, my_bd+1, my_bd+2, my_bd+3, my_bd+4, my_bd+5]
my_3th_bd = years_list[3]
print('Year when I was 3 year old:', my_3th_bd)
things = ["mozzarella", "cinderella", "salmonella"]
print('List of sth: ', things)
things[1] = "Cinderella"
print ('List with element connect wit people upper first letter:', things)
things[0] = "MOZZARELLA"
print('Next step: Chesse element in list upper letter: ', things)
del things[2]
things.append('Nobel prize')
print('Next step: Delete desease, get Nobel prize: ', things)
#Создайте список, который называется surprise и содержит элементы 'Groucho','Chico' и 'Harpo'.
surprise = ['Groucho', 'Chico', 'Harpo']
print(surprise)
#Напишите последний элемент списка surprise со строчной буквы, затем обратите его и напишите с прописной буквы.
str1 = str(surprise[2])
str1 = str1.lower()
surprise[2] = str1
print(surprise)
str1 = str1.title()
surprise[2] = str1
print(surprise)
9**9

