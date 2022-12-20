#### Hexlet tests and linter status:
[![Actions Status](https://github.com/zluuba/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/zluuba/python-project-49/actions) <a href="https://codeclimate.com/github/zluuba/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/8f30055514168a104cb1/maintainability" /></a>


### Welcome to the Brain Games
'Brain Games' includes five math games: 'Parity Check', 'Calculator', 'Greatest Common Divisor', 'Arithmetic Progression' and 'Is it a Simple Number?'. <br />
This is the **first project** created as part of Python learning.
All games are started and played using the terminal. <br />
[Readme на русском языке >>](https://github.com/zluuba/python-project-49#%D0%B8%D0%B3%D1%80%D1%8B-%D1%80%D0%B0%D0%B7%D1%83%D0%BC%D0%B0)

### Requirements
- [python](https://www.python.org/), version 3.10 or higher
- [poetry](https://python-poetry.org/), version 1.0.0 or higher
- [prompt](https://prompt.readthedocs.io/en/latest/) package, version 0.4.1 or higher

### Installation
Download ZIP-file to your PC and unzip it.
You can also clone this repo or **download it with pip**:
```ch
git clone https://github.com/zluuba/python-project-49.git                   # clone repository
```
```ch
pip install --user git+https://github.com/zluuba/python-project-49.git      # download with pip
```

Go to the installed folder in the terminal and using these commands to install package:
```ch
make install
make build
make package-install
```

### Commands for playing
Once the package is installed, to start playing, you should enter any of the commands below.

#### **"Parity Check"** game
Is a number on the screen, you must enter "yes" if the number is even and "no" if it's not. <br />
[Demonstration](https://github.com/zluuba/python-project-49#even-game)
```ch
brain-even
```

#### **"Calculator"** game
Is given a mathematical expression, you need to calculate it and enter the result. <br />
[Demonstration](https://github.com/zluuba/python-project-49#calculator-game-1)
```ch
brain-calc
```

#### **"The Greatest Common Divisor"** game
Two numbers are given, you need find the greatest common divisor and enter the result. [More about GSD](https://en.wikipedia.org/wiki/Greatest_common_divisor) <br />
[Demonstration](https://github.com/zluuba/python-project-49#greatestcommondivisor-game)
```ch
brain-gcd
```

#### **"Arithmetic Progression"** game
Is given an arithmetic sequence in which one number is hidden, you must enter the missing number. <br />
[Demonstration](https://github.com/zluuba/python-project-49#progression-game)
```ch
brain-progression
```

#### **"Is it a Simple Number?"** game
Is a number on the screen, you must enter "yes" if the number is prime and "no" if it's not. [More about prime numbers](https://en.wikipedia.org/wiki/Prime_number) <br />
[Demonstration](https://github.com/zluuba/python-project-49#prime-game)
```ch
brain-prime
```


### How to play. Demonstration

#### Even Game:
[![asciicast](https://asciinema.org/a/h6cIIpEGMbiNajL8XJ02GrOPX.svg)](https://asciinema.org/a/h6cIIpEGMbiNajL8XJ02GrOPX)

#### Calculator Game:
[![asciicast](https://asciinema.org/a/H00VVTCBDKfmdu3LVuOQPEMza.svg)](https://asciinema.org/a/H00VVTCBDKfmdu3LVuOQPEMza)

#### GreatestCommonDivisor Game:
[![asciicast](https://asciinema.org/a/hgcLbeJ0WcWTQIHewflnZrFGQ.svg)](https://asciinema.org/a/hgcLbeJ0WcWTQIHewflnZrFGQ)

#### Progression Game:
[![asciicast](https://asciinema.org/a/PBE94ttXoDZKKZ4EcT5A3vaC7.svg)](https://asciinema.org/a/PBE94ttXoDZKKZ4EcT5A3vaC7)

#### Prime Game:
[![asciicast](https://asciinema.org/a/rELtozb3KeYL1sz5XDkqLyZhv.svg)](https://asciinema.org/a/rELtozb3KeYL1sz5XDkqLyZhv)

<hr>

## Игры Разума
"Игры Разума" - это мой первый проект, созданный для начального изучения Python, окружения и Git. Проект включает в себя пять математических игр: "Проверка на чётность", "Калькулятор", "Наибольший общий делитель", "Арифметическая прогрессия" и "Простое ли число?".
Все игры запускаются с помощью терминала.

### Минимальные требования
- [python](https://www.python.org/), версия 3.10 или выше
- [poetry](https://python-poetry.org/), версия 1.0.0 или выше
- [prompt](https://prompt.readthedocs.io/en/latest/) package, версия 0.4.1 или выше


### Установка
Чтобы установить сборник мини-игр, нужно скачать архив (ZIP-файл) и разархивировать его на своём компьютере.
Также вы можете склонировать этот репозиторий через терминал или скачать пакет при помощи терминала и команды pip:
```ch
git clone https://github.com/zluuba/python-project-49.git                   # клонирование репозитория
```
```ch
pip install --user git+https://github.com/zluuba/python-project-49.git      # скачать пакет с помощью pip
```

Затем, при помощи терминала нужно перейти в директорию с загруженными файлами и установить пакет с помощью команд:
```ch
make install
make build
make package-install
```

### Как играть 
Когда пакет установлен, чтобы начать играть, нужно ввести любую команду из списка:

#### **"Проверка на четность"**
На экран выводится число, нужно ввести "yes", если число четное и "no", если не четное. <br />
[Demonstration](https://github.com/zluuba/python-project-49#even-game)
```ch
brain-even
```

#### **"Калькулятор"**
Даётся математическое выражение, нужно его вычислить и ввести результат. <br />
[Demonstration](https://github.com/zluuba/python-project-49#calculator-game-1)
```ch
brain-calc
```

#### **"Наибольший общий делитель"**
Даются два числа, нужно вычислить наибольший общий делитель и записать его. [Подробнее о НОД](https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D0%B8%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B8%D0%B9_%D0%BE%D0%B1%D1%89%D0%B8%D0%B9_%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C) <br />
[Demonstration](https://github.com/zluuba/python-project-49#greatestcommondivisor-game)
```ch
brain-gcd
```

#### **"Арифметическая прогрессия"**
Даётся последовательность из чисел, в которой одно число спрятано, нужно ввести недостающее число. <br />
[Demonstration](https://github.com/zluuba/python-project-49#progression-game)
```ch
brain-progression
```

#### **"Простое ли число?"** game
Дается число, нужно ввести "yes", если число простое, если нет, ввести "no". [Подробнее о простых числах](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE) <br />
[Demonstration](https://github.com/zluuba/python-project-49#prime-game)
```ch
brain-prime
```

<hr>

##### From [Hexlet](https://hexlet.io/my) student with love :› <br />
