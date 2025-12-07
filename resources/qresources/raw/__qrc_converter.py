from os import system, listdir
from os.path import join, dirname, isfile


def convert(qrc_directory: str, py_directory: str) -> None:
    for file_name in listdir(qrc_directory):
        qrc_file_path = join(qrc_directory, file_name)
        py_file_name = file_name.replace(".qrc", ".py")
        py_file_path = join(py_directory, py_file_name)

        if isfile(qrc_file_path) and file_name.endswith(".qrc"):
            print(f"Converting {qrc_file_path}")
            status = system(f"PySide6-rcc {qrc_file_path} -o {py_file_path}")

            if status == 0:
                print(f"Ui {qrc_file_path} converted")
            else:
                print(f"Ui {qrc_file_path} converting failed. Exit code: {status}")


if __name__ == "__main__":
    qrc_directory = dirname(__file__)
    py_directory = join(qrc_directory, "../")

    convert(qrc_directory, py_directory)

    input("Press enter for closing...")
