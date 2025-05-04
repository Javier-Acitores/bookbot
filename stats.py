

# Prints a word counter in total
def words_counter(file_contents):
    words = file_contents.split()
    contador = 0
    for i in range(0,len(words)):
        contador += 1
    return f"Found {contador} total words"

# Prints a Dictionary of the different characters used
def character_counter(file_contents):
    characters = file_contents.lower() #this is an list of characters
    result = {}
    for character in characters:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result

def sorted_list_of_dictionaries(character_dictionary):
    list_dictionaries=[]
    for key in character_dictionary:
        temporary_dictionary={}
        temporary_dictionary["char"] = key
        temporary_dictionary["num"] = character_dictionary[key]
        list_dictionaries.append(temporary_dictionary)
    
    list_dictionaries.sort(reverse=True,key=sort_on)
    return list_dictionaries

def sort_on(dict):
    return dict["num"]

def print_sorted_dictionary(list_dictionaries):
    for list_dictionarie in list_dictionaries:
        if list_dictionarie["char"].isalpha()==True:
            print(f"{list_dictionarie["char"]}: {list_dictionarie["num"]}")

#string1 = "aaaaaaaaaaaaaaaaaaaa      bbbbbbbbbbbb"
#print(sorted_list_of_dictionaries(character_counter(string1)))