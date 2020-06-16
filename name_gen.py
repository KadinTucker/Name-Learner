import random
import json

MIN_LEN = 3
MAX_LEN = 9

LETTERS = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
INDICES = {}

for i in range(len(LETTERS)):
    INDICES[LETTERS[i]] = i

#fitness variables: frequency, following



def generate_name(frequencies, following):
    length = random.randint(MIN_LEN, MAX_LEN)
    letter_pool = get_letter_pool(frequencies)
    name = random.choice(letter_pool)
    prev_letter = name[0]
    for i in range(1, length):   
        name += random.choice(letter_pool + get_letter_pool(following[INDICES[prev_letter]]))
        prev_letter = name[i]
    return name

def get_letter_pool(frequencies):
    pool = []
    for x in range(len(frequencies)):
        for y in range(frequencies[x] + 1):
            pool.append(LETTERS[x])
    return pool
    
def query_name(name, frequencies, following):
    query = raw_input("Is the string '" + name + "' a name? ")
    if query.startswith("y"):
        learn_name(name, frequencies, following)

def learn_name(name, frequencies, following):
    for x in range(len(name) - 1):
        frequencies[INDICES[name[x]]] += 1
        following[INDICES[name[x]]][INDICES[name[x + 1]]] += 1
    frequencies[INDICES[name[len(name) - 1]]] += 1
    

def main():
    #frequencies = [0 for i in range(26)]
    #following = [[0 for i in range(26)] for i in range(26)]
    freqs = open("frequencies.txt", "r")
    follows = open("followings.txt", "r")
    frequencies = json.load(freqs)
    following = json.load(follows)
    freqs.close()
    follows.close()

    for i in range(100):
        query_name(generate_name(frequencies, following), frequencies, following)

    #for i in range(100):
    #    learn_name(raw_input(" : "), frequencies, following)
    
    freqs = open("frequencies.txt", "w")
    follows = open("followings.txt", "w")
    json.dump(frequencies, freqs)
    json.dump(following, follows)
    freqs.close()
    follows.close()

if __name__ == "__main__":
    main()