# Juego el Ahorcado
Repositorio del Trabajo Práctico de la materia **Programación I** del 
primer cuatrimestre de 2025.

Profesor: Loffreda Ariel Alfredo

## Integrantes del grupo
|Nombre del alumno|Legajo|
|--|--|
|Ibañez, Emanuel |1176686|
|Patze Pacheco, Diego Alvaro |1196069|
|Sixto Calderón, Edwar Manuel |1200984|
|Montero, Tomas Angel |1204179|

## Descripción del proyecto
El Ahorcado es un juego clásico de palabras que se utiliza comúnmente como recurso educativo y de entretenimiento. Su objetivo principal es que el jugador adivine una palabra oculta, letra por letra, dentro de un número limitado de intentos. Cada intento incorrecto hace que el jugador este cada vez más cerca a perder, simbolizada tradicionalmente por el dibujo progresivo de una figura humana en una horca. 

Este juego fomenta habilidades lingüísticas, como la ortografía, el vocabulario y la capacidad de deducción lógica. Además, promueve la concentración y la toma de decisiones estratégicas, ya que el jugador debe seleccionar con cuidado cada letra para evitar agotar sus oportunidades. 

Debido a su simplicidad y dinamismo, El Ahorcado es ampliamente utilizado en contextos educativos para reforzar el aprendizaje del idioma de manera interactiva y motivadora. 

Funcionalidades del Juego 

Carga de Inicio Al iniciar el programa:  

 

Se muestra una pantalla de inicio que presenta dos opciones: 

REGISTRARSE: Permite el registro de un nuevo usuario. 

INICIAR SESIÓN: Nos permite ingresar el usuario existente, y empezar el juego. 

SALIR: Finaliza la ejecución del programa. 

Gestión de Usuarios Creación de Cuenta: 

Al seleccionar “REGISTRARSE”, se solicita el ingreso de un usuario que nunca haya sido registrado. El nombre de usuario debe ser único. En caso de que el nombre ya exista, se solicitará un nombre distinto. 

La contraseña debe tener como mínimo una longitud de 8 caracteres. 

Al seleccionar “INICIAR SESIÓN”, una vez creado el usuario, el registro se completa y el jugador puede acceder a su cuenta del juego. 

Mecánica del Juego Dinámica: 

El objetivo es adivinar una palabra oculta antes de agotar los intentos. Al inicio de cada nivel, se muestra una horca y una serie de guiones bajos (“_ _ _ _ _“) representando el número de letras de la palabra. 

El jugador cuenta con 6 intentos. Cada letra incorrecta reduce el número de intentos y dibuja progresivamente la silueta en la horca, si el jugador acierta una letra, esta se revela en la palabra. Al completar correctamente la palabra, el jugador avanza al siguiente nivel. 

Perder: 

Si el jugador pierde todos los intentos, el nivel se da por perdido. Al volver a intentarlo, la palabra será diferente y seleccionada aleatoriamente. 

Sistema de Progreso: 

 

El progreso se guarda automáticamente, permitiendo continuar desde el último nivel alcanzado. 

Si es la primera vez que el jugador participa, comienza desde el nivel 1. 

Sistema de Monedas Recompensas: 

El jugador recibe 100 monedas al crear su cuenta. Por cada nivel superado, el jugador obtiene 25 monedas adicionales. Las monedas se acumulan y pueden ser utilizadas para obtener ventajas en el juego. 

Intercambio de Monedas: 

Las monedas permiten comprar ayudas, como la función "Revelar Letra". El costo de revelar una letra es de 40 monedas. Esta función está disponible excepto cuando solo queda una letra por adivinar. 

Reinicio de Nivel:  

Si el jugador pierde el nivel, puede intentarlo nuevamente. La palabra será diferente a la anterior para evitar repetición y fomentar el desafío. 

Finalización del Juego: 

El jugador puede finalizar la sesión en cualquier momento y regresar posteriormente para continuar su progreso. 

El juego concluye una vez que el jugador haya completado todos los niveles o decida no seguir jugando. 
