# ========== DEFINICIONES PRINCIPALES ==========

# PERSONAJES
define prota = Character("Alex", color="#ff6b6b")
define entrenador = Character("Entrenador Marco", color="#4ecdc4")
define medico = Character("Dra. Silva", color="#ffd166")

# VARIABLES DEL ESTADO
default energia = 100
default concentracion = 100
default ritmo_cardiaco = 70
default confianza = 50
default salud_mental = 100

# TRANSFORMACIONES
transform centrado:
    xalign 0.5 yalign 0.5

transform izquierda:
    xalign 0.2 yalign 0.5

transform derecha:
    xalign 0.8 yalign 0.5

# IMAGENES SIMPLES (sin archivos externos)
image alex pensativo = Placeholder("boy")
image alex mirando_lejos = Placeholder("boy")
image alex triste = Placeholder("boy")
image alex normal = Placeholder("boy")
image alex determinacion = Placeholder("boy")
image alex concentrado = Placeholder("boy")
image alex aliviado = Placeholder("boy")
image alex feliz = Placeholder("boy")
image alex melancolico = Placeholder("boy")

image entrenador = Placeholder("man")
image entrenador serio = Placeholder("man")
image medico = Placeholder("woman")

image circulo_verde = Solid("#00ff00", xsize=100, ysize=100)
image circulo_rojo = Solid("#ff0000", xsize=100, ysize=100)
image efecto_exito = Solid("#00ff88", xsize=200, ysize=200)
image efecto_fracaso = Solid("#ff4444", xsize=200, ysize=200)

# ESCENAS SIMPLES
image negro = Solid("#000000")
image vestuario = Solid("#2c3e50")
image campo atardecer = Solid("#e67e22")
image gimnasio = Solid("#34495e")
image departamento = Solid("#95a5a6")
image parque = Solid("#27ae60")

# PANTALLAS DE INTERFAZ CORREGIDAS
screen barra_progreso_respiracion(actual, objetivo):
    zorder 100
    fixed:
        xalign 0.5 
        yalign 0.1
        vbox:
            text "Progreso de Respiración" size 24 color "#ffffff"
            hbox:
                text "[" size 24 color "#ffffff"
                for i in range(objetivo):
                    if i < actual:
                        text "★" size 24 color "#ffff00"
                    else:
                        text "☆" size 24 color "#ffffff"
                text "]" size 24 color "#ffffff"

screen barra_progreso_fuerza(actual, objetivo):
    zorder 100
    fixed:
        xalign 0.5 
        yalign 0.1
        vbox:
            text "Fuerza Mental" size 24 color "#ffffff"
            hbox:
                text "[" size 24 color "#ffffff"
                for i in range(objetivo):
                    if i < actual:
                        text "●" size 24 color "#00ff00"
                    else:
                        text "○" size 24 color "#ffffff"
                text "]" size 24 color "#ffffff"

# ========== HISTORIA PRINCIPAL ==========

label start:
    scene negro
    "CORAZÓN EN EL CAMPO"
    "Una novela visual sobre fútbol, superación y salud emocional"
    
    jump decision_crucial

label decision_crucial:
    scene vestuario
    show alex pensativo at centrado
    with fade

    "Tres meses después del diagnóstico..."
    "La doctora fue clara: 'Puedes seguir jugando, pero debes aprender a manejar el estrés o tu corazón sufrirá.'"
    
    show entrenador at izquierda with moveinleft
    entrenador "Alex, sé que ha sido difícil. El contrato está sobre la mesa..."
    entrenador "Pero solo tú puedes decidir si vale la pena el riesgo."
    
    hide entrenador with moveoutleft
    show alex mirando_lejos at centrado
    
    "Miro mis botas gastadas. Siento el eco de los aplausos en mi memoria."
    "Por un lado, el miedo a que mi cuerpo no responda..."
    "Por otro, el sueño que he perseguido desde niño."

    menu:
        "Seguir adelante. El fútbol es mi vida.":
            $ eleccion_carrera = True
            jump continuar_carrera
            
        "Retirarme. Mi salud es primero.":
            $ eleccion_carrera = False
            jump retirarse

# ========== FINAL DE RETIRADA ==========

