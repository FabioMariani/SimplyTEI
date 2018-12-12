import re

def Teialo (input_path, output_path):
    paragraph_list = []
    with open(input_path, 'r', encoding='utf8', errors='ignore') as myfile:
        data = myfile.read()
        paragraphs = data.split("\n")
        while '' in paragraphs:
            paragraphs.remove('')
    for x in paragraphs:
    #this is for chapter title style: ex "1. The siege of Gondor"   Change format if different
        if x[0].isdigit() and x[1]==".":
            paragraph_list.append("<head>" + x + "</head>")
        else:
            paragraph_list.append("<p>"+x+"</p>")
    with open(output_path, "w") as output:
        for x in paragraph_list:
            print(x)
            output.write(x+"\n")
            
