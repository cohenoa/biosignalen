# Oncosense package:

# 1. Installation #
Our program is compatible with Python 3 on Windows/Linux.
1. Install Python 3: https://www.python.org/download/releases/3.0/ 
2. Download freely available code from this repository.
3. Unzip the downloaded file. 
4. Rename the unzipped folder (optional): <CODE_FOLDER>, e.g., `“C:\oncosense\”`
5. Open the command line (Windows command: cmd) 
6. Go to the folder: `cd C:\oncosense\`
7. Run the following command (installation of necessary software components):
`pip install -r requirements.txt`

# 2. Execution #
## 2.1. Input folder preparation
Before executing the program, prepare an _input folder_ named `Data` within the `oncosense` folder, which will contain 
your input data files.
The format of the input file is an excel file (.xlsx suffix) containing two essential worksheets: 'G', 'L' and 'ErrorLimitLambda':
- In the 'G' worksheet, each row represents a protein: the “UID” column lists the protein name, and the subsequent columns contain the scores for each process (here, the surprisal‑analysis scores).
- In the 'L' worksheet, we see for each cell line the treatment details: compound added, mathcing dosage and time, followed by [TBD]
- The 'ErrorLimitLambda' worksheet contains a single value [TBD]

## 2.2. Running the program
In order to run the program, set the `data_name` variable in line 4 in the `main.py` file (e.g., 'Table1_myData97_demo') and execute the main.
The program will ask you to choose which cell lines should be included in the analysis by  For each cell line the 

## 2.3. Output
The program will automatically create an output folder names as the inupt file, containing the following information:
1. A folder names `G` containing:
   * The `edges.csv` file displays the top and bottom 10% of proteins (the "tails" in our analysis).
   * The `sort_G.csv` file displays all of the proteins, sorted by the G value
   * The `Graphs` folder contains an svg graph per process, showing all proteins sorted by their G value [TBD]
2. Several folders of cell line info:
   * Each folder [TBD]

# 3. Running Examples #
## 3.1. First Example
When running the program on the `Data\supp_data_26.xlsx` (see Supplementary Table 26) which contains data of a single cell line with five different treatments, we get the following two pop-up windows:<br/>
I. Select cell lines for the analysis:<br/>
![image](https://github.com/user-attachments/assets/46d69598-9e5a-4775-a971-80791ae1f349)<br/>
II. For each cell line selected in (I),select the control compounds in the left panel and the non‑control compounds in the right panel:<br/>
![image](https://github.com/user-attachments/assets/68f40fee-7db1-4c3b-affb-3e174d605b9f)

<br/>The resulting output folders are:<br/>
![image](https://github.com/user-attachments/assets/ea46ad38-785a-4a23-b660-3dc48372da11)


## 3.2. Second Example
### 3.2.1. Running the program:

When running the program on the `Data\supp_data_4.xlsx` (see Supplementary Table 4) which contains data of several single cell lines with five different treatments and 17 cell lines, we get the following two pop-up windows:<br/>

![image](https://github.com/user-attachments/assets/9598d1a6-990c-4f4c-809d-10df8c4b8331)<br/>

For all cell lines, select the control compounds in the left panel and the non‑control compounds in the right panel.<br/>
For example for PC3 we get: </br>
![image](https://github.com/user-attachments/assets/bd838533-8013-4527-b729-d873a8c3dfbd) </br>
and for MDAMB231HT we get: </br>

![image](https://github.com/user-attachments/assets/88ac89ad-4b5b-4624-b2f8-76ad120945ea) </br>

When using the default suggested by the tool for each cell line in this case, the resulting output folders are:<br/>
![image](https://github.com/user-attachments/assets/ef720b97-4fd2-4288-9b3c-137f333408c4)<br/>

### 3.2.1. Interpretation

For demonstration purposes, we focus on the PC3 cell line. In the output file PC3_AVG_by_time.csv, 10 processes are reported as being affected by the treatment (Processes 1, 2, 3, 4, 5, 8, 11, 12, 13, and 14). These effects are categorized as 'Sign change,' 'Emerging process,' or 'Disappearing process,' based on the corresponding values in the input data (only significant changes with p-value > 0.05 are reported).

More specifically, for example, Process 1 exhibits a sign change after 24 hours and is classified as an emerging process after 48 hours. In contrast, Process 12 is identified as a disappearing process at both 24 and 48 hours.

<img src="https://github.com/user-attachments/assets/b75260d3-0323-47fb-bd7f-ce95c923a376" style="width:200%;"/>

![image](https://github.com/user-attachments/assets/b75260d3-0323-47fb-bd7f-ce95c923a376)



































