from spacy.matcher import PhraseMatcher
import csv
import os

def load_analytes(file_name):
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, file_name)

    with open(path, 'r') as f:
        reader = csv.reader(f)
        metabolites = list(reader)
    return [item[0].lower() for item in metabolites]

def createMatcher(nlp, analyte_list):
    analyte_matcher = PhraseMatcher(nlp.vocab)
    analyte_matcher.add('analytes', [nlp(item) for item in analyte_list])
    return analyte_matcher

def get_analytes(text, analyte_matcher):
    analytes = analyte_matcher(text)
    potential_analytes = []
    for match_id, start, end in analytes:
        potential_analytes.append(text[start:end])
    return potential_analytes