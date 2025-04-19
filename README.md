# Oncosense package:

## 1. Installation ##
Our program is compatible with Python 3 on Windows/Linux.
1. Install Python 3: https://www.python.org/download/releases/3.0/ 
2. Download freely available code from this repository.
3. Unzip the downloaded file. 
4. Rename the unzipped folder (optional): <CODE_FOLDER>, e.g., `“C:\OncosenseSoftware\”`
5. Open the command line (Windows command: cmd) 
6. Go to the folder: `cd C:\OncosenseSoftware\`
7. Run the following command (installation of necessary software components):
`pip install -r requirements.txt`

## 2. Execution ##
### 2.1 Input folder preparation
Before executing the program, prepare an _input folder_ named `Data` within the `OncosenseSoftware` folder, which will contain 
your input data files.

### 2.2

### 2.3 Output
The program will automatically create an output folder names as the inupt file, containing the following information:
1. A folder names `G` containing:
   a. The `edges.csv` file displays the top and bottom 10% of proteins (the "tails" in our analysis).
   b. The `sort_G.csv` file displays all of the proteins, sorted by the G value
   c. The `Graphs` folder
3. Folders with cell line info [TBD]