label retirarse:
    scene departamento
    show alex triste at centrado
    with fade
    
    prota "Lo siento... no puedo arriesgarme."
    
    "Devuelvo el contrato sin firmar. Las palabras no salen fácilmente."
    
    show entrenador serio at izquierda with moveinleft
    entrenador "Lo entiendo, Alex. Tu salud es lo más importante."
    entrenador "Siempre serás bienvenido aquí."
    
    "El entrenador se va. El silencio en la habitación es ensordecedor."
    
    # SALTO TEMPORAL - 6 MESES DESPUÉS
    scene negro
    "Seis meses después..."
    
    scene parque
    show alex normal at centrado
    with fade
    
    "La vida continúa. Encuentro un trabajo estable, mis días son tranquilos."
    "Pero cada sábado por la tarde..."
    
    show alex melancolico at centrado
    "Cuando escucho los gritos del estadio cercano..."
    "Cuando veo a niños jugando fútbol en el parque..."
    
    prota "¿Y si hubiera seguido? ¿Qué habría pasado?"
    
    "Ese 'qué tal si' se convierte en una sombra silenciosa."
    "Una pregunta que nunca tendrá respuesta."
    "Aprendo a vivir con ella, pero duele. Duele cada vez que pasa una camiseta de fútbol."
    
    show alex mirando_lejos at centrado
    "Mi corazón está a salvo, pero mi alma... mi alma todavía anhela el campo."
    
    # FINAL TEMPRANO
    "Has elegido la seguridad sobre el sueño."
    "A veces, la vida nos enfrenta a decisiones donde no hay respuestas correctas,"
    "solo diferentes tipos de dolor."
    
    return

# ========== CONTINUAR CARRERA ==========

label continuar_carrera:
    scene campo atardecer
    show alex determinacion at centrado
    with fade
    
    prota "No estoy listo para decir adiós. Tengo que intentarlo."
    
    show entrenador at izquierda with moveinleft
    entrenador "¡Excelente decisión! Comenzaremos con entrenamientos progresivos."
    
    jump nivel_1_entrenamiento

# ========== NIVEL 1 - ENTRENAMIENTO ==========

label nivel_1_entrenamiento:
    scene gimnasio
    show alex normal at centrado
    with fade
    
    entrenador "Bienvenido a tu primer día de entrenamiento controlado, Alex."
    entrenador "Hoy trabajaremos en técnicas de respiración y fuerza mental."
    
    show alex pensativo at centrado
    prota "Entiendo... necesito aprender a manejar el estrés en el campo."
    
    show medico at derecha with moveinright
    medico "Alex, estaré monitoreando tus signos vitales durante todo el proceso."
    medico "Recuerda: si en algún momento te sientes mal, debemos detenernos."
    
    hide medico with moveoutright
    
    # MINIJUEGO DE RESPIRACIÓN
    entrenador "Comencemos con ejercicios de respiración. ¿Listo?"
    
    prota "Sí, estoy listo."
    
    call minijuego_respiracion
    
    # EVALUACIÓN DESPUÉS DEL MINIJUEGO
    if ritmo_cardiaco > 90:
        show medico at derecha with moveinright
        medico "Tu ritmo cardíaco está elevado. Necesitamos hacer una pausa."
        medico "Tómate 5 minutos para recuperarte."
        $ energia -= 10
        hide medico with moveoutright
    else:
        entrenador "¡Buen trabajo! Tu control está mejorando."
        $ confianza += 10
    
    # MINIJUEGO DE FUERZA MENTAL
    entrenador "Ahora trabajemos en tu fortaleza mental."
    
    call minijuego_fuerza
    
    # RESULTADO DEL ENTRENAMIENTO
    show alex aliviado at centrado
    prota "Eso fue intenso, pero me siento... más consciente."
    
    entrenador "Hoy fue un buen comienzo. Mañana continuaremos."
    entrenador "Recuerda aplicar estas técnicas en tu vida diaria."
    
    # ACTUALIZAR ESTADISTICAS
    $ energia -= 20
    $ concentracion += 15
    
    # TRANSICIÓN AL SIGUIENTE DÍA
    scene negro
    "Después del entrenamiento, reflexiono sobre lo aprendido..."
    "La respiración consciente realmente ayuda a calmar los nervios."
    "Pero todavía me preocupa cómo me sentiré en un partido real..."
    
    jump siguiente_etapa

# ========== SIGUIENTE ETAPA ==========

label siguiente_etapa:
    scene vestuario
    show alex normal at centrado
    with fade
    
    "Una semana después..."
    
    show entrenador at izquierda with moveinleft
    entrenador "Alex, has progresado mucho en estos días."
    entrenador "Hoy tendrás tu primera prueba real: un partido de entrenamiento."
    
    show alex pensativo at centrado
    prota "¿Un partido real? ¿Estás seguro?"
    
    entrenador "Sí. La Dra. Silva estará monitoreando todo."
    entrenador "Es hora de aplicar lo que has aprendido."
    
    hide entrenador with moveoutleft
    
    show alex determinacion at centrado
    prota "Está bien... tengo que intentarlo."
    
    "Camino hacia el campo sintiendo cómo mi corazón late con fuerza."
    "Pero esta vez, en lugar de entrar en pánico, recuerdo las técnicas de respiración."
    
    jump partido_entrenamiento

