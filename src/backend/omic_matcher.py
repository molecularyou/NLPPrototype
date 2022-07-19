from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
import csv
import os

def load_metabolites(file_name):
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, file_name)

    with open(path, 'r') as f:
        reader = csv.reader(f)
        metabolites = list(reader)
    return [item[0].lower() for item in metabolites]

def createMetaboliteMatcher(nlp, metabolite_list):
    analyte_matcher = PhraseMatcher(nlp.vocab)
    analyte_matcher.add('analytes', [nlp(item) for item in metabolite_list])
    return analyte_matcher

def get_omics(nlp, text, metabolite_matcher):
    omic_matcher = Matcher(nlp.vocab)
    metabolomics = [{"LEMMA": {"IN": ["metabolomics", "metabolic", "metabolite"]}}]
    proteomics = [{"LEMMA": {"IN": ["proteomic", "protein"]}}]
    genomics = [{"LEMMA": {"IN": ["genomic", "genome", "gene"]}}]
    microbiomics = [{"LEMMA": {"IN": ["microbiomic", "microbiome", "bacterium", "fungus", "virus"]}}]
    multiomics = [{"LEMMA": {"IN": ["multiomic"]}}]
    
    omic_matcher.add('metabolomics', [metabolomics])
    omic_matcher.add('proteomics', [proteomics])
    omic_matcher.add('genomics', [genomics])
    omic_matcher.add('microbiomics', [microbiomics])
    omic_matcher.add('multiomics', [multiomics])
 
    omics = omic_matcher(text)
    analytes = metabolite_matcher(text)
    potential_omics = []
    for match_id, start, end in omics:
        potential_omics.append(text[start:end])
    for match_id, start, end in analytes:
        potential_omics.append(text[start:end])
    return potential_omics