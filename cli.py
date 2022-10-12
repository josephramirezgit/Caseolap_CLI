import argparse
import sys

def preprocessing(args):
    print(args)
    print("Preproccessing branch, still in development")
    
    ## TODO
    # flags: abbreviations, diseases, cellcomp, proteinlist, output folder, parameters, -s synonyms, -t synlist
    # Check arguments
    has_parameter_file = False #TODO
    if has_parameter_file:
        param_file_name = "TODO" #TODO
        parameters = parse_parameters_file(param_file_name)
    else:
        parameters = {}
        # TODO
        # parse input files
        abbreviations = parse_abbreviations(args.abbreviations) #TODO make these functions, args.abbrev might not be right
        diseases = parse_diseases(args.diseases) # TODO same as above, also need to check against MeSH tree, if it is valid input
        cellular_component = parse_subcellular_component(args.cell_comp) #TODO same, need to check against GO terms to see if it is valid input
        protein_list = parse_protein_list(args.proteinlist) #TODO
        
        # TODO synonym list for proteins

        # TODO check if output folder is valid, otherwise create the folder

    # Run the proprocessing module
    print("TODO running preprocessing module")
    return

def textmining(args):
    print(args)
    print("Textmining branch, still in development")

    # flags: date range, full-text flag (boolean), impute-labels (boolean), parameters file, 
    # TODO add: input-folder from previous step; OR list of proteins and diseases from prev step.

    # Check arguments
    ## TODO same as above

    date_from,date_to = args.date_range # TODO or something like that
    if check_date(date_from) and check_date(date_to):
        pass
    else:
        # throw exception
        print("Invalid date")

    return

def analysis(args):
    print(args)
    print("Analysis branch, still in development")
    # TODO add: path to input-folder from previous step; OR add knowledge graph edges
    return

def check_date(date):
    # Checks to see if date a valid input.
    # TODO
    return

def check_file(file_name):
    # Checks to see if input file is valid.
    # TODO
    return

def parse_parameters_file(file_name):
    # User provided input as a parameter file.
    is_valid = check_file(file_name)

    if is_valid:
        print("Parsing parameter file")
        #TODO read parameters (as a json or a text field, TBD).
        parameters = {}
        return parameters
    else:
        #TODO throw an error, tell user the parameter file is invalid.
        print("Error")

class MyParser(argparse.ArgumentParser):
   def error(self, message):
      sys.stderr.write('error: %s\n' % message)
      self.print_help()
      sys.exit(2)

def args_parser():
    ## TODO implement sub-parsers 
    
    '''
    TODO: implement sub-parsers. See 'login' vs 'register' in the link below. Three subparsers needed: 
    source: https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
    '''
    
    # Create a description for the CLI
    DESCRIPTION = ("There are three components to the CaseOLAP LIFT pipeline which must be performed in order\n" 
    "preprocessing      Prepare diseases and proteins of interest\n" 
    "text_mining        Perform text mining analysis\n" 
    "kg_analysis        Analyze the knowledge graph help\n")
    
    # Create parser object
    parser = MyParser()
    #parser = argparse.ArgumentParser(description = DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
    
    # Add preprocess flags
    parser.add_argument('-a abrv', '--abbreviations abrv', type = str, help = "Abbreviations for diseases")
    parser.add_argument('-d diseases', '--disease_list', type = list, help = "List of diseases of interest")
    parser.add_argument('-c cell_comp', '--subcellular_component cell_comp', type = str, help = "Subcellular component of interest")
    parser.add_argument('-l protein_list', '--protein_list', type = str, help = "Include a custom list of proteins of interest")
    # unsure if this is rigth since there are a lot of spaces in the argument
    parser.add_argument('-o output folder', type = str, help = 'Output directory to program results') 
    parser.add_argument('-p parameters parameters.txt', type = str, help = 'Input .json or .txt file specifying parameters to run')
    ##TODO actually, this should not have 'boolean', it should be a flag only. Same for all boolean (-f,-i)
    parser.add_argument('-s boolean', '--synonyms boolean', type = str, help = 'Include synonyms for proteins')
    parser.add_argument('-t synonyms_list', '--synonym_list synonym_list', type = list, help = 'Include a custom list of protein synonyms')
    
    # Add text mining flags
    parser.add_argument('-d date_start', '--date_range date_start date_end', type = str, help = 'Specify the date range for PubMed documents which will be downloaded')
    parser.add_argument('-f boolean', '--full_text boolean', type = bool, help = 'Specify to use full-text in text mining analysis or not')
    parser.add_argument('-i boolean', '--impute_labels boolean', type = bool, help = 'Whether to impute missing labels on text')
    
    return parser

def main():

    # Set up argument parsing
    parser = args_parser()
    args = parser.parse_args()
    print(args)
    
    # Print help if no arguments given 
    if len(sys.argv) < 2:
        parser.error("Incorrect usage.")
        sys.exit(0)
    
    # Execute sub-branches of program depending on command
    command = args.command 
    if command == 'preprocessing':
        preprocessing(args)
    elif command == 'text_mining':
        textmining(args)
    elif command =='analysis':
        analysis(args)
    else:
        parser.error("Mode not found: %s"%sys.argv)
        sys.exit(0)

if __name__ == "__main__":
    main()
