import os

class DirLooks:

    def __init__(self, name_dir):
        self.name_dir = name_dir
        self.is_dir = True


    def dir_contents(self):
        if self.is_dir:
            dirs = list()
            files = list()
            for item in os.listdir(self.name_dir):
                if os.path.isdir(item):
                    dirs.append(item)
                else:
                    files.append(item)
            self.content = {'filenames': files, 'dirnames': dirs}

    def sort(self, reverse):
        if isinstance(reverse, bool):
            self.content['filenames'].sort(reverse = reverse)
            self.content['dirnames'].sort(reverse = reverse)
            return self.content
        else:
            print('Input False or True')

    def add_i(self, i):
        if '.' in i[1:]:
            self.content['filenames'].append(i)
        else:
            self.content['dirnames'].append(i)
        return self.content

direcroty = DirLooks(os.getcwd())
direcroty.dir_contents()
print(direcroty.content)
print(direcroty.add_i('Dir'))
print(direcroty.add_i('File.txt'))
print(direcroty.sort(False))