# check whether the given 2 strings are anagrams


def is_anagrams(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # check if same numbers of letters
    if len(s1) != len(s2):
        return False

    # count frequency of each letter
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

x = is_anagrams('clint EASTWOOD', 'old WEST action')

print(x)

is_anagrams('dog', 'god')
