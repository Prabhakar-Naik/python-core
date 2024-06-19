import json

def convert_json_to_csv():
    try:
        with open('input.json','r') as file:
            data = json.loads(file.read())
            
            output = ",".join([*data[0]])
            
            for obj in data:
                output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open('output.csv', 'w') as f:
            f.write(output)
            print("your csv file filled with data take a look.")
    except Exception as ex:
        print(f'Error: {str(ex)}')
        

if __name__ == '__main__':
    convert_json_to_csv()