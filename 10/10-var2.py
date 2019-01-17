from zipfile import ZipFile
import os.path

def add_archive(name, ext):
    with ZipFile(name, "a") as archive:
        for root, dirs, files in os.walk("."):
            for filename in files:
                if os.path.splitext(filename)[1] == ext:
                    print(os.path.basename(filename))
                    archive.write(filename)
        archive.close()

if __name__ == "__main__":
    archive_name = "My.zip"
    file_ext = ".txt"

    add_archive(archive_name, file_ext)