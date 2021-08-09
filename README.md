# PoligonAPI

Test de API para generar Poligonos

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

  | Función                             | URLs                                        |
  | ----------------------------------- | ------------------------------------------- |
  | [Generar Polígono](#Polygon-add)    | `http://18.219.166.96:8000/polygon/create/` |
  | [Listar Polígonos](#Polygon-list)   | `http://18.219.166.96:8000/polygon/list/`   |
  | [Encontrar Polígono](#Polygon-find) | `http://18.219.166.96:8000/polygon/find/`   |
  | [Verificar Punto](#Polygon-verify)  | `http://18.219.166.96:8000/polygon/verify/` |

- <b>Examples</b>

  - <b><a id="Polygon-add">Agregar Polígono ingresando el número de puntos (POST)</a></b>
    [(back)](#Polygon-urls-end)

    <b>JSON Code</b>

    ```javascript
    {
      "puntos_n": 3
    }
    ```

    <b>POSTMAN Code</b>

    ![imagen](https://user-images.githubusercontent.com/38510593/116279164-d6ead780-a74c-11eb-9993-c835c2370c99.png)

  - <b><a id="Polygon-list">Listar todos los Polígonos (GET)</a></b>
    [(back)](#Polygon-urls-end)

    <b>JSON Code</b>

    ```javascript
    {
    }
    ```

    <b>POSTMAN Code</b>

    ![imagen](https://user-images.githubusercontent.com/38510593/116279439-26c99e80-a74d-11eb-84ad-e92e14f786c4.png)

  - <b><a id="Polygon-find">Buscar Polígono con ID (POST)</a></b>
    [(back)](#Polygon-urls-end)

    <b>JSON Code</b>

    ```javascript
    {
        "id":2
    }
    ```

    <b>POSTMAN Code</b>

    ![imagen](https://user-images.githubusercontent.com/38510593/116279644-65f7ef80-a74d-11eb-8f06-65ba3f363897.png)

  - <b><a id="Polygon-verify">Verificar punto dentro del Polígono (POST)</a></b>
    [(back)](#Polygon-urls-end)

    <b>JSON Code</b>

    ```javascript
      {
        "id": 1,
        "x":0.0,
        "y":0.0
      }
    ```

    <b>POSTMAN Code</b>

    ![imagen](https://user-images.githubusercontent.com/38510593/116280870-bf145300-a74e-11eb-9346-268db837a085.png)

## [Autors](#Contents)

- Soichi Tamashiro

## [License](#Contents)

```

```
