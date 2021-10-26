def get_data(aTuple):
    '''
    args: aTuple -> a tuple nesting a few 2-tuples in the format (number,word)
    e.g. (1,one),(2,two),(3,three)

    returns: a tuple with 
        1. the smallest number (min_nums)
        2. the highest number (max_nums)
        3. the no. of unique words (unique_words)
    '''
    nums = ()
    words = ()
    for t in aTuple:
        nums += (t[0],)
        if t[1] not in words:
            words += (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)

(small,large,words) = get_data(((1,'yes'),
                                (2,'no'),
                                (3,'yes')))
# Expected values: 
# small = 1, 
# large = 3, 
# words = 2 (since there's 2 unique words: 'yes' and 'no)

print('Smallest number:', small, '\n'+
    'Largest number:',large, '\n'+
    'No. of unique words:',words)
