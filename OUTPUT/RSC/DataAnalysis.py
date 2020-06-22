# Analysing the df
import pandas as pd

citescompleted = pd.read_csv("output/citescompleted.csv")

def identif(col):
    for i in col:
        return i


def maxcount(col):
    return col.value_counts().idxmax()


speciesInformation = citescompleted.groupby(by="Taxon").agg(Class=("Class", identif), Order = ("order", identif),Phylum = ("phylum", identif), Exporter=("Exporter",maxcount), Importer = ("Importer", maxcount), Origin = ("Purpose", maxcount), Purpose =("Purpose", maxcount), Qty=("Taxon", "count"))

def user_request(species,information):
    result = speciesInformation[speciesInformation.index==f"{species}"]
    if information == "Class":
        Class = list(result["Class"])
        return f"{species} belongs to the " + Class[-1] + " class"
    if information == "Order":
        Order = list(result["Order"])
        return f"{species} belongs to the " + Order[-1] + " order"
    if information == "Phylum":
        Phylum = f"{species} belongs to the" + Phylum[-1] + "phylum"
        return result["Phylum"]
    if information == "Exporter":
        Exporter = result["Exporter"]
        return f"The country that mostly exports {species} is " + Exporter[-1]
    if information == "Importer":
        Importer = list(result["Importer"])
        return f"The country that mostly imports {species} is " + Importer[-1]
    if information == "Purpose":
        Purpose = list(result["Purpose"])
        return 'The purpose of the trade is mainly for ' + Purpose[-1] + " purposes(go to Report or help for further information)"
    if information == "Quantity":
        Qty = list(result["Qty"])
        return f'The trades for {species} sums ' + str(Qty)
    
