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

def sort_on_count(dict):
    return dict["count"]

def generate_report (character_count):
    report = []
    for k in character_count.keys():
        if k.isalpha():
            report.append({
                "character": k,
                "count": character_count[k]
            })
    report.sort(reverse=True, key=sort_on_count)
    return report
