import argparse

# Create a description for the CLI
DESCRIPTION = ("There are three components to the CaseOLAP LIFT pipeline which must be performed in order\n" 
"preprocessing      Prepare diseases and proteins of interest\n" 
"text_mining        Perform text mining analysis\n" 
"kg_analysis        Analyze the knowledge graph help\n")

# Create parser object
parser = argparse.ArgumentParser(description = DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)

# Add preprocess flags
parser.add_argument('-a abrv', '--abbreviations abrv', type = str, help = "Abbreviations for diseases")
parser.add_argument('-d diseases', '--disease_list', type = list, help = "List of diseases of interest")
parser.add_argument('-c cell_comp', '--subcellular_component cell_comp', type = str, help = "Subcellular component of interest")
parser.add_argument('-l protein_list', '--protein_list', type = str, help = "Include a custom list of proteins of interest")
# unsure if this is rigth since there are a lot of spaces in the argument
parser.add_argument('-o output folder', type = str, help = 'Output directory to program results') 
parser.add_argument('-p parameters parameters.txt', type = str, help = 'Input .json or .txt file specifying parameters to run')
parser.add_argument('-s boolean', '--synonyms boolean', type = str, help = 'Include synonyms for proteins')
parser.add_argument('-t synonyms_list', '--synonym_list synonym_list', type = list, help = 'Include a custom list of protein synonyms')

# Add text mining flags
parser.add_argument('-d date_start', '--date_range date_start date_end', type = str, help = 'Specify the date range for PubMed documents which will be downloaded')
parser.add_argument('-f boolean', '--full_text boolean', type = bool, help = 'Specify to use full-text in text mining analysis or not')
parser.add_argument('-i boolean', '--impute_labels boolean', type = bool, help = 'Whether to impute missing labels on text')

args = parser.parse_args()
