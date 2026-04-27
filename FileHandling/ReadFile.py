location = "../Misc/wordlist2-1626415171030.txt"


def open_file_no_closing():
    file = open(location)
    # lines = file.readlines()  # display with new line character \n
    lines = file.read().splitlines()  # without new line character
    print(lines)
    file.close()


open_file_no_closing()


# use with keyword to auto close the file
def open_file_auto_closing():
    try:
        with open(location) as password_file:
            lines = password_file.read().splitlines()
            print(lines)
    except FileNotFoundError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print("Closing the function")


open_file_auto_closing()
