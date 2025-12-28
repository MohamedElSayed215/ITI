from pathlib import Path 

def write_data():
    input_file=input('Enter file name : ')
    text=input('Enter text to save ')
    file=Path(input_file)
    try :
        file.write_text(text)
    except PermissionError :
        print(f"file name : '{file}' can not write !")
    else :       
        print(file.read_text())

write_data()