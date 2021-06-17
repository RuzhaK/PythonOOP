VOWELS={'A', 'E', 'U', 'I', 'O'}
def vowel_filter(function):

    def wrapper(*args,**kwargs):
        result= function(*args,**kwargs)
        return [c for c in result if c.upper() in VOWELS]


    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())


