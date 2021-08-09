<h1 align="center">PoligonAPI</h1>

## ArrowIT REST Server

Servidor REST en Django para Test de API para generar, listar, encontrar polígonos y verificar si un punto esta dentro del poligono

## Contents

- [Usage](#Usage)

  - [EndPoints Api](#EndPoints-Api)

- [Autor](#Autor)
- [License](#License)

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