# ========== PARTIDO DE ENTRENAMIENTO ==========

label partido_entrenamiento:
    scene campo atardecer
    show alex concentrado at centrado
    with fade
    
    "El partido comienza. Siento la adrenalina corriendo por mis venas."
    "Pero también siento algo diferente: control."
    
    show entrenador at izquierda with moveinleft
    entrenador "¡Vamos Alex! ¡Concéntrate en tu respiración!"
    
    menu:
        "Aplicar técnicas de respiración durante el juego":
            $ aplico_tecnicas = True
            show alex concentrado at centrado
            prota "Inhalo... cuatro segundos... exhalo... seis segundos..."
            "Mantengo la calma y juego con precisión."
            $ ritmo_cardiaco -= 15
            $ confianza += 20
            $ concentracion += 10
            
        "Jugar de forma instintiva, como antes":
            $ aplico_tecnicas = False
            show alex normal at centrado
            "Juego con intensidad, pero pronto siento la presión."
            "Mi corazón comienza a latir más rápido."
            $ ritmo_cardiaco += 25
            $ energia -= 15
    
    # RESULTADO DEL PARTIDO
    if aplico_tecnicas and ritmo_cardiaco < 100:
        show alex feliz at centrado
        prota "¡Lo logré! Mantuve el control durante todo el partido."
        
        show medico at derecha with moveinright
        medico "Excelente, Alex. Tus signos vitales se mantuvieron estables."
        medico "Estás listo para el siguiente nivel."
        $ confianza += 25
        $ salud_mental += 15
        
    else:
        show alex pensativo at centrado
        prota "Fue difícil... todavía tengo que trabajar más."
        
        show medico at derecha with moveinright
        medico "No te preocupes, es un proceso. Lo importante es que reconoces cuando necesitas calmar."
        medico "Seguiremos trabajando."
        $ confianza += 10
    
    hide medico with moveoutright
    hide entrenador with moveoutleft
    
    jump final_primer_nivel

# ========== FINAL PRIMER NIVEL ==========

label final_primer_nivel:
    scene negro
    "Fin del Primer Nivel"
    
    "Estadísticas Finales:"
    "Energía: [energia]"
    "Concentración: [concentracion]"
    "Ritmo Cardíaco: [ritmo_cardiaco]"
    "Confianza: [confianza]"
    "Salud Mental: [salud_mental]"
    
    "¡Has completado la primera etapa del entrenamiento!"
    "Alex ha aprendido técnicas valiosas para manejar el estrés."
    "El camino es largo, pero va por buen camino."
    
    return

# ========== MINIJUEGOS FÁCILES Y FUNCIONALES ==========

label minijuego_respiracion:
    scene gimnasio
    show alex concentrado at centrado
    
    entrenador "Ejercicio de respiración. Solo elige la opción correcta en cada paso."
    
    $ respiraciones_correctas = 0
    $ objetivo = 3
    
    show screen barra_progreso_respiracion(respiraciones_correctas, objetivo)
    
    while respiraciones_correctas < objetivo:
        if respiraciones_correctas == 0:
            "Paso 1: ¿Cómo debes inhalar para calmarte?"
            menu:
                "Rápidamente y de forma superficial":
                    show circulo_rojo at centrado with hpunch
                    "Incorrecto. La respiración rápida aumenta la ansiedad."
                    $ ritmo_cardiaco += 5
                    hide circulo_rojo
                
                "Lentamente y profundamente":
                    $ respiraciones_correctas += 1
                    show circulo_verde at centrado with dissolve
                    "¡Correcto! La respiración lenta ayuda a calmar el cuerpo."
                    $ ritmo_cardiaco -= 8
                    $ confianza += 5
                    hide circulo_verde
                
                "Aguantando la respiración el mayor tiempo posible":
                    show circulo_rojo at centrado with hpunch
                    "No, aguantar la respiración puede ser peligroso."
                    $ ritmo_cardiaco += 10
                    hide circulo_rojo
        
        elif respiraciones_correctas == 1:
            "Paso 2: ¿Qué hacer si sientes que tu corazón late muy rápido?"
            menu:
                "Respirar más rápido para igualar el ritmo":
                    show circulo_rojo at centrado with hpunch
                    "Eso solo empeoraría la situación."
                    $ ritmo_cardiaco += 8
                    hide circulo_rojo
                
                "Concentrarte en exhalar lentamente":
                    $ respiraciones_correctas += 1
                    show circulo_verde at centrado with dissolve
                    "¡Excelente! La exhalación lenta reduce el ritmo cardíaco."
                    $ ritmo_cardiaco -= 10
                    $ confianza += 8
                    hide circulo_verde
                
                "Dejar de respirar por un momento":
                    show circulo_rojo at centrado with hpunch
                    "Nunca dejes de respirar, es peligroso."
                    $ salud_mental -= 5
                    hide circulo_rojo
        
        else:
            "Paso 3: ¿Cuál es la técnica más efectiva para controlar el estrés?"
            menu:
                "Pensar en todas las cosas que podrían salir mal":
                    show circulo_rojo at centrado with hpunch
                    "Eso solo aumenta la ansiedad."
                    $ salud_mental -= 10
                    hide circulo_rojo
                
                "Respirar contando: 4 segundos inhalar, 6 exhalar":
                    $ respiraciones_correctas += 1
                    show circulo_verde at centrado with dissolve
                    "¡Perfecto! Esta técnica es muy efectiva para la calma."
                    $ ritmo_cardiaco -= 12
                    $ confianza += 10
                    hide circulo_verde
                
                "Ignorar completamente cómo te sientes":
                    show circulo_rojo at centrado with hpunch
                    "Ignorar las emociones no es saludable."
                    $ salud_mental -= 8
                    hide circulo_rojo
        
        $ renpy.pause(1.0, hard=True)
    
    hide screen barra_progreso_respiracion
    show alex aliviado at centrado
    prota "Ahora entiendo cómo controlar mi respiración."
    $ confianza += 15
    return

