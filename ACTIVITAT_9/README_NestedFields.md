# Documentación Nested Body Fields

## Atributo como subtipo list
![Definir atributo como subtipo](imagenes/SubtipoPython.png)
En este caso tags sera una lista que contendra strings, es importante antes de nada Importar List
![prueba1](imagenes/prueba_swagger1.png)

## Atributo como subtipo set
![subtipo set](imagenes/setNestedFields.png)
Ahora en este caso en vez de usar una lista utiliza un set
![prueba2](imagenes/prueba_swagger2.png)

## Definir submodelo
![submodelo img](imagenes/submodeloNested.png)
Aqui podemos ver que primero define un modelo Image y luego en otro modelo lo utliza el modelo anterior como atributo.


De esta manera FastApi nos devolveria algo parecido a esto:
```json
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
```
![prueba3](imagenes/prueba_swagger3.png)

## Tipos singulares complejos
![http](imagenes/httpNestedFields.png)
Es poden utilitzar tipus singulars més complexes en aquest cas s'utilitza http que es heredat del str, tenim que tenir en compte que hi ha que importar el modul
![prueba4](imagenes/prueba_swagger4.png)


## Submodelo list
![Submodelo List](imagenes/SubmodeloList.png)
Aqui podemos ver como se define un submodelo y ademas que puede ser de tipo List
![prueba5](imagenes/prueba_swagger5.png)

## Submodelos Anidados
![modelo anidado](imagenes/submodelosAnidados.png)
En esta imagen podemos ver como hace el submodelo de un submodelo
![prueba6](imagenes/prueba_swagger6.png)