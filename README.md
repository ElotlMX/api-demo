# ¿Qué es una API? y ¿Para qué se usan?

API son siglas en inglés para *application programming interface* y es
un conjunto de definiciones y protocolos que permiten la integración de
diferentes aplicaciones.

# Interface

Una interface es una capa de abstracción lo que significa que podemos
interactuar con un sistema sin la necesidad de entender como está hecho o qué
esta pasando por detrás

Las APIs permiten acceder a desarrolladoras a datos y funcionalidades de la
comunidad.

Estas desarrolladoras no necesitan saber como funcionan solo necesitan saber
cómo pedirle cosas (*requests*).

# Ejemplos

* Una aplicación movil que diario muestra una frase en mixteco
* Juegos basados en palabras de lenguas mexicanas

Con esto se simplificar el desarrollo de aplicaciones haciendolo más rápido,
barato y sencillo (en teoría :p). 

# La API de Comunidad Elotl 

En el caso de la API de Elotl se abre el acceso a nuestros corpus paralelos
para que sean accesibles de forma programática. 

En otras palabras, acceso a las funcionalidades de búsqueda de Esquite por
medio de código en vez de una interface web.

# APIs fántasticas y dónde encontrarla

La API para acceder a los corpus paralelos de Comunidad Elotl se encuentra en
la url **`https://api.elotl.mx/`**

![Vista web de la API](img/api-web.png "opt title")

# ¿Como usar la API de Comunidad Elotl?

Un punto de partida es la documentación oficial de la API dónde se
muestra detalladamente información sobre como hacer las consultas, indices
disponibles entre otras.

## `https://esquite.readthedocs.io/es/latest/api.html`

![Documentación de la API](img/api-docs.png "opt title")

# ¿Desde dónde hago mi consulta?

Hay diferentes formas de usar la API con las que obtenemos resultados de
búsqueda.

* Desde Web

* Con un cliente

* Usando un lenguaje de programación (DEMO)

# Usuarias

Hay dos tipos de usuarias en la API, las anonimas y las registradas. La
diferencia entre una usuaria anonima y una registrada se muestra a continuación:


| Usuaria | Límite de peticiones | Límite de resultados |
|---------|----------------------|----------------------|
| anonima | 20 por hora / 50 por día | 10 |
| registrada| 50 por hora / 200 por día | 100 |

**NOTA:** Si les interesa registrarse para nuestro *early-access* de la API manden un
correo a `contacto at elotl.mx`

# ¿Como hacer consultas?

## Básica

```json
{
	"lang": "l1",
	"query": "niño",
	"index": "kolo-production"
}
```

## Completa


```json
{
	"lang": "l2",
	"query": "jamädi",
	"index": "tsunkua-production",
	"variants": ["ots", "ote"]
}
```

# ¿Como se ve la respuesta de datos?

```json
{
	"document_name": "Visión de los vencidos (hñahñu)",
	"pdf_file": "visiondelosvencidoshnahnu.pdf",
	"variant": "Otomí del Mezquital (ote)",
	"highlight": {
		"l2": [
				"Nu'i ri <em>jamädi</em> ya jä'i,"
		],
		"variant": [
				"<em>Otomí del Mezquital (ote)</em>"
		]
	},
	"l1": "Favorecido por la gente estás,",
	"l2": "Nu'i ri jamädi ya jä'i,"
}
```

# EsCLIte



---
title: "Usando la API de Elotl para construir tus propias aplicaciones"
author: Diego A. Barriga (@umoqnier)
institute: Comunidad Elotl
theme: metropolis
colortheme: default 
date: "17 de Julio 2021"
navigation: horizontal
---
