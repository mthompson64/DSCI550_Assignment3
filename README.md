# USC DSCI 550 Assignment 3 - Spring 2021

Team Banana

- [X] Take your TSV dataset and convert the data to JSON to use in D3.
   - [X] You may need to write scripts to summarize your data for D3. As a start,
consider using ETLlib (http://github.com/chrismattmann/etllib) and its
tsvtojson tool.
- [X] Pick 5 visualization types from https://github.com/d3/d3/wiki/Gallery and create
the associated Data Insights web pages and associated JSON data to display them
showing off your dataset (see Task 1). Consider similarity, consider using the
questions from Assignment 1 and Assignment 2 that you answered in your reports
and how the D3 visualizations will help you answer them.
   - [X] Develop scripts for summarizing and preparing your TSV datasets for D3
JSON conversion.
   - [X] The scripts you write are part of your delivery for the assignment. Please
provide documentation for each script that you create in order to visualize
the data using D3. Make sure that your scripts are portable and there are a
simple set of instructions on how to run them. Any libraries that the scripts
depend on should be clearly indicated.
- [X] Ingest your sightings data from TSV JSON you created in Tasks 1 and 2 into
Apache Solr (http://lucene.apache.org/solr/) and/or ElasticSearch
(http://elastic.co). Both have adequate documentation and are easily installed.
- [X] Install Image Space via
https://github.com/nasa-jpl-memex/image_space/wiki/Quick-Start-Guide-with-Im
ageCat. This is optional: You can also write your own custom ingest scripts using
Tika Python (http://github.com/chrismattmann/) and Tika-Server, etc.
  - [X] Ingest your fake attacker image data (whatever you got in assignment #2)
into Image Space using the provided instructions and scripts or the ones
you write on your own using Tika-Python.
  - [X] Browse and find similar images and use the ImageSpace search index and
search the Image forensics and similarity (SMQTK).
- [X] Submit your Solr or ElasticSearch index by tarring it up and gzipping it. Both
your index for your scientist data along with your ImageCat indices.
- [X] Install MEMEX GeoParser and run it against your TSV data and location data
from assignment 1 and 2.
- [ ] (EXTRA CREDIT) Submit Pull request and improve GeoParser, and/or Image
Space. Improvements to the software will be considered for extra credit.
