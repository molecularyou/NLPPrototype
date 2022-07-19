from flask import Flask, jsonify
from flask import request
from Bio import Entrez
from spacy.matcher import Matcher
from spacy.tokenizer import Tokenizer
import spacy
from spacy.util import compile_infix_regex
from age_matcher import get_age
from analyte_matcher import load_analytes
from analyte_matcher import get_analytes
from analyte_matcher import createMatcher
from omic_matcher import createMetaboliteMatcher
from control_group_matcher import get_control_groups, get_healthy_control_groups
from fluid_matcher import get_fluids
from n_matcher import get_n
from omic_matcher import get_omics, load_metabolites
from sex_matcher import get_sexes

nlp = spacy.load("en_core_web_trf")

# def custom_tokenizer(nlp):
#     inf = list(nlp.Defaults.infixes)               # Default infixes
#     inf.remove(r"(?<=[0-9])[+\-\*^](?=[0-9-])")    # Remove the generic op between numbers or between a number and a -
#     inf = tuple(inf)                               # Convert inf to tuple
#     infixes = inf + tuple([r"(?<=[0-9])[+*^](?=[0-9-])", r"(?<=[0-9])-(?=-)"])  # Add the removed rule after subtracting (?<=[0-9])-(?=[0-9]) pattern
#     infixes = [x for x in infixes if '-|–|—|--|---|——|~' not in x] # Remove - between letters rule
#     infix_re = compile_infix_regex(infixes)

#     return Tokenizer(nlp.vocab, prefix_search=nlp.tokenizer.prefix_search,
#                                 suffix_search=nlp.tokenizer.suffix_search,
#                                 infix_finditer=infix_re.finditer,
#                                 token_match=nlp.tokenizer.token_match,
#                                 rules=nlp.Defaults.tokenizer_exceptions)
# nlp.tokenizer = custom_tokenizer(nlp)


email = ''
metabolite_list = load_metabolites('metabolites.csv')
analyte_list = load_analytes('analytes.csv')
anaylte_matcher = createMatcher(nlp, analyte_list)
metabolite_matcher = createMetaboliteMatcher(nlp, metabolite_list)

app = Flask(__name__)

@app.route('/paper')
def papers():
    doi = request.args.get('doi')
    Entrez.email = email
    handle = Entrez.elink(dbfrom="pubmed", db="pmc", linkname="pubmed_pmc", id=doi, retmode="xml")
    id_return = Entrez.read(handle)
    handle.close()
    handle = Entrez.efetch(db="pmc", id=id_return[0]['LinkSetDb'][0]['Link'][0]['Id']) 
    records = handle.read()
    handle.close()
    results = []
    text = nlp(records.decode("utf-8").replace('\n', ' '))
    potential_n = get_n(nlp, text)
    potential_sexes = get_sexes(nlp, text)
    potential_fluids = get_fluids(nlp, text)
    potential_omics = get_omics(nlp, text)
    potential_ages = get_age(nlp, text)
    potential_control_groups = get_control_groups(nlp, text)
    potential_healthy_control_groups = get_healthy_control_groups(nlp, text)
    potential_analytes = get_analytes(nlp, text, analyte_list)
    results.append(f'<b>input</b><br/>{text}<br/><b>possible sample sizes:</b><br/>{potential_n}<br/><b>possible sexes:</b><br/>{set(potential_sexes)}<br/><b>possible ages:</b><br/>{set(potential_ages)}<br/><b>possible fluids:</b><br/>{set(potential_fluids)}<br/><b>possible omics:</b><br/>{set(potential_omics)}<br/><b>possible control group:</b><br/>{potential_control_groups}<br/><b>possible healthy control group:</b><br/>{potential_healthy_control_groups}')
    return '<br/>'.join(results)

@app.route("/")
def entrance():
    doi = request.args.getlist('doi')
    abstract_dict = {}
    without_abstract = []
    Entrez.email = email
    handle = Entrez.efetch(db="pubmed", id=','.join(doi),rettype="xml", retmode="text") 
    records = Entrez.read(handle)
    for pubmed_article in records['PubmedArticle']:
        pmid = int(str(pubmed_article['MedlineCitation']['PMID']))
        article = pubmed_article['MedlineCitation']['Article']
        if 'Abstract' in article:
            abstract = ' '.join(article['Abstract']['AbstractText']).replace(',', '')
            abstract_dict[pmid] = abstract.encode("ascii", "ignore").decode()
        else:
            without_abstract.append(pmid)
    handle.close()
    results = []
    for key, abstract in abstract_dict.items():
        text = nlp(abstract)
        potential_n = get_n(nlp, text)
        potential_sexes = get_sexes(nlp, text)
        potential_fluids = get_fluids(nlp, text)
        potential_omics = get_omics(nlp, text, metabolite_matcher)
        potential_ages = get_age(nlp, text)
        potential_control_groups = get_control_groups(nlp, text)
        potential_healthy_control_groups = get_healthy_control_groups(nlp, text)
        potential_analytes = get_analytes(text, anaylte_matcher)
        results.append({'doi': key,'input': [t.text for t in text], 'size': [{
            'start':item.start, 'end': item.end} for item in potential_n], 
            'fluids':[{'start':item.start, 'end': item.end} for item in potential_fluids], 
            'sexes':[{'start':item.start, 'end': item.end} for item in potential_sexes], 
            'ages':[{'start':item.start, 'end': item.end} for item in potential_ages],
            'omics':[{'start':item.start, 'end': item.end} for item in potential_omics],
            'controlGroups': [{'start':item.start, 'end': item.end} for item in potential_control_groups],
            'healthyControlGroups': [{'start':item.start, 'end': item.end} for item in potential_healthy_control_groups],
            'analytes': [{'start':item.start, 'end': item.end} for item in potential_analytes]
            })
    if (len(abstract_dict.items()) > 0):
        response = jsonify(results)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    else:
        return '<p>no abstract</p>'


if __name__ == '__main__':
    print('loading')
    app.run(port=8080)