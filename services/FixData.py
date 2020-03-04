

def fixVocab(prefix, eng_word, mean):
    """
    this service will replace the old mean to the new mean and save to source file
    Return: Nothing
    Example:
    fixVocab(prefix='Destination_B2_unit4', eng_word='hello', mean='xin chao')

    """


    prefix = "statics/data/{}".format(prefix)
    path_to_eng = '{}e.txt'.format(prefix)
    path_to_vie = '{}v.txt'.format(prefix)
    engs, viets = load_files(path_to_eng, path_to_vie)

    for i in range(len(engs)):
        if engs[i] == eng_word:
            viets[i] = mean
            break
    
    with open(path_to_vie, 'w', encoding='utf-8') as file:
        for viet_word in viets:
            file.write("{}\n").format(viet_word)
    file.close()


def updateVocab(prefix, engs, viets):
    """
    can use this function to create data or update existing data
    Return: Nothing

    Example:
    updateVocab('Destination_B2_unit4', ['hello', 'goodbye'], ['xin chao', 'tam biet'])
    the function will create 2 files english and vietnamese and then save data
    """
    prefix = "statics/data/{}".format(prefix)
    path_to_eng = '{}e.txt'.format(prefix)
    path_to_vie = '{}v.txt'.format(prefix)

    with open(path_to_eng, 'w', encoding='utf-8') as file:
        for ele in engs:
            file.write("{}\n".format(ele))
    file.close()

    with open(path_to_vie, 'w', encoding='utf-8') as file:
        for ele in viets:
            file.write("{}\n".format(ele))
    file.close()