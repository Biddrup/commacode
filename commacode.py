#This will take a list from user and
#return with all the iteams by a comma and a space
# inserted 'and' before the last one


#This function will make list to string
def listname(givenlist):
    dostring = ''
    for i in givenlist:
        dostring = dostring + str(i)
        if givenlist.index(i) == len(givenlist) - 2:
            dostring = dostring + ', and '
        elif givenlist.index(i) == len(givenlist) - 1:
            dostring = dostring
        else:
            dostring = dostring + ', '
    return dostring

#variable for the list
makealist = []

print ('For which you are going to make a list')
urlist = input()
print ('Type your input name or hit enter when you done')

#Making a list base on your given value
while True:
    print('Input or empty: ')
    name = input()
    #This will continue until user give value
    if name != '':
        #This will add the new input in the list
        makealist.append(str(name))
        continue
    #Empty value stop this loop
    else:
        break
print ('So, your list of ' + urlist + ' is: ')
print(listname(makealist))
