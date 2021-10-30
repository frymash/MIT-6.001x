animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# print(list(animals.values()))

# Submit code after this line

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for i in range(len(aDict)):
        if len(list(animals.values())[i]) > 1:
            count += len(list(animals.values())[i])
        else:
            count += 1
    return count

print(how_many(animals))
