import os
import shutil

class Organizer():
    def __init__(self, src, dst):
        self.name        = "Organize files based on its extensions."
        self.source      = src
        self.destination = dst

    def move(self):
        # get all directories
        files = os.listdir(self.source)

        for file in files:
            dir = os.path.join(self.source, file) # folder directories

            # conditional statements for getting regular files
            if os.path.isfile(dir):
                # split root (name) and extension (ext)
                name, ext = os.path.splitext(dir)
                # folder extensions
                dir_file_ext = f"{self.destination}/{ext[1:]}"
                
                os.makedirs(dir_file_ext, exist_ok = True)

                # file paths
                file_path = f"{dir_file_ext}/{file}"

                # move all directories to file_path
                shutil.move(dir, file_path)

    def run(self):
        self.move()
        print(f"Source     : {self.source}     ")
        print(f"Destination: {self.destination}")

if __name__ == "__main__":
    # Set source and destination. 
    src = "C:/Users/Administrator/Downloads"
    # Creating 'new_folder' in variable instead of create manually
    dst = f"{src}/new_folder"

    # create your own object
    organize = Organizer(src, dst)

    # run your program :)
    organize.run()
