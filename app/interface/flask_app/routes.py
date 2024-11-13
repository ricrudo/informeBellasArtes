from flask import redirect, url_for

def go_to(origen, action):
    '''
    Apartir de una lista definida con el orden de las paginas redirige al usuario, dependiendo de back o next a otra pagina
    '''
    pages = [
        'inicio.sections_menu',
        'inicio.informacion_docente',
        'docencia.func_misional_docencia',
        'docencia.participa_procesos_curriculares',
        'investigacion.part_grupos_investigacion',
        'investigacion.redes_academicas_profesores',
        'investigacion.desarollo_proyectos_investigacion_creacion',
        'investigacion.productos_creacion',
        'investigacion.publicacion_articulos',
        'investigacion.publicacion_libros',
        'investigacion.part_eventos_academicos',
        'investigacion.convenios_productos_redes',
        'investigacion.patentes_derechos_autor',
        'investigacion.direcion_tesis',
        'investigacion.evaluacion_tesis',
        'investigacion.coordinacion_semilleros',
        'investigacion.convocatorias_semilleros',
        'investigacion.movilidad_estudiantes_semilleros',
        'investigacion.jovenes_investigadores_apoyados',
        'investigacion.otras_actividades_investigacion_extension_creacion',
        'investigacion.otras_actividades_recursos_estrategias',
        'ext_y_proy.propuestas_educacion',
        'ext_y_proy.gestion_convenios',
        'ext_y_proy.proyeccion_poblacion_priorizada',
        'bienestar.asignacion_misional_bienestar',
        'bienestar.atendidos_bienestar'
    ]
    index_origen = pages.index(origen)
    if not 'action':
        return redirect(url_for(pages[next_pag]))
    elif action == 'back':
        next_pag = index_origen - 1 if index_origen > 0 else index_origen 
    elif action == 'next':
        next_pag = index_origen + 1 if index_origen + 1 < len(pages) else index_origen
    else:
        next_pag = index_origen
    return redirect(url_for(pages[next_pag]))


