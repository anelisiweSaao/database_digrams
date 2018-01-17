import os

#add_css =''
for filename in os.listdir(os.getcwd()+"/files"): # files in a directory

    if filename.endswith('.html'): #files that ends with .html extension

        with open('files/' + filename, 'r') as file: #open files to read and write

            with open('2' + filename, 'w')  as newFiles:  # create new files

                for line in file: #loop every line in a file
                    #print(line)
                    if line == '<head>\n': # if line is head in html
                        line +='<link rel = "stylesheet" type = "text/css" href = "styling.css" >\n' #add this line below the head

                    if line == '<body>\n':  # if line is body in html
                        #print('its heeeeerreee', line)
                        line += '<div class="topnav" id="myTopnav"> \n'\
                                '<a href="Home-page.html">Home</a> \n'\
                                '<a href="2Fault.html">fault</a> \n' \
                                '<a href="2SologEvent_layout.html">SologEvent</a> \n' \
                                '<a href="2Salticam.html">Salticam</a> \n' \
                                '<a href="2Rss.html">Rss</a> \n' \
                                '<a href="2proposal.html">proposal</a> \n' \
                                '<a href="2OcsStep.html">OcsStep</a> \n' \
                                '<a href="2ObsConfig_layout.html">ObsConfig</a> \n' \
                                '<a href="2HRS.html">HRS</a> \n' \
                                '<a href="2filedata.html">filedata</a> \n' \
                                '<a href="2Bvit.html">Bvit</a> \n' \
                                '<a href="2Block_Layout.html">Block</a> \n' \
                                '</div>\n'

                    newFiles.write(line)  # add this to new files created





