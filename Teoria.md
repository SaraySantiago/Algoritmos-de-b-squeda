# estudio de busquedas

*¿Qué es un algoritmo de búsqueda?*
un algoritmo de búsqueda es un procedimiento computacional diseñado para localizar un elemento específico dentro de una estructura de datos. Esta estructura de datos puede ser desde un simple array hasta complejas bases de datos o grafos.

*Algoritmo de búsqueda:* Un algoritmo de búsqueda es un conjunto de instrucciones que le dicen a la computadora cómo encontrar algo específico dentro de un grupo de cosas. Es como una receta para encontrar un tesoro escondido.

# ¿Cómo funciona?
Imagina que tienes una lista de números y quieres encontrar uno en particular. Un algoritmo de búsqueda te diría cómo revisar la lista para encontrar ese número. 
**Partes de un algoritmo de búsqueda**

*¿Dónde?* Es el lugar donde vas a buscar, puede ser una lista de números o un libro.
*¿Qué?* Es lo que estás buscando, desde un número hasta una palabra.
*¿Cómo?* Es la forma en la que lo vas a buscar, puede ser revisando uno por uno o diviendo el lugar de búsqueda en partes más pequeñas.

**Ejemplo de las partes de un algoritmo de búsqueda**
Vamos a buscar la palabra "manzana" en un libro, y lo haremos de la siguiente forma:
*¿Dónde?* En el libro.
*¿Qué?* La palabra "Manzana".
*¿Cómo?* Revisando cada página del libro hasta encontrar la palabra "manzana" (búsqueda lineal) o dividiendo el lugar de búsqueda (las páginas) en partes más pequeñas y buscar en las partes que más se acerquen a la palabra manzana (búsqueda binaria).

Tipos de algoritmos de búsqueda Hay muchos tipos de algoritmos de búsqueda, pero aquí te explicaré los dos más básicos:

**Búsqueda lineal** (búsqueda secuencial): EL más sencillo.
Funciona revisando cada elemento de la lista uno por uno, hasta que encuentra el elemento que estás buscando.
Es como buscar un libro en una estantería revisando cada libro uno por uno.
Ejemplo:
DONDE Tienes la lista de números: [5, 2, 8, 1, 9]
QUE el número 8.
COMO: revisaráS el 5, luego el 2, luego el 8. ... Cuando llegueS al 8, STOP y MENSAJE DE "encontrado"

**Búsqueda binaria**: Este algoritmo es mucho más rápido que la búsqueda lineal, pero solo funciona si la lista está ordenada. Funciona dividiendo la lista por la mitad y luego decidiendo en qué mitad buscar. Repite este proceso hasta que encuentra el elemento que estás buscando. Es como buscar una palabra en un diccionario: abres el diccionario por la mitad, miras la página y decides si la palabra está antes o después de esa página. Ejemplo: Tienes la lista ordenada de números: [1, 2, 5, 8, 9] Quieres encontrar el número 8. 

La búsqueda binaria divide la lista por la mitad y mira el número del medio, que es el 5. Como el 8 es mayor que el 5, sabe que tiene que buscar en la segunda mitad de la lista. Divide la segunda mitad de la lista por la mitad y mira el número del medio, que es el 8. Como encontró el 8, se detiene y te dice que lo encontró. 

¿Cuándo usar cada algoritmo? 
Usa la búsqueda lineal cuando la lista no está ordenada o cuando es muy pequeña.
Usa la búsqueda binaria cuando la lista está ordenada y es grande. 

# ¿Qué más tipos de busquedas hay?
Existen otros tipos de búsquedas que se utilizan en informática:

- **Búsqueda en profundidad (DFS)**: Imagina un laberinto. Este algoritmo explora un camino hasta el final antes de retroceder y probar otro. Es útil para encontrar soluciones en espacios de búsqueda con muchas opciones.

- **Búsqueda en anchura (BFS)**: En el mismo laberinto, este algoritmo explora todos los caminos cercanos antes de avanzar a los más lejanos. Se utiliza para encontrar el camino más corto entre dos puntos.

