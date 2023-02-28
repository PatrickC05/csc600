# CSC600
## Code
This repository contains all the code for this project. The conda environment is provided in `requirements.txt` and can be installed by running `pip install -r requirements.txt`. The two main files are `nc-gerrychain.ipynb` and `pa-race.ipynb`. The remaining files in `experiments/` are either tutorials or experiments. All files are described below.
### `nc-gerrychain.ipynb`
`nc-gerrychain.ipynb` is a Jupyter Notebook containing the code for generating a graph from the North Carolina 2020 congressional redistricting plan. It goes through the process of loading the shapefile, loading the population data from the census, referencing the block equivalency file, and creating the graph. However, it failed to create a graph on this data because of a bug in Gerrychain converting shapefiles and dataframes into graphs. It failed to do this on the default files provided in the tutorials too. If this method had worked, I would have been able to analyze the potential for racial gerrymandering in North Carolina's 2020 congressional redistricting plan. The shapefile was downloaded from the the US Census Bureau. The population data was downloaded from the US Census Bureau. The block equivalency file was downloaded from the North Carolina Assembly.
### `pa-race.ipynb`
 `pa-race.ipynb` is a Jupyter Notebook containing the code for analyzing the potential for racial gerrymandering in Pennsylvania's 2011 congressional redistricting plan. It is a modified version of the GerryChain tutorial that looks at potential racial rather than partisan gerrymandering. It goes through the process of loading the graph, running the Markov chain, and analyzing the results. It also contains the code for generating the figures in the report. Notably, because `nc-gerrychain.ipynb` failed to create a graph on custom data, I was only able to analyze Pennsylvania, as that was the only state with a graph that could be loaded. The JSON file was downloaded from Gerrychain.

### Other Files
These files are in `experiments/` and are either tutorials I followed or experiments.
* `create-map.ipynb` generates a map of the racial breakdown of North Carolina's Census Tracts based on the 2020 census.
* `gerrychain-recom.ipynb` and `gerrychain-tutorial.ipynb` follow tutorials provided by GerryChain's documentation.
* `nc-districts.ipynb` generates a map of North Carolina's congressional districts based on the 2020 census.
* `reock.ipynb` calculates the Polsby-Popper and Reock scores for each of North Carolina's districts
* `util.py` contains the code for calculating Polsby-Popper and Reock scores, as I had originally anticipated using them in my analysis before realizing Gerrychain had them already implemented.