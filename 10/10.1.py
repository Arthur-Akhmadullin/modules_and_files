from zipfile import ZipFile
import os.path

def add_archive(name, ext):
    try:
        with ZipFile(name, "a") as archive:
            for files in os.listdir("."):
                if os.path.splitext(files)[1] == ext:
                    archive.write(files)
            archive.close()
    except Exception:
        print("Ошибка добавления в архив")


if __name__ == "__main__":
    archive_name = "My_archive.zip"
    file_ext = ".txt"

    add_archive(archive_name, file_ext)