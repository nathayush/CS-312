import itertools
import time
class Data_Match:
    def __init__(self,fragment_data):
        import itertools
        self.matches = []
        self.data = open("data.txt","r").read().split("\n\n")
        for fragment in fragment_data:
            self.check_fragment(fragment)
        self.unique_match()
    def unique_match(self):
        new_matches = []
        match_var = []
        for match in self.matches:
            if match[1] not in match_var:
                new_matches.append(match)
                match_var.append(match[1])
        self.matches = new_matches
            
            
    def check_fragment(self,fragment):
        def check_data(code,input_list,output_val):
            outputlist = []
            input_variables = ["x","y","z"]
            output = None
            for i,input_value in enumerate(input_list):
                exec(input_variables[i]+" = "+input_value)
            if code[0] == "x":
                try:
                    output = eval(code)
                    if output == None:
                        output = eval("x")
                except:
                    return(False)
            else:
                try:
                    output = eval(code)
                except:
                    return(False)
            if str(output_val) == str(output):
#                input(output)
#                input(output_val)
                t2_start = time.perf_counter()
                output = eval(code)
                t2_stop = time.perf_counter()
                time_taken = t2_stop-t2_start
                return(time_taken)
            else:
                return(False)
        
        for code in self.data:
#            print(fragment.output_val[0])
            try:
                result = check_data(code,fragment.input_val,fragment.output_val[0])
                if result != False:
                    self.matches.append([fragment,code,result])
                elif fragment.optional_input != []:
                    result = check_data(code,fragment.input_val+fragment.optional_input,fragment.output_val[0])
                    if result != False:
                        self.matches.append([fragment,code,result])
            except:
                continue