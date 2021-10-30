animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# Submit the code below this line
def biggest(aDict):
    largestkey = None
    for i in range(len(aDict)):
        #print(list(aDict.values())[i])
        if largestkey is None or len(list(aDict.values())[i]) > len(largestkey[1]):
            largestkey = list(aDict.items())[i]
    return largestkey[0]

print(biggest(animals))
