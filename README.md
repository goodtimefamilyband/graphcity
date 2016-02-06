# graphcity
Devfest 2016

Team Members:

* Andrew O'Reilly
* Alex Curtis
* Dillon Omane
* Tianhao Lu

The goal for this hackathon was to visualized cities and their charateristics and relationships to eachother. To do this we scraped data from Wikipidia pages, made a database of the major cities and measured the distance using cosine similarity. To finalize we created a search bar where one could input a city and show a 5 point node graph that gives you 5 other related cities.The tools we used to build this project were Python,Flask, MongoDB, and D3.js. Python and Flask were used for the web framework and front-end design. MongoDB was used to interpret our reference points of data. Lastly D3 was used to create and interactive node like display of our information.

To set up the database, run the python scripts import\_cities and import\_data (in that order) to load the information into a Mongo Database.  Apologies if requirements.txt is not set up properly.
