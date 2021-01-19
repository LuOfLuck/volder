window.sr = ScrollReveal();
    // definimos time y suma, time marcar como tiempo inicial y suma para la diferencia de tiempo entre cada animacion
    suma = 300;
    time = 0;

    //header
    sr.reveal('.header-animacion', {
        duration: 1500,
        origin: 'bottom',
        distance: '-10px'
    });
    //botones de la izquieda
    sr.reveal('.contenedor-animacion', {
        delay: time,
        duration: 2000,
        origin: 'right',
        distance: '-50px'
    });
    time += suma;
    //botones de la izquieda
    sr.reveal('.boton-animacion', {
        delay: time,
        duration: 2000,
        origin: 'right',
        distance: '-50px'
    });
    time += suma;
    //meditad, o sea el contenido
    sr.reveal('.mid-contenido-animacion', {
        delay: time,
        duration: 2000,
        origin: 'top',
        distance: '-50px'
    });
    time += suma;
    //lo de adentro del contenido, osea ultimos trabajos
    sr.reveal('.tarea-animacion', {
        delay: time,
        duration: 2000,
        origin: 'top',
        distance: '-50px'
    });
    time += suma;

    //derecha. tu perfil
    sr.reveal('.container-animacion', {
        delay: time,
        duration: 2000,
        origin: 'left',
        distance: '-50px'
    });
    time += suma;
    //compañeros de clase
    sr.reveal('.compañeros-animacion', {
        delay: time,
        duration: 2000,
        origin: 'left',
        distance: '-50px'
    });


    sr.reveal('.tarea2-animacion', {
        delay: 200,
        duration: 1000,
        origin: 'top',
        distance: '-50px'
    });
    sr.reveal('.footer', {
        delay: 200,
        duration: 1000,
        origin: 'top',
        distance: '-50px'
    });

