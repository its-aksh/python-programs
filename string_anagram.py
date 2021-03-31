"""
Program to check the string anagram in the given array:


"""
from collections import Counter    
def stringAnagram(dictionary, query):
    counter_array = []
    for index, que in enumerate(query):
        que_list = list(que)
        que_list.sort()
        query[index] = ''.join(que_list)
    for index,  val in enumerate(dictionary):
        val_list = list(val)
        val_list.sort()
        dictionary[index] = ''.join(val_list)
    dict_counter = dict(Counter(dictionary))
    for que in query:
        counter_array.append(dict_counter.get(que, 0))
    return counter_array
  
  
if __name__ == "__main__":
    counter_array = stringAnagram(["heater","cold","clod","reheat" ,"docl"], ["codl", "heater", "abcd"])
    print(counter_array)
