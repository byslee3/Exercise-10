from sys import argv
import string


#Open the file and convert it to lowercase
script, file_name = argv

my_file = open(file_name)


#Create an initial placeholder dictionary
counter_dict = {}


#This block of code will go through each word one by one
for line in my_file:                                        #Read each line one by one
    
    words_on_line = line.strip().split()                    #For each line, strip it and split it into words

    for word in words_on_line:                              #Read each word one by one      

        word = word.strip(string.punctuation)               #Strip the punctuation from beginning and end of word
        word = word.lower()                                 #Convert it to lowercase

        counter_dict[word] = counter_dict.get(word,0) + 1   #Does the same thing as the block comment below

        """
        if word in counter_dict:                  #If the word is already in the dictionary
            counter_dict[word] += 1               #Increment the word counter by 1
        elif word not in counter_dict:            #If the word is NOT in the dictionary yet
            counter_dict[word] = 1                #Create a new entry in the dictionary and set the word counter = 1
        """


#Close the file
my_file.close()


#Loop through the dictionary and print it out
#for word, count in counter_dict.items():
#   print "%s <------> %d" % (word, count)


#####################################################
#Extra Credit: Print in descending order of frequency

#Create one list = All of the keys in the dictionary
#Create another list = All of the values in the dictionary
#Create this as a list of tuples

paired_list = []

for word, count in counter_dict.items():
    tuple_to_add = (count, word)   #Switch the order of word and count so that we can sort by the first element in the tuple automatically
    paired_list.append(tuple_to_add)

sorted_list = sorted(paired_list, reverse=True)  #Sort the list by first element in tuple

for item in sorted_list:        #Print out the sorted list
    print str(item[1]) + " <----> " + str(item[0])





