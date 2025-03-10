def count_words (text):
    words = text.split()
    return len(words)

def count_characters (text):
    result = {}
    for c in text:
        if c.lower() not in result:
            result[c.lower()] = 0
        result[c.lower()] += 1
    return result
