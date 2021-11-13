# AV_api_for_scanning_folders_fastapi

REST API application scans a folder with all subfolders and text files and provides aggregate statistics for certain indicators.<br>

### Basic functionality:<br>
1.Web REST API<br>
2.For a start application scans DIR (base directory) with all subfolders and text files<br>
3.Information for REST API:<br>
  -List of folders and files<br>
	-Count of files<br>
	-Names_of files<br>
	-The most common word<br>
	-The rarest word<br>
	-Average length of words<br>
	-Count of vowels/consonants/syllables<br>
4.For each file or word you can use RESR API request: 	/api/file/readable-file-id 
5.You can use this app English and Russian words

### Stack of technologies:<br>
-Python >= 3.9<br>
-FastApi<br>
-linter: Black<br>


### APIs endpoints:<br>
| requests | url | description  |
| ------- | --- | --- |
| GET | /folder/ | folder information |
| GET | /file/{filename}/ | file information |
| GET | /word/{word}/ | one word information |


## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/AV_api_for_scanning_folders_fastapi <br>
$ cd AV_api_for_scanning_folders_fastapi<br>

### Create virtualenv:<br>
$ virtualenv venv<br>
$ source venv/bin/activate<br>

### Dependency:
$ pip install -r requirements.txt<br>

### Run the sample server:<br>
$ uvicorn app.main:app --reload <br>

### Tests: <br>
$pytest


### API from the browser:
You can work on the API directly in your browser.<br>
You will see the automatic interactive API documentation (provided by Swagger UI).
http://127.0.0.1:8000/docs <br>


### Examples:<br>

![Screenshot](https://github.com/SparklingAcidity/AV_api_for_scanning_folders_fastapi/blob/main/img_for_readme/1.png) <br>
![Screenshot](https://github.com/SparklingAcidity/AV_api_for_scanning_folders_fastapi/blob/main/img_for_readme/2.png)<br><br>
