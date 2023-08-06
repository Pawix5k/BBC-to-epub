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

![screenshot_2023_08_05T23_31_33+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/36ac7e11-bdc3-45ac-a861-a0f693e246ce)
![screenshot_2023_08_05T23_39_17+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/735a7b2b-78c8-46a9-809f-8f678ad6110b)
![screenshot_2023_08_05T23_31_14+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/907796a2-2206-46bc-9d3e-519683fcb5b9)
![screenshot_2023_08_05T23_34_12+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/7f57b437-c645-4c6b-b705-8425f809d812)
![screenshot_2023_08_05T23_33_53+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/3369c330-5e0e-4c85-8d9e-fd56187fd0b2)
![screenshot_2023_08_06T13_12_51+0200](https://github.com/Pawix5k/BBC-to-epub/assets/35242389/c28ac1fb-0a14-46c9-9936-523aaa7575d1)


