##create a file that writes and appends the same file to read the content

##basic file operations 
# read(): Reads the entire file content as a single string.
# readlines(): Reads all lines in a file and returns them as a list of strings.
# write(): Writes a single string to a file, overwriting existing content.
# writelines(): Writes a list of strings to a file without adding newline characters automatically.
# Append Mode: Opens a file in append mode to add content at the end without altering existing content.

#reading operation on the file 
with open("contextmanagers\input.txt","r") as file:
    for line in file:
        print(line)

#writing in th file input.txt
with open("contextmanagers\input.txt","w") as file:
    for text_typing_to_file in range(10):
        # file.write(input())   ##it appends all the text into one line of operation no new line is added for them 
        file.writelines(f"{input()}\n") ## these two methods write and writelines do the same thing of writing the contents in one lines but the write returns the number of bytes its take 

##appending operation to a file 
with open("contextmanagers\input.txt","a") as file:
    for text_typing_to_file in range(10):
        file.write(input())
