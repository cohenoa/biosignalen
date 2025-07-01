# Oncosense package:

## 1. Installation ##
Our program is compatible with Python 3 on Windows/Linux.
1. Install Python 3: https://www.python.org/download/releases/3.0/ 
2. Download freely available code from this repository.
3. Unzip the downloaded file. 
4. Rename the unzipped folder (optional): <CODE_FOLDER>, e.g., `“C:\oncosense\”`
5. Open the command line (Windows command: cmd) 
6. Go to the folder: `cd C:\oncosense\`
7. Run the following command (installation of necessary software components):
`pip install -r requirements.txt`

## 2. Execution ##
### 2.1 Input folder preparation
Before executing the program, prepare an _input folder_ named `Data` within the `oncosense` folder, which will contain 
your input data files.
The format of the input file is an excel file (.xlsx suffix) containing two essential worksheets: 'G', 'L' and 'ErrorLimitLambda':
- In the 'G' worksheet, each row represents a protein: the “UID” column lists the protein name, and the subsequent columns contain the scores for each process (here, the surprisal‑analysis scores).
- In the 'L' worksheet, we see for each cell line the treatment details: compound added, mathcing dosage and time, followed by [TBD]
- The 'ErrorLimitLambda' worksheet contains a single value [TBD]
### 2.2 Running the program
In order to run the program, set the `data_name` variable in line 4 in the `main.py` file (e.g., 'Table1_myData97_demo') and execute the main.
The program will ask you to choose which cell lines should be included in the analysis by  For each cell line the 

### 2.3 Output
The program will automatically create an output folder names as the inupt file, containing the following information:
1. A folder names `G` containing:
   * The `edges.csv` file displays the top and bottom 10% of proteins (the "tails" in our analysis).
   * The `sort_G.csv` file displays all of the proteins, sorted by the G value
   * The `Graphs` folder contains an svg graph per process, showing all proteins sorted by their G value [TBD]
2. Several folders of cell line info:
   * Each folder [TBD]

## 3. Running Example ##
### 3.1 First Example
When running the program on the `Data\Table1_myData97_demo.xlsx` (see Supplementary Table 26) which contains data of a single cell line with five different treatments, we get the following two pop-up windows:<br/>
<b>I. Select cell lines for the analysis:<b/><br/>
![image](https://github.com/user-attachments/assets/46d69598-9e5a-4775-a971-80791ae1f349)
<br/><b>II. For each cell line selected in (I),select the control compounds in the left panel and the non‑control compounds in the right panel:<b/><br/>
![image](https://github.com/user-attachments/assets/68f40fee-7db1-4c3b-affb-3e174d605b9f)

<br/>The resulting output folders are:<br/>
![image](https://github.com/user-attachments/assets/eabeb1da-dba8-4967-b47d-0fc5450e6fb5)

### 3.2 Second Example
When running the program on the `Data\supp_data_4.xlsx` (see Supplementary Table 4) which contains data of several single cell lines with five different treatments, we get the following two pop-up windows:<br/>

![image](https://github.com/user-attachments/assets/33431c72-6d22-4260-97d1-9ec79ef202a6)

<b>I. Select only the "pc3" cell line for the analysis:<b/><br/>
![image](https://github.com/user-attachments/assets/5eba478f-c062-48a8-be44-dffdaf010ba0)


<br/><b>II. For the selected cell line,select the control compounds in the left panel and the non‑control compounds in the right panel:<b/><br/>
![image](https://github.com/user-attachments/assets/bd838533-8013-4527-b729-d873a8c3dfbd)

<br/>The resulting output folders are:<br/>
![image](https://github.com/user-attachments/assets/54f75e6f-244d-4c32-979b-e0e4f7f48373)

































