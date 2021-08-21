import json

annotations = []

#Read in the badly formatted logs
def getLineAndColumnNumbers(split_line):
    start_bracket = split_line[0].index('(')
    end_bracket = split_line[0].index(')')

    line_numbers = split_line[0][start_bracket+1:end_bracket]

    line_column_split = line_numbers.split(',')
    line_start_end = line_column_split[0]
    column_start_end = line_column_split[1]
    return line_start_end,column_start_end

def getPath(split_line, line_start_end, column_start_end):
    # Remove line numbers
    path = split_line[0].strip("("+line_start_end+","+column_start_end+")")
    # Remove whitespace
    path = path.strip()
    return path


with open('report/linters_logs/ERROR-CSHARP_DOTNET_FORMAT.log',encoding="utf8") as file:
    for line in file:
        
        split_line = line.split(':')
        if(len(split_line) != 3):
            continue
        
        #Do Something 
        print (line)

        #We now definitely have an actual log line we care about 

        line_start_end, column_start_end = getLineAndColumnNumbers(split_line)
        
        path = getPath(split_line, line_start_end, column_start_end)
        
        message = split_line[2]

        severity = split_line[1].strip().split(" ")[0]
        
        if(severity == "error"):
            severity = "failure"
        

        annotations.append({"title":"CSharp Linter","message":message,"file":path,"line": int(line_start_end),"annotation_level":severity})


#Dump Json
with open("annotations.json", "w") as annotations_file:
    my_json_object = json.dump(annotations, annotations_file)