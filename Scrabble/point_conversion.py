import pickle
def point_calculation(word_list):
    file = open("c:\\TestData\\letter_points.dat", "rb")
    points = pickle.load(file)
    file.close()
    word_value = []
    for word in word_list:
        current_word = word.strip()
        total = 0
        for letter in word:
            total += points[letter]
        word_points = f'{current_word}:{str(total)} points'
        word_value.append(word_points)
    return word_value
        
        
            
    

