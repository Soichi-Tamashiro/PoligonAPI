<h1 align="center">PoligonAPI</h1>

## ArrowIT REST Server

Servidor REST en Django para Test de API para generar, listar, encontrar polígonos y verificar si un punto esta dentro del poligono

## Contents

- [Despliegue](#Despliegue)

  - [Requerimientos](#Requerimientos)
  - [Django](#Django)

- [Usage](#Usage)

  - [EndPoints Api](#EndPoints-Api)

- [Autors](#Autors)
- [License](#License)

## [Despliegue](#Contents)

## [Requerimientos](#Contents)

- <b>Paso 1 actualizar Amazon Linux 2 (EC2 Instance)</b>

  ```
  yum update -y
  ```

- <b>Paso 2 Instalar el repositorio Epel y descargar PIP</b>

  ```
  sudo amazon-linux-extras install epel -y
  ```

- <b>Paso 3 Instalar Django usando PIP</b>

  Instalar PIP

  ```
  sudo yum install python3-pip -y
  ```

  Instalar Django

  ```
  pip3 install django
  ```

- <b>Paso 4 Instalar Virtualenv y activar</b>

  Instalar virtualenv

  ```
  sudo pip3 install virtualenv
  ```

  crear virtualenv

  ```
  virtualenv djangoenv
  ```

  activar virtualenv

  ```
  source ~/djangoenv/bin/activate
  ```

- <b>Paso 5 Instalar Django dentro de virtualenv</b>

  ```
  pip3 install – -upgrade Django
  ```

- <b>Paso 7 Instalar sqlite3</b>

  ```
  sudo yum install libsqlite3-dev
  ```

  fix sqlite3 error

  ```
  export LD_LIBRARY_PATH="/usr/local/lib/"
  ```

- <b>Paso 8 Instalar DjangoRestframework</b>

  ```
  pip3 install django djangorestframework django-cors-headers gunicorn
  ```

- <b>Paso 9 Instalar shapely</b>

  ```
  pip3 install shapely
  ```

- <b>Paso 10 Instalar git</b>

  ```
  sudo yum install git -y
  ```

- <b>Paso 11 Clonar repositorio</b>

  ```
  git clone https://github.com/Soichi-Tamashiro/PoligonAPI.git
  ```

## [Requerimientos](#Contents)

- <b>Paso 1 Actualizar ALLOWED_HOST en settings.py agregar la IP publica de la instancia</b>

  ```
  ALLOWED_HOSTS = [
    "18.219.166.96",
    "127.0.0.1",
  ]
  ```

- <b>Paso 2 agregar una regla inbound para el puerto 8000</b>

  ![image](https://user-images.githubusercontent.com/26827763/128682834-d45afdd5-b600-4f0d-8f30-c33b600355bd.png)

- <b>Paso 1 Actualizar ALLOWED_HOST en settings.py</b>

  ```
  ALLOWED_HOSTS = [
    "18.219.166.96",
    "127.0.0.1",
  ]
  ```

## [Usage](#Contents)

### [EndPoints Api](#Contents)

- <b><a id="Polygon-urls-end">Urls</a></b>

  | Función                             | Tipo | URLs                                        |
  | ----------------------------------- | ---- | ------------------------------------------- |
  | [Generar Polígono](#Polygon-add)    | POST | `http://18.219.166.96:8000/polygon/create/` |
  | [Listar Polígonos](#Polygon-list)   | GET  | `http://18.219.166.96:8000/polygon/list/`   |
  | [Encontrar Polígono](#Polygon-find) | POST | `http://18.219.166.96:8000/polygon/find/`   |
  | [Verificar Punto](#Polygon-verify)  | GET  | `http://18.219.166.96:8000/polygon/verify/` |

- <b>Examples</b>

  - <b><a>Header and Token</a></b>
    [(back)](#Polygon-urls-end)

    Token para poder realizar los pedidos a la API

    <b>Token</b>

    ```
    3839b4431817b745f027644a104a69c66b949179
    ```

    <b>POSTMAN Code</b>

    ![image](https://user-images.githubusercontent.com/26827763/128678366-1b838804-f070-4b5c-b468-b64dace63d71.png)

  - <b><a id="Polygon-add">Generar Polígono (POST)</a></b>
    [(back)](#Polygon-urls-end)

    Agregar Polígono ingresando el número de puntos

    <b>JSON Code</b>

    ```javascript
    {
      "puntos_n": 3
    }
    ```

    <b>POSTMAN Code</b>

    ![image](https://user-images.githubusercontent.com/26827763/128677001-12c0ee15-3978-4bef-b484-fa932665318e.png)

  - <b><a id="Polygon-list">Listar Polígonos (GET)</a></b>
    [(back)](#Polygon-urls-end)

    Listar todos los Polígonos

    <b>JSON Code</b>

    ```javascript
    {
    }
    ```

    <b>POSTMAN Code</b>

    ![image](https://user-images.githubusercontent.com/26827763/128677098-b40ab564-7be7-4b5c-a3c5-74c18422871d.png)

  - <b><a id="Polygon-find">Encontrar Polígono (POST)</a></b>
    [(back)](#Polygon-urls-end)

    Buscar Polígono con ID

    <b>JSON Code</b>

    ```javascript
    {
        "id":2
    }
    ```

    <b>POSTMAN Code</b>

    ![image](https://user-images.githubusercontent.com/26827763/128677158-2d019d18-bfce-4de7-a1fe-5cd65a1dec63.png)

  - <b><a id="Polygon-verify">Verificar Punto (POST)</a></b>
    [(back)](#Polygon-urls-end)

    Verificar punto dentro del Polígono

    <b>JSON Code</b>

    ```javascript
      {
        "id": 1,
        "x":0.0,
        "y":0.0
      }
    ```

    <b>POSTMAN Code</b>

    ![image](https://user-images.githubusercontent.com/26827763/128677210-abf647d4-9219-4752-89a9-de8e694ff7af.png)

## [Autors](#Contents)

- Soichi Tamashiro

## [License](#Contents)

```

```
