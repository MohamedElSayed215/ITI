from pathlib import Path 

def reading_file():
    input_file=input('Enter file name : ')
    file=Path(input_file)
    try :
        content=file.read_text()
    except FileNotFoundError :
        print(f"file name : '{file}' is not exist")
        text=input('Would you like to try again? (yes/no):')
        if text == 'yes' :
            reading_file()
    else :       
        print(content)


reading_file()