label minijuego_fuerza:
    scene gimnasio
    show alex concentrado at centrado
    
    entrenador "Ejercicio de fuerza mental. Elige las mejores estrategias."
    
    $ fuerza_lograda = 0
    $ repeticiones = 3
    
    show screen barra_progreso_fuerza(fuerza_lograda, repeticiones)
    
    while fuerza_lograda < repeticiones:
        if fuerza_lograda == 0:
            "¿Cómo manejar la presión durante el entrenamiento?"
            menu:
                "Forzarte al máximo sin importar cómo te sientas":
                    show efecto_fracaso at centrado with hpunch
                    "Forzarte puede llevar a lesiones. Escucha a tu cuerpo."
                    $ energia -= 15
                    $ salud_mental -= 5
                    hide efecto_fracaso
                
                "Establecer metas realistas y progresar gradualmente":
                    $ fuerza_lograda += 1
                    show efecto_exito at centrado with dissolve
                    "¡Excelente! El progreso gradual es clave para el éxito."
                    $ confianza += 10
                    $ energia += 5
                    hide efecto_exito
                
                "Compararte constantemente con otros atletas":
                    show efecto_fracaso at centrado with hpunch
                    "Las comparaciones pueden dañar tu confianza."
                    $ confianza -= 8
                    hide efecto_fracaso
        
        elif fuerza_lograda == 1:
            "¿Qué hacer cuando sientes que no puedes continuar?"
            menu:
                "Gritar y frustrarte":
                    show efecto_fracaso at centrado with hpunch
                    "La frustración no ayuda, solo consume energía."
                    $ salud_mental -= 10
                    $ energia -= 10
                    hide efecto_fracaso
                
                "Tomar un descanso breve y respirar profundamente":
                    $ fuerza_lograda += 1
                    show efecto_exito at centrado with dissolve
                    "¡Perfecto! Los descansos estratégicos son importantes."
                    $ energia += 10
                    $ concentracion += 10
                    hide efecto_exito
                
                "Seguir hasta colapsar":
                    show efecto_fracaso at centrado with hpunch
                    "Colapsar es peligroso. Conoce tus límites."
                    $ salud_mental -= 15
                    $ energia -= 20
                    hide efecto_fracaso
        
        else:
            "¿Cómo mantener la motivación a largo plazo?"
            menu:
                "Pensar solo en ganar trofeos y reconocimiento":
                    show efecto_fracaso at centrado with hpunch
                    "La motivación externa no es sostenible."
                    $ salud_mental -= 5
                    hide efecto_fracaso
                
                "Recordar por qué amas el fútbol y celebrar pequeños logros":
                    $ fuerza_lograda += 1
                    show efecto_exito at centrado with dissolve
                    "¡Maravilloso! La motivación interna es la más poderosa."
                    $ confianza += 15
                    $ salud_mental += 10
                    hide efecto_exito
                
                "Depender completamente de la aprobación del entrenador":
                    show efecto_fracaso at centrado with hpunch
                    "Tu motivación debe venir de ti mismo también."
                    $ confianza -= 5
                    hide efecto_fracaso
        
        $ renpy.pause(1.0, hard=True)
    
    hide screen barra_progreso_fuerza
    
    if fuerza_lograda >= 2:
        show alex feliz at centrado
        prota "¡Me siento más fuerte mentalmente!"
        $ confianza += 20
        $ energia += 10
    else:
        show alex pensativo at centrado
        prota "Todavía tengo que aprender, pero voy por buen camino."
        $ confianza += 10
    
    return