- **Búsqueda por interpolación**: Es como buscar una palabra en un diccionario, pero estimando dónde podría estar según la posición de la primera letra. Se utiliza cuando los datos están distribuidos uniformemente.

- **Búsqueda de salto**: En lugar de revisar cada elemento, este algoritmo salta algunos elementos y luego busca linealmente en un rango más pequeño. Es útil para listas grandes y ordenadas.

- **Algoritmos de búsqueda heurística**: Estos algoritmos utilizan información adicional para adivinar dónde podría estar el elemento buscado. Se utilizan en inteligencia artificial para resolver problemas complejos.

Además, Los algoritmos de búsqueda no solo se usan en listas de números, sino también en muchos otros lugares:

- Buscadores de internet: Cuando buscas algo en Google, Bing o DuckDuckGo, los algoritmos de búsqueda te ayudan a encontrar las páginas web que coinciden con lo que buscas.

- Bases de datos: Las bases de datos son como grandes bibliotecas digitales que almacenan mucha información. Los algoritmos de búsqueda se utilizan para encontrar información específica dentro de estas bases de datos.

- Sistemas de navegación GPS: Cuando usas un GPS para encontrar una dirección, los algoritmos de búsqueda te ayudan a encontrar la ruta más corta.

- Redes sociales: Cuando buscas amigos, publicaciones o grupos en Facebook, Instagram o Twitter, los algoritmos de búsqueda te ayudan a encontrar lo que buscas.

- Tiendas en línea: Cuando buscas productos en Amazon, eBay o Mercado Libre, los algoritmos de búsqueda te ayudan a encontrar los productos que te interesan.

- Videojuegos: Los algoritmos de búsqueda se utilizan en videojuegos para que los personajes encuentren objetos, naveguen por el mundo del juego o encuentren la mejor estrategia para ganar.
- Inteligencia artificial: Los algoritmos de búsqueda son una parte importante de la inteligencia artificial. Se utilizan para que las computadoras puedan aprender y tomar decisiones.

- Robótica: Los algoritmos de búsqueda se utilizan en robótica para que los robots puedan encontrar objetos, navegar por entornos desconocidos o realizar tareas complejas.

- Bioinformática: Los algoritmos de búsqueda se utilizan en bioinformática para buscar patrones en secuencias de ADN o proteínas.

**Otras maneras de buscar serían:**

- Búsqueda heurística:
Imagina que buscas un tesoro en un mapa muy grande. La búsqueda heurística te da pistas sobre dónde es más probable que esté el tesoro, para que no tengas que revisar todo el mapa.
Se usa mucho en inteligencia artificial, por ejemplo, para que un robot encuentre la mejor manera de moverse por un lugar.

- Búsqueda paralela:
Es como tener muchos amigos buscando el mismo tesoro al mismo tiempo. Cada amigo revisa una parte del mapa, así se encuentra el tesoro mucho más rápido.
Se usa en computadoras muy potentes para buscar en bases de datos enormes.

- Búsqueda distribuida:
Es similar a la búsqueda paralela, pero en lugar de tener muchos amigos en el mismo lugar, cada amigo busca desde su propia casa y luego comparten la información.
Se usa en internet, por ejemplo, cuando buscas algo en Google.

- Búsqueda cuántica:
Es una forma muy avanzada de búsqueda que utiliza las leyes de la física cuántica para encontrar cosas aún más rápido.
Todavía está en desarrollo, pero podría revolucionar la forma en que buscamos información en el futuro.


**¿Dónde se usan los algoritmos de búsqueda?**
Los algoritmos de búsqueda se usan en muchas aplicaciones, como: Motores de búsqueda (Google, Bing) Bases de datos Inteligencia artificial Videojuegos
**¿Por qué son importantes los algoritmos de búsqueda?**
 Los algoritmos de búsqueda son importantes porque nos permiten encontrar información rápidamente. Sin ellos, sería muy difícil encontrar información en el mundo digital.
