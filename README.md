# Name-Learner
A terrible, uneducated attempt at making a machine learn how to generate realistic-looking names, such as those one might find in a sci-fi or fantasy universe.

## How it works

The name generator works by randomly generating strings of characters. The chance to choose each character, however, is based on data given by a human. The human, in this case, determines whether or not a randomly generated string is a "name". 

If the string is determined to be a name, the program stores each character in the string and each character that follows another character. For example, if the string `halbi` was determined to be a name, the program would store occurrences of `h`, `a`, `l`, `b`, `i`, and store that `a` followed `h`, `l` followed `a`, and so on. 

Given this data, the generator is then more likely to choose letters which have occurred more frequently in names, and it is more likely to place letters that have more often followed the letters in existing names.

## Successes and Failures

From what I have seen the frequency of more name-looking strings has increased over time with learning. However, there are some problems with the way the generator recognizes names. One notable issue is that there is no way to prevent tripled letters. This is something that never occurs, but since double letters exist, it is very possible and fairly likely for tripled letters to appear given this method of generation. This issue is not so severe, as it is simple enough to remove extra letters. Another issue is that there is no discrimination between vowels and consonants. It is true that vowels will more often follow consonants than consonants following consonants, but given this generation method it is fairly likely to have unrealistic consonant clusters in words. 

As such, this name generator, in its current state, will most certainly never learn itself to the point that it can reliably generate names.
