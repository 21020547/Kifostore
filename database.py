import datetime
import os


class Database:
    FolderList = ["mp3", "video", "picture"]  
    folder_path = ''


    def __init__(self, file_path, root_path):
        self.filepath = file_path
        self.UserDict = {}
        self.load_dictionary()
        self.root_path = root_path


#s_list[0] : Name

#s_list[2] : Password


    def load_dictionary(self):
            with open(self.filepath, "r") as f:
                lst = f.read().splitlines()
                for i in range(len(lst)):
                    s_list = lst[i].split(';')
                    self.UserDict[s_list[1]] = [str(s_list[0]), str(s_list[2]), str(s_list[3]), str(s_list[4])]


    def load_database(self):
        with open(self.filepath, 'w') as f:
            for key in self.UserDict.keys():
                f.write(self.UserDict[key][0] + ';' + key + ';' + self.UserDict[key][1] + ';' + self.UserDict[key][2] + ';' + self.UserDict[key][3] + '\n')



    def save_data(self, name, email, password):
        x = datetime.date.today()
        with open(self.filepath, "a") as f:
            f.write(name + ';' + email + ';' + password + ';' + str(x) + ';' + self.folder_path + '\n')
        
        self.UserDict[email] = [str(name), str(password), str(x), self.folder_path]
        

    def search_data(self, email, passw):
        if (email in self.UserDict): 
            if (self.UserDict[email][1] == passw):
                return True
        return False


    def search_email(self, email):
        if (email in self.UserDict):
            return True
        return False
    
    def get_user(self, email):
        if email in self.UserDict.keys():
            return self.UserDict[email]
        else:
            return "ERROR"
    
    def CreateFolder(self, email):
        
        try: 
            path =  os.path.join(self.root_path, email[0:email.index("@")])
            os.makedirs(path)

            self.folder_path = path

            for folder in self.FolderList:
                newpath = os.path.join(path, folder)
                os.makedirs(newpath)
        except OSError as error:
            print(error)
            




