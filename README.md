# LightNotes
**WARNING**: This project is a work in progress

A note-taking system for project management based on little insights written in Python. 
<img src="./img/Captura de tela_2021-10-06_19-16-22.png">

## Requirements 
- Python 3.8 or more recent versions
- ttk-bootstrap - Collection of modern, flat themes inspired by Bootstrap for tkinter/ttk. (Read "Installation" section)
- ttf-symbola - Font for unicode symbols (recognize the emoji in the notes)

## Installation 
1. Clone the repository

```bash
git clone https://github.com/HicaroD/LightNotes.git && cd LightNotes
```

2. Install all required dependencies 

```bash
pip3 install -r requirements.txt
```

3. Install symbola fonts

Install the ttf-symbola font. The license for that font is very limited, that's why I can't host it right here. If you don't install it, you will not see any emoji in the notes timestamp (that's very optional, to be honest).

4. Execute the program 

```bash
cd src/ && python3.8 main.py
```

## Usage
You can create a new project note and add little notes as you build your project. After create your project, press "See notes". All changes will automatically be shown on the screen.

## License 
[MIT](./LICENSE)

