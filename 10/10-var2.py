from zipfile import ZipFile
import os.path

def add_archive(name, ext):
    try:
        with ZipFile(name, "a") as archive:
            for root, dirs, files in os.walk("."):
                for filename in files:
                    if os.path.splitext(filename)[1] == ext:
                        archive.write(os.path.join(root, filename), filename)
            archive.close()
    except Exception:
        print("Ошибка добавления в архив")


if __name__ == "__main__":

    archive_name = "My_archive.zip"
    file_ext = ".txt"
    add_archive(archive_name, file_ext)