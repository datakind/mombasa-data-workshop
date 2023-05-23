# This is a comment, note the '#' at the start. Python will ignore anything after a '#'

print("Hello Mombasa!")    # Print something!

x = 10                     # Set a variable 'x' to a value 10
print(x)                   # Print the value of a variable

# There are different types of variables
a = 10                     # An integer
b = 3.14                   # A floating point number
c = "Hello!"               # A string
my_variable = 10           # A variable can have any name
my_list = [1, 2, 3, 4, 5]  # A list of numbers
my_list = ['a', 'b', 'c']  # A list of strings
b = str(10)                # Convert a number to a string
# A list of mixed types
my_list = [1, 'a', 3.14, 'bananas', 'bike', 'Hitchiker guide to the galaxy']   
my_tuple = (1, 2, 3, 4, 5) # A tuple of numbers, you can't change the values
my_dict = {
    'a':19, 
    'b':21, 
    'c':3
} # A dictionary of key-value pairs

# You can access individual values in lists and dictionaries
print(my_list[0])          # Print the first element of a list
print(my_dict['a'])        # Print the value of the key 'a' in a dictionary, which would be 19
print(my_dict.keys())      # Print the keys of a dictionary

# You can also access ranges of values
print(my_list[0:2])        # Print the first 3 elements of a list. Note how counting starts at 0!

# You can do mathematics with numbers where '*' means multiply, and '/' means divide.
z = 2 * x + 3
print(f"x is {x} and so z is {z}")

# You can loop over lists
for val in my_list:         
   print(val)               # Print each number in the list

# Tell 'em about indentation, each indent signifies an inner section of code

# If statements (Boolean logic)
for val in my_list:     
   if val == 'a':           
       print("Woooo Hoooooooo! We found an 'a'!!! Life is AMAZING!!!") 

# If statements with more, err, ifs. Also, 
for val in my_list:     
    if 'a' in str(val) and val != 'a':           
        print(val) 

# You can define a function, a special tiny program that you can use later
def my_function(x):        # Define a function called 'my_function' that takes one input argument 'x'
   return x * 2           # Return the value of x multiplied by 2

result_var = my_function(10)     # Call the function with the value 10. It will return 20

# Class
class MyClass:
    def __init__(self, name, age):  # The __init__ function is called when you create a new instance of the class
        self.name = name            # Set the name attribute of the class to the value of the input argument 'name'
        self.age = age              # Set the age attribute of the class to the value of the input argument 'age'
    
    def my_function(self):          # Define a function called 'my_function' that takes no input arguments
        return self.age             # Return the value of the age attribute
    
class_instance = MyClass("Matt", 20) # Create a new instance of the class called 'class_instance'
print(class_instance)                # Weird machine stuff
print(class_instance.my_function())  # Call a class method which lies about Matt's age

# ============ Present Dataframe goodies here!!! =======

# Reading a CSV file
import pandas as pd        # Import the pandas library

# Create an empty dataframe
output_data = pd.DataFrame() 

# Import from a datafile
input_data = pd.read_csv('./data/bongo-music-data.csv', sep=',') # Read the CSV file into a variable called 'input_data'

# Getting some summary info
print(input_data.shape)
print(input_data.info())

# Dropping those darn NAs
print(input_data["Main Artist"])
input_data = input_data.dropna(subset=["Lyrics"])
print(input_data["Main Artist"])
input_data.dropna(subset=["Lyrics"], inplace=True)

# Replacing values
input_data["Main Artist"].replace("Diamond Platnumz", "Diamond", inplace=True)

# Renaming columns
input_data.rename(columns={"Artists": "Main Artist and featured Guest"}, inplace=True)
print(input_data.info())

# Subsetting madness!
print(input_data["Song"])
print(input_data["Main Artist"][0:10])
data = input_data[0:10, "Main Artist"]  # !!!???? What the R!?
data = input_data.loc[0:10, "Main Artist"]  
print(data)

# Creating columns
input_data['stuff'] = 'things'
print(input_data.columns)
input_data["word_count"] = input_data["Lyrics"].str.split().str.len()

# Looping over rows
for index, row in input_data.iterrows():
    print(row["Song"])

# Calculating stats using apply
print(input_data[["word_count"]].apply(["mean","median","min","max"]))

# Doing more stuff with apply
input_data["most_common_word"] = input_data["Lyrics"].apply(lambda x: pd.value_counts(x.split(" ")).index[0])   
print(input_data[["Song","most_common_word"]])

# Grouping
print(input_data.groupby("Main Artist").agg({"word_count": ["mean", "median", "min", "max"]}))

# Sorting
print(input_data.sort_values(by="word_count", ascending=False))

# Merging
input_data2 = pd.read_csv('./data/bongo-music-data.csv', sep=',') # Read the CSV file into a variable called 'input_data'
input_data_merged = input_data.merge(input_data2, on="Song", how="left")
print(input_data_merged.info())

# Pandas profile report 
from pandas_profiling import ProfileReport
profile = ProfileReport(input_data, title="Pandas Profiling Report")
profile.to_file("output.html")

# Output
input_data.to_csv('./data/test.csv')

