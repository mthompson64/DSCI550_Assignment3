### Step 6 GeoParser Instructions
Based on the steps from https://github.com/nasa-jpl-memex/GeoParser/wiki/Sample:-COVID19-publication-data-parsing. BUT, replace the existing files in the GeoParser folder with the files within this Github Q6 Folder. Replacing these files are important to obtain GeoParser location of our fraudulent emails dataset. Information about which files to replace are listed below.

Files To Replace:
1.) Replace 'create-core.sh' (in GeoParser/examples/covid19 folder) with the modified 'create-core.sh' in this Github folder. 
2.) Replace 'add-fields.sh' (in GeoParser/examples/covid19 folder) with the modified 'add-fields.sh' in this Github folder. 
3.) Replace 'Ingest COVID data.ipynb' (in GeoParser/examples/covid19 folder) with 'Ingest fraudulent_emails data.ipynb' in this Github folder. 

Note:
1.) Delete 'download-metadata.sh' because it is not needed to run for our dataset. 
2.) Upload 'fraudulent_emails_v2.tsv' from this Github folder into GeoParser/examples/covid19 folder.

Once you have done all the modification above, you can proceed with the steps to run GeoParser:

### Steps:
1. **Pre-Requisites**:
    
    1.) pip install jupyterlab && pip install notebook
    
    2.) pip install pandas pysolr requests tqdm

2. **Installation**:
    
    1.) docker pull nasajplmemex/geo-parser
    
    2.) docker-compose up -d


3. **Get Data**:

    1.) cd GeoParser/examples/covid19
    
    
    2.) ./create-core.sh (make sure that you can see http://localhost:8983/solr/ if not wait a few seconds for Solr to start up)
    
    3.) ./add-fields.sh 


4. **Open Up Jupyter**:
    
    1.) cd GeoParser/examples/covid19 && juptyer notebook

    2.) Run Ingest fraudulent_emails data.ipynb (will take ~10-20 minutes)


5. **Using GeoParser**:

    1.) Click on Configure Index Tab

    2.) Set Domain Name to fraudulent_emails.
    
    3.) Set Index Path to http://localhost:8983/solr/fraudulent_emails/
    
    4.) Click on add index

    5.) Click add index to store the index of the domain in the database.

    6.) Click on Database Icon Tab

    7.) Click on GeoParse button, and then wait (takes ~10 minutes)

    8.) Click on View button
