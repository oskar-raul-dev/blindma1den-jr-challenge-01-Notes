Pasos para la instalación

- ir a https://www.python.org/downloads/windows/
    * Ultimo instalador y ejecutar
    * En el primer paso del instalador marcar la casilla de agregar ejecutables de python
      al path
    * Luego de la instalación abrir una consola y probar comandos
      python --version
      pip --version

- Virtual environments (venv)
  https://docs.python.org/3/library/venv.html

  Tutorial 
  https://realpython.com/python-virtual-environments-a-primer/

  permite crear un proyecto autocontenido 
  con un directorio que tiene todo el entorno específico

    * comando
    python -m venv [directorio del entorno virtual]
    Ejemplo (tradición el directorio se llaman venv)

    python -m venv venv

    * El venv es dependiente del SO, eso significa
      que si cambian a linux o macos deben generar el 
      directorio venv (no se incluya en el repo github)

    Arranque del entorno virtual
     Se ejecuta el script activate.bat (windows)
     venv\scripts\activate

     activate.sh (linux)
     source venv/scripts/activate.sh

- Pip para manejo de dependencias
   un gestor para descarga de depencias 

   - Las librerías de python se pueden descargar de un registro
     en 
       * https://pypi.org/  Descarga de dependencias
       * https://pypi.org/project/pip/ comando pip


     Para gestionar la descarga se usa el comando pip
       - En la raíz del proyecto creo un archivo dependecies.txt

Para iniciar un proyecto 
  * instalar venv en el dir. raiz (python -m venv venv)
  * Crear en la raíz un archivo txt para las dependencias de pip (depencies.txt o requirements.txt)
  * activar el venv (venv\scripts\activate)
  * instalar depencias (pip -r ./dependencies.txt)
  * la primera vez si se desea "pinear" las dependcias a una versión fija 
    se usa el comando pip freeze
    pip freeze -r .\dependencies.txt
    El comando emite en la salida de consola, el contenido nuevo
    de dependencias y se puede escribir al archivo dependencies.txt
  
  * Cuando termino el trabajo puedo desactivar el venv con el comando
    deactivate

    Se ejecuta el script deactivate.bat (windows)
     venv\scripts\deactivate

     deactivate.sh (linux)
     source venv/scripts/deactivate.sh

     Validar si esto no funciona en power shell
