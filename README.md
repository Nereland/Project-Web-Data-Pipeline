# Project Web Data Pipeline


The CITES Trade Database holds over 13 million records of trade wildlife. The data that were provided for this study were collected between 2016 and 2017. 

I downloaded the original CITES dataset from [Kaggel](https://www.kaggle.com/), a free platform that provides different types of datasets to analyse.
I chose this one for three main reasons, the first one was that I have always been intersted on animal research and I already knew "Cites", so I was curious. 
Once I looked at the data and I saw all the information they provided, I was sure I wanted to dive into data to understand its meaning, and finally, I thought it could be a good dataset to answer some important questions about the origin, the denstiny, the reasons and the origin of legally traded animals. 
And, thus, with this in mind I proceeded to study data... maybe a little bit too much in depth, I like that part...

![buzzard-5241399_1920](/assets/buzzard-5241399_1920.jpg)

## CITES DATASET

Originally, the objectives of many analyses of CITES trade data were:
####
    - To monitor trade levels and identify where trade might adversely affect wild population

    - To assess whether the information supplied by each Party provides an accurate representation of its trade in CITES-listed species and whether the data were provided in sufficient detail to fulfil the requirements of CITES;
    - To ascertain whether the available data provide evidence of trade infractions or inadequate enforcement of 
    CITES and national regulations; 
    - To discern the most important trade in terms of volume;
    - To provide a summary of major trade between countries and thus facilitate, over time, the analysis of trends in trade; 
    - To identify major anomalies in the reporting of imports and exports.
                                                                            CITES Trade Database - User guide, 2013

## MY QUESTIONS

For the purpose of this study I aimed to investigate:
       
    1. which countries were more frequently animal importers and which were mainly importers.
    2. What was the purpose of the import and export of exotic animals (and for this, I excluded all data related 
    to plants).
    3. Also I was interested in knowing the source, the origin of these animals to be traded, so I also analysed 
    these data.
    4. Of course I was interested on the type of animals that were more frequently traded in 2016-2017,


The rest of the information provided by CITES was not selected for this study. However, and although the original dataset was very complete, basic information regarding the order (i.e. the taxonomic rank) and the phylum (i.e. the principal taxonomic category that ranks above class and below kingdom) of the animals was not provided. 

In order to include some taxonomic information, I cleaned and sorted the original dataset and I used [Gbif API](https://www.gbif.org/es/developer/summary). 

![markus-spiske-vqU47hNXGE0-unsplash](/assets/markus-spiske-vqU47hNXGE0-unsplash.jpg)

For this proyect I used [Pandas dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.dayofweek.html), the Graphs library [Plotly](https://plotly.com/), Json library, and some relevant modules from python 3 such as the [requests module](https://pypi.org/project/requests/), sys and os, and argparse.

Finally I also created a program to ask the for each species and, as a result, obtain one of these at a time for each one of the most representative taxons of my dataset:
- Class
- Order
- Phylum	
- Exporter	
- Importer	
- Origin	
- Purpose
- Quantity

And species should be called as follows:

- Acipenser baerii
- Acipenser gueldenstaedtii
- Alligator mississippiensis
- Caiman crocodilus crocodilus
- Caiman crocodilus fuscus!
- Caiman crocodilus yacare
- Crocodylus niloticus
- Crocodylus novaeguineae
- Crocodylus porosus
- Elephantidae
- Falco rusticolus
- Hippopotamus amphibius
- Loxodonta africana
- Macaca fascicularis
- Psittacus erithacus
- Python bivittatus
- Python brongersmai
- Python reticulatus
- Salvator merianae
- Scleractinia
- Varanus niloticus
- Varanus salvator
- Vicugna vicugna

![nature-3066848_1920](/assets/nature-3066848_1920.jpg)

For a better understanding of the results, I add some basic information about the meaning of purpose and the source keywords of the outcome of the request

### PURPOSE

![Captura de pantalla 2020-06-22 a las 23.27.38](/assets/Captura%20de%20pantalla%202020-06-22%20a%20las%2023.27.38.png)

### SOURCE

![Captura de pantalla 2020-06-22 a las 23.27.28](/assets/Captura%20de%20pantalla%202020-06-22%20a%20las%2023.27.28_qzf41p5zo.png)

The main results from the analysis can be found in the final report

![african-4627563_1920](/assets/african-4627563_1920.jpg)