def fix_machine(escombros, producto):
   i = 0
   while i < len(producto):
       if escombros.find(producto[i])==(-1):
           return "Give me something that's not useless next time."

       i = i+1

   return producto





print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time.")
print("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity')
print("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity')
print("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt')
print("Test case 5: ", fix_machine('matrix reloaded', 'dedo mixta lordo') == 'dedo mixta lordo')


def compress(sentence):
    lista = []
    i=0
    while i < len(sentence)-1:
        word = ''
        while sentence[i] != ' ':
            print(i)
            word = word + sentence[i]
            i = i+1;

        if word != '':
            lista.append(word)
            i = i+1



    output = ''
    i=0
    while i<len(lista):
        word = lista[i]
        if list.find(word) == i:
            output = output + i

        if list.find(word) < i:
            output = output + list.find(word)

        i = i + 1

    return output

print(compress("The bumble bee")+' '+ "012")
print(compress("the one bumble bee one bumble the bee")+' '+ "01231203")


