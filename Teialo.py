import re

def Teialo (input_path, output_path):
    paragraph_list = []
    with open(input_path, 'r', encoding='utf8', errors='ignore') as myfile:
        data = myfile.read()
        paragraphs = data.split("\n")
        while '' in paragraphs:
            paragraphs.remove('')
    for pos, x in enumerate(paragraphs):
        if '"' in x:
            paragraphs[pos] = re.sub(r'\"(.+?)\"', '<q>"' + r"\1" + '"</q>', x)
    for x in paragraphs:
        if x[0].isdigit() and x[1]==".":
            paragraph_list.append("<head>" + x + "</head>")
        else:
            paragraph_list.append("<p>"+x+"</p>")
    with open(output_path, "w") as output:
        for x in paragraph_list:
            print(x)
            output.write(x+"\n")


def Glossalo (input_path, output_path):
    with open(input_path, 'r', encoding='latin1', errors='ignore') as myfile:
        data = myfile.read()
        paragraphs = data.split("\n")
        while '' in paragraphs:
            paragraphs.remove('')
    for pos, x in enumerate(paragraphs):
        if len(x) < 2:
            paragraphs[pos] = "<head>" + x + "</head>"
        else:
            name = x.split(":")[0].replace(" ", "_")
            paragraphs[pos] = '<gloss target="#' + name + '">' + x + "</gloss>"
    with open(output_path, "w") as output:
        for x in paragraphs:
            print(x)
            output.write(x+"\n")
            
            
     #Made with love and laziness by Fabio Mariani
     #CC BY-NC 4.0 
