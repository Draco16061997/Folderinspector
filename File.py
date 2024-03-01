import os
import config


class Folder():

    def __init__(self, path):
        self.path = path
        self.l = []
        self.g =[]

    def WalkFiles(self,current_path=None):
        if current_path is None:
            current_path = self.path

        for i in os.listdir(current_path):

            if os.path.isdir(current_path + '/' + i):
                self.WalkFiles(current_path + '/' + i)
            else:

                self.l.append(i)
        return self.l

    def getListFiles(self):

        for i in self.WalkFiles(self.path):
            s = i.replace(".ewc2", "")
            s = s.replace(".mp4", "")

            s = s.split('_')

            status = False

            for l in config.exept:
                if s[-1] == l:
                    status = False
                    break
                else:
                    status = True

            if status:
                self.g.append(s)


        return self.g


if __name__ == '__main__':
    pass
    folder = Folder(config.path)

    for i in folder.getListFiles():
        print(i)
