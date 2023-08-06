# BBC articles to .epub converter

## General info
Simple converter to create .epub file from list of links to BBC articles, useful for language learning purposes.
Tested on most [languages](https://www.bbc.co.uk/ws/languages) but not compatible with english.
Support for both left-to-right and right-to-left languages.

## Installation
Make sure you have python 3.10+ installed

### Clone repository

```
git clone https://github.com/Pawix5k/BBC-to-epub.git
```

### Create virtual environment.

```
python -m venv venv
```
or
```
python3 -m venv venv
```

### Activate virtual environment
```
venv/Scripts/activate
```

### Install dependencies.

```
python -m pip install -r requirements.txt
```
or
```
python3 -m pip install -r requirements.txt
```

## Usage

### Change first line of user_input.txt to desired file name and paste links to articles in subsequent lines.
```
bbc-articles
https://www.bbc.com/somelang/someid
https://www.bbc.com/somelang/articles/otherid
```
### Run the script.
```
python main.py
```
or
```
python3 main.py
```

## Examples
![screenshot_2023_08_05T23_31_33+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/5a20dd03-dee6-4879-a443-3d57bc5ccf09)
![screenshot_2023_08_05T23_39_17+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/be875d3c-d1dd-4975-b75a-8c8f7cbe3b99)
![screenshot_2023_08_05T23_31_14+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/1b05f460-f469-4b1d-95aa-96de88d75908)
![screenshot_2023_08_05T23_34_12+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/03d186cd-eb34-46e9-8218-5ed3c6481de5)
![screenshot_2023_08_05T23_33_53+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/540e97cb-21e9-4d30-9050-a4a7653832c7)
