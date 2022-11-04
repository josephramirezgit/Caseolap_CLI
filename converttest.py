import pandas as pd
import json

class FileConversion:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    def json_to_text(self):
        # open the json file
        json_file = open(self.input_file, 'r')
        json_data = json.load(json_file)

        # open the txt file
        text_file = open(self.output_file, 'w')

        # write to text file
        for k, v in json_data.items():
            if type(v) == list:
                # for list of lists, handle all lists seperately
                if type(v[0]) == list:
                    for list_idx in range(len(v)):
                        list_text = " ".join(v[list_idx])
                        text = "{key}: {value}\n".format(key = k, value = list_text)
                        text_file.write(text)
                # if it is not a list of lists, just print all contents out normally
                else:
                    # handle lists of type int seperately 
                    if type(v[0]) == int:
                        list_text = " ".join(map(str, v))
                    else:
                        list_text = " ".join(str(v))
                    text = "{key}: {value}\n".format(key = k, value = list_text)
                    text_file.write(text)
            # if the type is not a list, then just print out the values
            else:
                text = "{key}: {value}\n".format(key = k, value = v)
                text_file.write(text)
        
        json_file.close()
        text_file.close()

def main():
    input_file = input("Enter input file name: ")
    output_file = input("Enter output file name: ")

    f = FileConversion(input_file, output_file)
    f.json_to_text()

if __name__ == "__main__":
    main()
    print("Process completed")