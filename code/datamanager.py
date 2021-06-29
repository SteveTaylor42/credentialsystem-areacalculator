#Import pathlib module to allow for file/folder path checking and creation
import pathlib

#Get absolute path of application root using Path.parents
#'__file__' is used to represent the current script path
#'Path().parents[1]' is the equivilant of 'Path().parent.parent'
current_dir = pathlib.Path(__file__).parents[1]

def get_datafolder():
    """Returns the path to the root application folder '\data' as string. 
If it isn't found, creates a new '\data' folder."""

    #Add '\data' to the current directory path
    #This allows us to check if the '\data' folder exists
    data_dir = str(current_dir) + '\data'

    #Check if '\data' folder exists
    #If not, print an error message and create a new data folder
    if not(pathlib.Path(data_dir).exists()):
        print ("ERROR: \data folder not found. Creating data folder.\n")
        pathlib.Path(data_dir).mkdir()

    #Return the final, error tested '\data' folder directory path
    return data_dir

def get_maxarea():
    """Returns the path to the 'maxarea.txt' file in '\data' as string. 
If it isn't found, creates a new maxarea.txt file (with the default value of 4)."""

    #Set maxarea_dir to data_dir + '\maxarea.txt'
    #This gives us the final, absolute path to the maxarea.txt file
    maxarea_dir = get_datafolder() + '\maxarea.txt'
    
    #Check if '\maxarea.txt' file exists
    #If not, print an error message and create a new maxarea.txt file
    if not(pathlib.Path(maxarea_dir).exists()):
        print ("ERROR: \data\maxarea.txt not found. Creating maxarea.txt with the default value of 4.\n")
        open(maxarea_dir, "w").write("4")

    #Return the final, error tested 'maxarea.txt' directory path
    return maxarea_dir

def get_userdata():
    """Returns the path to the 'userdata.txt' file in '\data' as string. 
If it isn't found, creates a new blank userdata.txt file."""

    #Set userdata_dir to data_dir + '\\userdata.txt'
    #This gives us the final, absolute path to the userdata.txt file
    #(The '\\' lets us ignore the '\u' Unicode prefix)
    userdata_dir = get_datafolder() + '\\userdata.txt'
    
    #Check if '\userdata.txt' file exists
    #If not, print an error message and create a new userdata.txt file
    if not(pathlib.Path(userdata_dir).exists()):
        print ("ERROR: \data\\userdata.txt not found. Creating userdata.txt file.\n")
        open(userdata_dir, "w").write("")

    #Return the final, error tested 'userdata.txt' directory path
    return userdata_dir