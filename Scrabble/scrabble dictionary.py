from point_conversion import point_calculation #Refers to file point_calulation
def word_possiblies(hand):#This function checks all the different word possiblies from user input.
    with open('C:\\Testdata\\CROSSWD.txt','r',errors ='ignore')as dictionary: #opens the file
        word_list = dictionary.readlines()
    player_words = []#list of all possible words
    for word in word_list:#Loop that goes through the file
        current_word = word.strip()
        player_hand = list(hand)#makes hand into a list.\
        count = 0
        for letter in current_word:#Loop that goes through the word and checks if a letter in player's hand is in the the word.
            if letter in player_hand:
                player_hand.remove(letter)
                count += 1
        if len(current_word) == count:#Checks if all letters in word, if true put into list.
            player_words.append(current_word)
    return point_calculation(player_words)


if __name__ == "__main__":#This function ask the user to input all the letters as one string.
    user_input = input("Please enter you scrabble word hand(Please type in this format: aaaaaaa):")
    for item in (x for x in word_possiblies(user_input)):
        print(item)
        
