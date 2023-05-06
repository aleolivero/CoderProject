# Proyecto Final Curso de Python
# Coder House
## Olivero Aimaretti Alexis Ivan

## Trivia Web APP

Este proyecto es parte del curso de Python de la plataforma Coder House y consiste en una aplicación de trivia. 

La aplicacion web de trivia consiste en un juego donde distintos jugadores realizan preguntas, los cuales deben responder mediante respuestas aproximadas, el ganador es aquel que su respuesta fue la mas proxima a la respuesta correcta.

Las preguntas que van generando los jugadores se agrupan en eventos. Dichos evetos se van generando y cerrando. Por lo que surgen ganadores de eventos, que son aquellos que mas puntos han sumado a lo largo de ganar las distintas preguntas.

La aplicacion permite el acceso de dos tipos de usuarios:

## USUARIOS

### **Players**
Los cuales tienen acceso a revisar respuestas y preguntas generados por ellos.
Ademas tienen acceso a participar en los eventos y ver los scores que se fueron generando.

La aplicación para los jugadores se divide en las siguientes secciones:

1. **Answers**
Permite visualizar todas las respuestas efectuadas por el jugador logueado.

2. **Questions**
Permite visualizar y gestionar las preguntas efectuadas por el jugador logueado.

3. **Events**
Permite participar en los eventos, respondiendo a las preguntas que generen los demas jugadores, y teniendo la posibilidad de ver el ranking del evento.

4. **Scores**
Listado que permite ver las puntuaciones por evento, cada pregunta generada y cuyo resultado fue determinado.

### **Staff**
Los miembros del staff, tienen una seccion adicional en la navbar que les permiten ver el listado de players, todas las respuestas y preguntas generadas.
Ademas tienen posibilidad de ver, añadir, editar y eliminar eventos y reglas de preguntas.

## DINAMICA

1. Un jugador crea una pregunta, dicha pregunta esta asignada a un evento y tiene asociada unas reglas (que determinan como seran los puntajes).
2. Los distinos jugadores de la app pueden participar contestando la pregunta desde la seccion de eventos. La pregunta se podra visualizar cuando hagan click en añadir respuesta.
3. Cuando todos los jugadores hayan participado, el creador de la pregunta podra cerrarla, evitando que se sigan cargando preguntas.
4. Luego de cerrarla, podra calcular el resultado.
5. Una vez calculado el resultado, se podra ver el resultado final con el listado de respuestas y el ganador de la pregunta.
6. El ganador de la pregunta tendra asignado puntos (de acuerdo a las reglas de la pregunta) que se iran acumulado a lo largo del evento.
7. La dinamica continua de la misma forma hasta que el evento se cierra.
8. En el proceso del juego, los jugadores pueden consultar como fueron los scores de las preguntas que se fueron generando y ademas consultar el ranking del evento.
8. Cuando el evento se cierra, se puede ver el ranking con el ganador del evento y el segundo y tercer puesto. Desd este momento no se pueden cargar mas preguntas.

## OTRAS FUNCIONALIDADES

### Profile
Cuando el usuario se registra, se genera mediante signals un registro en el model Players, que sera el perfil del usuario.
En el profile, el usuario puede cargar sus datos y su avatar.

### Account
Permite al jugador cambiar su email o contraseña

## Exchange
Es un sistema de chat de la web app, donde todos los jugadores pueden enviar mensajes 

