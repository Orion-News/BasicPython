def read(file_name):
    a = open(file_name, 'r')
    for i in a:
        print(i)

    a.close()


def save_file(file_name, text):
    a = open(file_name, 'w')
    a.write(text)

    a.close()


def create_file(file_name):
    a = open(file_name, 'x')

    a.close()


def append_file(file_name, text):
    a = open(file_name, 'a')
    a.write(text)
    
    a.close()

create_file('pessoas.txt')
save_file('pessoas.txt', 'ana \ncarlos \nMarcos \nGabriela \nAlexandre \nTiago \n')
append_file('pessoas.txt', '\nDaniel \n')
read('pessoas.txt')
