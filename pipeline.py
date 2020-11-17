"""
Ce code permet d'implementer un pipe de traitement de donnees
"""

# Import des packages
import pandas as pd
from nltk import word_tokenize
import json
import logging
import json


class DataPipeline():
    """
         Cette Classe a travers ses fonctions implemente toutes les etapes du pipeline de traitement des donnees a 
         savoir:  extraction >> traitement >> sauvegarde
    """

    def extraction(self, file_drug, file_pubmed, file_clinical_trial):
        """ Cette fonction permet d extraire les donnees des fichiers d input """
        logging.info("extraction des fichier input ...")
        data_drugs = pd.read_csv(file_drug, header=0, index_col=0)
        data_pubmed = pd.read_csv(file_pubmed, header=0)
        data_clinical_trial = pd.read_csv(file_clinical_trial, header=0)
        return data_drugs, data_pubmed, data_clinical_trial

    def traitement(self, data_drugs, data_pubmed, data_clinical_trial):
        """ Cette fonction permet d extraire les donnees extraits """
        # Traitement des donnees de drug
        result = {}
        for i in list(data_drugs['drug']):
            result[i] = []
        for drug in result.keys():
            # Traitement des donnees de pubmed
            for i in data_pubmed.index:
                list_data = [l.lower()
                             for l in word_tokenize(data_pubmed['title'][i])]
                if drug.lower() in list_data:
                    result[drug].append({'pubmed': data_pubmed['title'][i], 'journal': data_pubmed['journal'][i],
                                         'date_mention': data_pubmed['date'][i]})
            # Traitement des donnees clinical_trials
            for i in data_clinical_trial.index:
                list_data = [l.lower() for l in word_tokenize(
                    data_clinical_trial['scientific_title'][i])]
                if drug.lower() in list_data:
                    result[drug].append({'clinical_trials': data_clinical_trial['scientific_title'][i],
                                         'journal': data_clinical_trial['journal'][i], 'date_mention': data_clinical_trial['date'][i]})
        return result

    def sauvegarde(self, result):
        """ Cette fonction permet de creer le fichier des donnees au format JSON """

        with open('output/data.json', 'w', encoding='utf-8') as fp:
            json.dump(result, fp)


def feature_journal_maxdrug(file):
    """ Cette fonction permet d'extraire le le journal ayant le plus de médicaments différents """

    with open(file) as json_data:
        data_dict = json.load(json_data)
    result2 = []
    for key in data_dict.keys():
        data = []
        if data_dict[key] != []:
            for u in data_dict[key]:
                data.append(u['journal'])
                data = list(set(data))
            for u in data:
                result2.append(u)
    output1 = [u for u in result2]
    output2 = [result2.count(u) for u in result2]

    return output1[output2.index(max(output2))]


if __name__ == "__main__":
    data = DataPipeline()
    extract = data.extraction('input/drugs.csv', 'input/pubmed.csv',
                              'input/clinical_trials.csv')
    output = data.traitement(extract[0], extract[1], extract[2])
    data.sauvegarde(output)
    journal = feature_journal_maxdrug("output/data.json")
    print("le journal ayant cité le max de médicaments différents est :" + journal)
