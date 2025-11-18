Integrantes del equipo

Quiroga Matías – Bubble Sort

Caballero Matías – Insertion Sort

Hanow Mateo – Selection Sort


Caballero Matías – Insertion Sort

En mi parte del proyecto me encargué de implementar el algoritmo Insertion Sort, y para que pudiera funcionar dentro del sistema de visualización se tomaron algunas decisiones específicas.
Primero, se decidió usar variables globales para los índices i y j, además de la lista items, porque la ejecución avanza paso a paso y es necesario conservar el estado entre una llamada y la siguiente dentro de la función step().

También se definió un mecanismo en el que i avanza por la lista y j se va moviendo hacia atrás cuando corresponde, realizando intercambios adyacentes entre las posiciones j y j-1 cuando el elemento anterior es mayor.

La función step() devuelve en cada ejecución un diccionario que incluye "a", "b", "swap" y "done", lo que permite comunicar al sistema qué elementos están siendo comparados o intercambiados, y en qué momento el algoritmo termina. Cuando j deja de cumplir la condición necesaria para seguir retrocediendo, se finaliza la inserción del elemento correspondiente y se incrementa i. Y cuando i supera el tamaño de la lista, el algoritmo se marca como terminado.

Quiroga Matías – Bubble Sort

En esta parte del proyecto desarrolle el algoritmo Bubble Sort, y también fue necesario adaptarlo al sistema de ejecución paso a paso. La lógica del método consiste en comparar pares de elementos e intercambiarlos cuando están desordenados, pero implementarlo respetando el contrato del proyecto exigió tomar ciertas decisiones importantes.

Para empezar, se tuvo que controlar con precisión los índices i y j para que el algoritmo avanzara una comparación por vez, sin saltarse posiciones y respetando los límites de cada pasada. Esto fue clave para que el comportamiento coincidiera exactamente con lo que esperaba la visualización.

Otra decisión importante fue asegurar que el intercambio de los valores sucediera antes de devolver el diccionario con "a", "b", "swap" y "done". Ese detalle fue esencial para que la interfaz mostrara correctamente el cambio entre elementos en el momento justo.

También hubo dificultades al llevar el código a la estructura del repositorio, ya que no resultaba clara la ubicación correcta de los archivos ni cómo la aplicación los interpretaba. Tras varios intentos, pruebas y ajustes, se logró integrar correctamente el algoritmo dentro de la app.

Hanow Mateo – Selection Sort

En mi parte del proyecto implementé el algoritmo Selection Sort y tuve que adaptarlo al sistema de ejecución paso a paso que usa la aplicación. A diferencia de otros métodos, acá la idea es recorrer la parte no ordenada de la lista buscando el elemento más chico y, una vez encontrado, intercambiarlo con la posición actual. Aunque la lógica general es simple, dividir todo eso en pasos pequeños —uno por cada llamada a step()— fue lo que requirió más atención.

Para que funcionara bien dentro de la visualización, decidí usar variables globales para manejar el índice i (que marca la parte ya ordenada), el índice j (que recorre la parte no ordenada) y min_idx (que guarda la posición del menor encontrado hasta el momento). Esto permitió que el algoritmo recuerde su estado entre una llamada y la siguiente, algo necesario para avanzar de a una comparación por vez.

También separé el proceso en dos fases:
una fase de búsqueda, donde se compara cada elemento con el mínimo actual y se actualiza min_idx cuando corresponde;
y una fase de swap, donde se intercambian los valores si el mínimo no está en la posición correcta.

Esto ayudó a que cada paso sea claro y compatible con lo que la interfaz espera mostrar.

Al principio hubo algunas dificultades con los índices, especialmente para evitar comparaciones fuera de rango o swaps innecesarios. También costó un poco interpretar exactamente qué debía devolver cada step() para que la visualización mostrara correctamente qué elementos se estaban comparando. Después de varias pruebas y ajustes, Selection Sort quedó funcionando correctamente dentro del sistema paso a paso.

Gracias a estas decisiones, la implementación final pudo respetar el contrato del proyecto y mostrar el comportamiento del algoritmo de forma clara y ordenada.
