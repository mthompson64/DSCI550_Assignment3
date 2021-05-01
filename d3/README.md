[D3](https://d3js.org/) Visualizations
===



Pre-requisite
===
- Download most recent package if desired: [D3](https://d3js.org)
- Other requirements are embedded within the HTML files such as any additional libraries or formatting used as well as the d3 v4 version
- If remotely does not work, download this folder with the corresponding data folder and run on a LOCAL HOST (specifically http://localhost:8888/). The file paths are coded within the HTML.


D3 visualization
----------------

### Unemployment Rates
- Unemployment rates extracted from Assignment 1 to match to email senders' locations.
- Multi-line chart with hover labels for each country over 2003-2007
```
* unemployment_final.json
* unemployment.html
```

<img src="https://github.com/mthompson64/DSCI550_Assignment3/blob/main/d3/unemployment.png" width = "900px" style = "float:left">


### Time Heatmap
- Extracted sent email timestamps and constructed a heatmap of the frequencies of sent emails.
- Non-interactive heatmap of cross frequencies (day of week vs. time of day)
```
* day_hour_final.json
* day_hour.html
```

<img src="https://github.com/mthompson64/DSCI550_Assignment3/blob/main/d3/heatmap.png" width = "900px" style = "float:left">

### Bubble Chart Content
- Most common words extracted from the fraud email messages grouped by our social engineering tags from Assignment 1.
- Non-interactive bubble chart 
```
* text.json
* bubble_se.html
```

<img src="https://github.com/mthompson64/DSCI550_Assignment3/blob/main/d3/bubble_chart.png" width = "900px" style = "float:left">

### Attacker Titles
- All attacker titles and their frequencies
- Non-interactive circular barplot 
```
* titles.json
* titles.html
```

<img src="https://github.com/mthompson64/DSCI550_Assignment3/blob/main/d3/attacker_titles.png" width = "900px" style = "float:left">


### Tika-Similarity
- Comparison of Tika-Similarity measures
- Non-interactive multilayered histogram
```
* cosine.csv
* edit.csv
* jaccard.csv
* histogram.html
```

<img src="https://github.com/mthompson64/DSCI550_Assignment3/blob/main/d3/histogram.png" width = "900px" style = "float:left">



