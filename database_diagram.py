import os

# page files and titles
pages = {
    'Home': 'Home-page.html',
    'Proposal': 'proposal.html',
    'Block': 'Block_Layout.html',
    'Salticam':'Salticam.html',
    'SologEvent':'SologEvent_layout.html',
    'Fault':'Fault.html ',
    'Filedata':'filedata.html',
    'OcsStep':'OcsStep.html',
    'Hrs':'HRS.html',
    'Bvit':'Bvit.html',
    'Rss':'Rss.html'

}
titles = ['Home', 'Proposal', 'Block', 'Salticam', 'Rss', 'Hrs', 'Bvit', 'SologEvent', 'Fault', 'Filedata']
files = ['Home-page.html', 'styling.css'] + ['files/' + filename for filename in os.listdir(os.getcwd()+"/files")]

outputPath=os.getcwd()+'/output'
if os.path.exists(outputPath):
    for file in os.listdir(outputPath):
        os.remove(outputPath +'/' +file)
else:
    os.mkdir(outputPath)

for path in files: # files in a directory
    filename = os.path.split(path)[1]
    if filename.endswith(('.html','.css')): #files that ends with .html extension
        with open(path, 'r') as file: #open files to read and write
            current_page =filename
            with open('output/' + current_page ,'w')as newFiles:  # create new files
                for line in file: #loop every line in a file
                    if line == '<head>\n': # if line is head in html
                        line +='<link rel = "stylesheet" type = "text/css" href = "styling.css" >\n' #add this line below the head
                    if line == '<body>\n':  # if line is body in html
                        line += '<div class="topnav" id="myTopnav"> \n'
                        for title in titles:
                            if pages[title] == current_page:
                                className = 'active'
                            else:
                                className = ''
                            line += '<a class="' + className + '" href="' + pages[title] + '">' + title + '</a>'
                        line += '</div>\n'
                    newFiles.write(line)  # add this to new files created
