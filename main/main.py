meme_dict = {
                "КРИНЖ": "Что-то очень странное или стыдное",
                "ЛОЛ": "Что-то очень смешное",
                'РОФЛ': 'Шутка',
                'ЩИЩ': 'Одобрение или восторг',
                'КРИПОВЫЙ': 'Страшный, пугающий',
                'АГРИТЬСЯ': 'Злиться'
                }
    word = input("Введите непонятное слово (большими буквами!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
        point = point + 1
    else:
        print('Слово не нашлось, пожалуйста, повторите ввод.')
