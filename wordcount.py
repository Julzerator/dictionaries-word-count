def file_word_count(filepath):
    """ 
    This function opens a file and counts how many times each space-separated 
    word occurs then prints those counts
    """
    word_counter = {}

    for line in open(filepath):
        line = line.rstrip()
        line = line.split(" ")

        for word in line:
            if word_counter.get(word) == None:
                word_counter[word] = 1

            else:
                word_counter[word] = word_counter[word] + 1


    for key, value in word_counter.items():
        print "word = %r, count = %r" % (key, value)


file_word_count("test.txt")

