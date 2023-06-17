import pandas as pd
import json

def ConvertFileFormat(option1, csv_file, option2, output_file):
    # Read the CSV file
    if option1 == 1:
        data = pd.read_csv(csv_file)
    elif option1 == 2:
        data = pd.read_excel(csv_file)
    else: 
        print("No options input")
    #print (data)
    #Concatenate the input columns with a separator, if necessary
    data['prompt'] = data['prompt'].astype(str)

    data['completion'] = data['completion'].astype(str)

    # Rename the output column
    # data = data.rename(columns={"column3": "completion"})

    # Select only the prompt and completion columns
    data = data[['prompt', 'completion']]

    # Convert the DataFrame to a list of dictionaries
    data_list = data.to_dict("records")
    if option2 == 1:
        data.to_csv(output_file, index=False)
    elif option2 == 2:
        data.to_json(output_file, orient='records', lines=True)
    else:
        print("No options input")
    # Save the list of dictionaries as a csv file / jsonl :::: Line 25 for csv, Line 26 to jsonl
    #data.to_csv("FAQ.csv", index=False)
    #data.to_json("carInsuranceInfo_Merged.jsonl", orient='records', lines=True)

def csv_to_gpt3_json_format(csv_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)
    #data = pd.read_excel(csv_file)
    # Concatenate the input columns with a separator, if necessary
    data['prompt'] = "My Car " + data['make'].astype(str) + " model " + data['model'].astype(str)  + " year " + data['year'].astype(str) + ' ncd ' + data['ncd'].astype(str) + ", how much would my car insurance be?"

    data['completion'] = "Your car insurance for Promilej 5000km it would be " + data['promilej 5000km'].astype(str) + " and for comprehensive it would be " + data['comprehensive'].astype(str)

    # Rename the output column
    # data = data.rename(columns={"column3": "completion"})

    # Select only the prompt and completion columns
    data = data[['prompt', 'completion']]

    # Convert the DataFrame to a list of dictionaries
    data_list = data.to_dict("records")

    # Save the list of dictionaries as a csv file
    data.to_csv("carInsuranceInfo.csv", index=False)
    #data.to_json("carInsuranceInfo.jsonl", orient='records', lines=True)

def merged_csv(file1, file2):
    files = [file1, file2]
    df = pd.DataFrame()
    for file in files:
        data = pd.read_csv(file)
        df = pd.concat([df, data], axis=0)
    df.to_csv('carInsuranceInfo_Merged.csv', index=False)


if __name__ == "__main__":

    # 1. Convert test data to csv
    test_csv_file = "testData.csv"  # Replace with your input CSV file
    #test_csv_file = "C:/Users/duxton.lim/OneDrive - P & O Global Technologies Sdn. Bhd/Documents/Python Code/Chatgpt_RnD/testData.csv"
    
    csv_to_gpt3_json_format(test_csv_file)

    # 2. Convert excel to csv 
    input_csv_file = "ProMilegFAQ.xlsx"  # Replace with your input CSV file
    #input_csv_file = "C:/Users/duxton.lim/OneDrive - P & O Global Technologies Sdn. Bhd/Documents/Python Code/Chatgpt_RnD/ProMilegFAQ.xlsx"
    ConvertFileFormat(2,input_csv_file,1,"PromilejFAQ.csv")
    
    # 3. Merge both csv file
    file1 = "PromilejFAQ.csv"
    file2 = "carInsuranceInfo.csv"
    #file1 = "C:/Users/duxton.lim/OneDrive - P & O Global Technologies Sdn. Bhd/Documents/Python Code/PromilejFAQ.csv"
    #file2 = "C:/Users/duxton.lim/OneDrive - P & O Global Technologies Sdn. Bhd/Documents/Python Code/carInsuranceInfo.csv"
    merged_csv(file1,file2)

    # 4. Convert merged csv file to jsonl
    file3 = "carInsuranceInfo_Merged.csv"
    file4 = "carInsuranceInfo_Merged.jsonl"
    #file3 = "C:/Users/duxton.lim/OneDrive - P & O Global Technologies Sdn. Bhd/Documents/Python Code/carInsuranceInfo_Merged.csv"
    #file4 = "C:/Users/duxton.lim/OneDrive - P & O Global Technologies Sdn. Bhd/Documents/Python Code/Chatgpt_RnD/carInsuranceInfo_Merged.jsonl"
    ConvertFileFormat(1,file3,2,file4)
