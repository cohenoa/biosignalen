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
Before executing the program, prepare an _input folder_ named `Data` within the `OncosenseSoftware` folder, which will contain 
your input data files.
The format of the input file is as follows: [TBD - Gil]
### 2.2 Running the program
[TBD - Noa]

### 2.3 Output
The program will automatically create an output folder names as the inupt file, containing the following information:
1. A folder names `G` containing:
   * The `edges.csv` file displays the top and bottom 10% of proteins (the "tails" in our analysis).
   * The `sort_G.csv` file displays all of the proteins, sorted by the G value
   * The `Graphs` folder contains an svg graph per process, showing all proteins sorted by their G value [TBD - Gil]
2. Several folders of cell line info:
   * Each folder [TBD - Gil]

## 3. Running Example ##
For example, when running the program on the `Data\Table1_myData38.xlsx` file, we get the following output folders:

