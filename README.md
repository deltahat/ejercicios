# Ejercicios resueltos
## Intalación
```sh
$ virtualenv -p python3 env_csvuploader
$ source env_csvuploader/bin/activate
(env_csvuploader) $ git clone https://github.com/deltahat/ejercicios.git
(env_csvuploader) $ cd ejercicios
(env_csvuploader) /ejercicios$ pip install -r requirements.txt
(env_csvuploader) /ejercicios$ cd csvuploader
(env_csvuploader) /ejercicios/csvuploader$ python manage.py makemigrations
(env_csvuploader) /ejercicios/csvuploader$ python manage.py migrate
```

### Ejercicio 1 (Merge Sort)
> En este ejercicio recibe dos listas y las une, creando asi una tercer lista que es retornada de manera ordenada de menor a mayor.
Para probarlo simplemente descomente el código comentando en ejercicios/mergesort.py y ejecutelo:

```sh
(env_csvuploader) $ cd ejercicios
(env_csvuploader) /ejercicios$ python mergesort.py
```
### Ejercicio 2 (CVS uploader)
> CVS uploader permite subir un archivo en formato .CSV con al menos dos columnas:
* country
* budget

>La plataforma procesa el archivo y obtiene segun un pais por defecto (USA):
* El costo total de todas los items de ese pais
* El costo promedio de todas los items de ese pais

> Tambien se pueden conocer:
* Todos los archivos csv subidos
* Todos los calculos de un archivo en particular

Para correr el servidor:
```sh
(env_csvuploader) /ejercicios/$ cd csvuploader
(env_csvuploader) /ejercicios/csvuploader$ python manage.py runserver
```

El servidor corre en [http://localhost:8000](http://localhost:8000)

#### Documentación
La documentación de la API está en [este link](https://app.swaggerhub.com/apis-docs/deltahat/CsvUploader/1.0.0/)