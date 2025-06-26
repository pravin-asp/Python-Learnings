def count_letters(word_list):
    """ See question description """

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0

    # enter code here
    count = 0
    letter = ""
    for word in word_list:
        for ch in word:
            letter_count[ch] += 1
            if letter_count[ch] == count:
                letter = min(letter, ch)
            elif letter_count[ch] > count:
                letter = ch
                count = letter_count[ch]

    return letter


monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")
print(count_letters(monty_words))
