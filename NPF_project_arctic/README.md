# NPF_project_arctic
Documentation for the folder

This document provides detailed documentation about the code and file management in the folder 'NPF_project_arctic'. Please read carefully before making any changes to the folder system/codes.

1. Folder system
- Folders in 'NPF_project_arctic' are split into multiple groups based on their functions. There are 3 types of folders: 1) ML algorithm folders, 2) data preprocessing/table making code folders, and 3) image storage.

1.1. ML algorithm folders
- ML algorithm folders function as a separate units not dependant on each other or other folders. Most codes are stored in the form of ipynb files. Input data is stored in the form of .csv file in each folder, and is called 'output_combined'.

- Note: if new input data is obtained, please replace 'output_combined' file in each folder. 
- Note: if new data is obtained, make sure that column names are have exactly the same names as 'output_combined' file. Order of columns is not important. 
- Note: make sure that data in 'day.type' column is 'Non', 'undefined', and 'NPF'.

- '{model name}_tuned_norm' file hold information about trained model results on raw data (so called as-it-is input). 
- '{model name}_tuned_smote' file hold information about trained model results on modified data (with usage of SMOTE, check https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html for more details).

- All result files are stored locally in the folder.

1.2. Data preprocessing/table making code folders
- Data preprocessing codes are stored in 'in_progress' folder. IMPORTANT: 'output_combined_maker' file takes raw data from previously available .csv files and repacks them into 'output_combined'. The flow of code is difficult to follow, and raw imput data is missing. Raw files are available in 'ATML_NAS/students/Aslan'. For your input data, you might need to change 'output_combined_maker' significantly.
- Table and figure making codes are stored in 'in_progress' and 'tables' folders. Note: files in 'in_progress' folder require precise adress of input file, make sure to set input adresses properly. Files in 'tables' folder are in .ipynb format, and do not depend on other folders. Note: all results need to be typed in manually.

1.4 Image storage
- All images from 'in_progress' file are stored in 'png' folder. DO NOT change the name of the folder.

2. Author notes
2.1. Github
- I recommend you to use github and gitbash for keeping track of your files. Gitbash would allow you to see the changes in your code over time. Github would allow you to retrieve old versions of your codes in case needed. Also, it would be easier to keep track of your work progress through github. In order to do so, create github repositories, and set that repository as a remote in gitbash terminal. More detailed guides can be found on https://stackoverflow.com/questions/42830557/git-remote-add-origin-vs-remote-set-url-origin and https://www.youtube.com/watch?v=tRZGeaHPoaw&t=266s&ab_channel=KevinStratvert.

2.2. Documentations
- Before makign any changes to functions, I recommend you to read the documentation about each specific function used. Documentations for most functions can be found on https://scikit-learn.org/stable/. 

2.3. Error handling
- For handling of verious errors, I recommend to check https://stackoverflow.com/. In case of specific error in terminal/logs, run codes in sections. 
- Common errors: data type mismatch (expected 'int', recieved 'datetime', etc), missing/altered input (column/row indexes, dataframe size mismatch), and wrong import/export adresses (wrong file/folder name).
- Python and libraries version mismatch is also one of the common issues. For this project, python 3.10.13 was used. Check logs/terminal for warnings/errors. If encountered, make sure to change function parameter input to resolve the warning/error.

2.4. Chat GPT
- Usage of Chat GPT is acceptable, however, make sure you understand the code propperly. Usually Chat GPT assumes certain data type, which might be different from your data type. Make sure the code is readable, and write documentation for each code.

2.5. 