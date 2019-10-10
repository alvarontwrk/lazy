# lazy

## Description
Script written in Python3 that lists closed issues from a given GitHub repository from a certain
date until now. 

## Installation
-   Clone the repo:
```bash
git clone https://github.com/AlvaroGarciaJaen/lazy
```

-   Install the dependencies:
```bash
pipenv install
```

## Usage
```bash
pipenv run python lazy.py -u <user> -r <repo> -d <date>
```

## Example
```bash
pipenv run python lazy.py -u AlvaroGarciaJaen -r alreadycracked -d 08-10-2019
```

Output:
```
[Documentación y estructura](https://github.com/AlvaroGarciaJaen/alreadycracked/milestone/1)
-    [Actualizar README](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/16)
-    [Configurar gh-pages](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/15)
-    [Cambiar localización de alreadycracked.rb](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/12)
-    [Mejorar .gitignore](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/7)
[Integración continua](https://github.com/AlvaroGarciaJaen/alreadycracked/milestone/2)
-    [Corregir clase tests](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/20)
-    [Añadir tests para devolución de texto plano](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/18)
-    [Añadir tests sobre detección de hashes](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/17)
-    [Añadir CircleCI](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/14)
-    [Corregir path de alreadycracked.rb en los tests](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/13)
-    [Añadir primeros tests](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/11)
-    [Crear .travis.yml](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/10)
-    [Añadir .ruby-version](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/8)
[Desarrollo microservicio](https://github.com/AlvaroGarciaJaen/alreadycracked/milestone/6)
-    [Añadir funciones al microservicio](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/19)
-    [Crear clase prototipo para el microservicio](https://github.com/AlvaroGarciaJaen/alreadycracked/issues/9)
```
