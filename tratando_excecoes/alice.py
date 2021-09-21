# title = "Alice in Wonderland"
# print(title.split())


def count_words(filename):
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {str(num_words)} words.")


fnames = ['alice.txt', 'moby_dick.txt', 'little_women.txt', 'siddhartha.txt']
for fname in fnames:
    count_words(fname)
