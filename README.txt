DSCI 550 Assignment 3
Team Banana
Madeleine Thompson, Sarah Pursley, Katie Chak, Amber Yu, and Claudia Winarko

To run code:
Install all dependencies in requirements.txt

***

Q1 folder - Did not end up using the tsvtojson tool to summarize our TSV from Assignment 2. There were some structural issues with the TSV file so we ended up using the JSON from Assignment 2. Unzip the fraudulent_emails_v2.zip and extract the fraudulent_emails_v2.json file, then run pre-processing.py from the same folder as fraudulent_emails_v2.json to summarize the data for easy ingest into D3.

Q2 folder (D3) - Read README.md for an in-depth view of how to re-create the five D3 visualizations. Will use the data created from pre-processing.py and five HTML scripts to create the visualizations. You will have to use localhost:/8888 or a similar port to visualize these scripts in your browser.

Q3/Q5 - setup a Solr instance on your local computer and ingest fraudulent_emails_v2.json and the data files created by pre-processing.py. You will find the indexed results in the Q5 folder along with the ImageSpace index.

Q4 folder (ImageSpace/ImageCat) - See screenshots in this folder of our ImageSpace instance.

Q6 folder (GeoParser) - Read README.md for an in-depth view of how to recreate GeoParser. You will need a copy of fraudulent_emails_v2.json for this step.