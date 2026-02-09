__all__ = ("find_shortest_longest_word",)
import re

def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    text = re.sub(r'\s+', ' ', text)
    words = text.split(' ')
    a = tuple()
    if len(words) == 0:
        a = (["None", "None"])
    else:
        a = [words[0], words[0]]
        for word in words:
            if len(word) > a[1]:
                a[1] = word
            if len(word) < a[0]:
                a[0] = word
    return a
 
