Configuración inicial:

1-Clonar el repositorio:

git@github.com:Gordisluis/Draftapp.git


2-Sincronización del repositorio:

git fetch origin
git merge origin/master

Esto traerá los últimos cambios del repositorio remoto y los fusionará en su rama local.

2.2- luego de clonar deben de ejecutar la instalacion de las dependencias:

pip install requirements.txt

2.3- luego corren el projecto con:

python manage.py runserver

para tailwindcss usaremos la rama tailwindcssmetodo2 que esta correcta la implementacion.

deben de pasar a la rama con git de vscode que es mas facil. cualquier duda me avisan

1.1 solo debes de ejecutar en otra terminal nueva este comando para que compile todos los cambios relacionados a tailwindcss 

npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch --minify



