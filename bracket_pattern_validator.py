"""
Program to validate the bracket opening and closing pattern in a given string of brackets
"""


def bracket_validator(input_string):
    opening_array = ['(', '{', '[']
    closing_array = [')', '}', ']']
    reslt_array = []
    for i in input_string:
        if i in closing_array and not len(reslt_array):
            print('Invalid')
            return
        if i in opening_array:
            reslt_array.append(i)
        elif i == ')' and reslt_array[reslt_array.__len__() - 1] == '(':
            reslt_array.pop()
        elif i == '}' and reslt_array[reslt_array.__len__() - 1] == '{':
            reslt_array.pop()
        elif i == ']' and reslt_array[reslt_array.__len__() - 1] == '[':
            reslt_array.pop()
        else:
            print('Invalid')
            return
    if (not len(reslt_array)):
        print('Valid')
    else:
        print('Invalid')
    return
  
  
if __name__ == "__main__":
    bracket_validator("{{}}{}}}]][[(()))))]]")
