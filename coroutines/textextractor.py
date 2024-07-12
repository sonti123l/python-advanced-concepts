from PIL import Image
import pytesseract


# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCRC:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#image opening
img = Image.open(r"C:\Users\saitr\OneDrive\Documents\GitHub\python-advanced-concepts\coroutines\imagetotext\attendence.jpeg")

#simple image to string
text = pytesseract.image_to_string(img)

# # created a newfile to check for the roll numbers
# with open("rollnumber.txt","w") as f:
#     for i in text:
#         f.writelines(i)


list_of_lists=[]

#using coroutines concept
def file_checker_for_each_line(load_file):
    with open(load_file,"r") as line_in_file:
        for line in line_in_file:
            make_it_into_a_list = (yield line).split()
            list_of_lists.append(make_it_into_a_list)   
            print(list_of_lists) 

#calling this generator object as a coroutine function
file = r"C:\Users\saitr\OneDrive\Documents\GitHub\python-advanced-concepts\coroutines\imagetotext\rollnumber.txt"
generator_file = file_checker_for_each_line(file)
 
i = next(generator_file)
generator_file.send(i)
