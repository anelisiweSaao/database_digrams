# database_digrams
STEPS FOR GENERATING SALT DATABASE DIAGRAMS(sdb_v7)

INTRODUCTION

These are the diagrams drawn from database (sdb_v7) released in 2017 which illustrate some of the tables,columns, keys and relationships in it. The diagrams are grouped in groups showing some relationships in between. This document explains the procedures followed to come up with the diagrams.


TOOLS

DbSchema 7.6.4 version or new

METHODS

Install DbSchema to your machine.

To reverse engineer schema from already existing database and manage schema diagrams.
Click on :

Connect to Database in Dbschema 
Enter details of the database you want to connect 
Select schema you connect to (sdb_v7 in this case)

To start making layout or diagram.

Click on layout on the toolbar
Select new empty layout
Drag the tables you want to connect to the field of the layout
Click on the arrows pointing outside the table to link with other tables

To see the relationship between tables and their data types

Right click on a layout field
Select layout properties
On settings select:
Show column data type
And Foreign key line to Table/Column

To group the tables

Highlight all of the tables to be grouped
Right click on space
click on grouping
 Then click on create a group of tables 

To change the color of the tables

Click on the table on layout or Highlight all the tables you want to change color if they are many
Right click and select change color
Choose the color you want and click ok

Save the project to your machine once done.

To generate html or image.

Click on project
Select Expose as
Then click on html or image
Save the diagram

UPDATING 

Updating an already existing diagram.

Layout showing the diagram must be saved in your machine
Layout saved must be of an extension .dbs NOT html
Click on the layout and it will lead to DbSchema installed in your machine.
The the diagram will be shown on a layout panel in the Dbschema.
Add or delete unnecessary tables in the diagram 
Save the diagram and generate html 

