import os
import shutil

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
titles = ['Home', 'Proposal', 'Block', 'Salticam', 'SologEvent', 'Fault', 'Filedata', 'OcsStep', 'Hrs', 'Bvit', 'Rss']
files = ['Home-page.html'] + ['files/' + filename for filename in os.listdir(os.getcwd()+"/files")]

for path in files: # files in a directory
    filename = os.path.split(path)[1]
    if filename.endswith('.html'): #files that ends with .html extension
        with open(path, 'r') as file: #open files to read and write
            current_page =filename
            if not os.path.exists(os.getcwd() + '/output'):
                os.makedirs('output')
            with open('output/'+current_page ,'w')as newFiles:  # create new files
                for line in file: #loop every line in a file
                    if line == '<head>\n': # if line is head in html
                        line +='<link rel = "stylesheet" type = "text/css" href = "../styling.css" >\n' #add this line below the head
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





