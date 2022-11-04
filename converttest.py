import json

class FileConversion:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def json_to_txt(self):
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

    def txt_to_json(self):
        # open the txt file
        text = open(self.input_file)
        lines = text.readlines()

        # determine keys
        keys = {}
        for line in lines:
            key = line.split(":")[0]
            if key in keys:
                keys[key] += 1
            else:
                keys[key] = 1

        # save res as dict to be transformed into json
        res = {}

        idx = 0
        for k, v in keys.items():
            # if there is more than one apperance of a key, we need to make a list of lists
            if v > 1:
                items = []
                i = 0
                while i < v:
                    list_text = lines[idx].split(":")[1].split(" ")
                    items.append(list_text)
                    i += 1
                    idx += 1
                res[k] = items
            else:
                # if v = 1, then we just need to append whatever is there
                res[k] = lines[idx].split(":")[1]
                idx += 1
        
        # write to files
        with open(self.output_file, "w") as outfile:
            json.dump(res, outfile)

        # close files
        text.close()
        outfile.close()
        
