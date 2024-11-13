from app.interface import db
from app.domain import models
from pathlib import Path
from datetime import date



class TestBlog:
    def setup_class(self):
        db.Base.metadata.create_all(db.engine)

        self.session = db.Session()
        #self.valid_author = Author(
        #    firstname="Ezzeddin",
        #    lastname="Aybak",
        #    email="aybak_email@gmail.com"
        #)

    def teardown_class(self):
        self.session.rollback()
        self.session.close()
        r = input('\n\nDesea eliminar la base de datos creada:')
        if r.strip().lower() == 'y':
            path_db = Path.cwd() / 'bellasartes_test.sqlite'
            if path_db.exists(): path_db.unlink()

    def test_person_valid(self):
        valid_person = models.Person(
            first_names = 'Ricardo Eduardo',
            last_names = 'Ost Bers',
            admin_role = True,
            max_education = 'magister',
            facultad = 'Bellas Artes',
            programas = 'musica'
        )
        self.session.add(valid_person)
        self.session.commit()
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        assert p.first_names == 'Ricardo Eduardo'
        assert p.last_names == 'Ost Bers'
        assert p.admin_role == True
        assert p.max_education == 'magister'
        assert p.facultad == 'Bellas Artes'
        assert p.programas == 'musica'

    def test_login_valid(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_login = models.Login(
            email = 'ricar@asd.com',
            password = '1234',
            id_person = p.id
        )
        self.session.add(valid_login)
        self.session.commit()
        r = self.session.query(models.Login).filter_by(id_person=p.id).first()
        assert r.email == 'ricar@asd.com'
        assert r.password == '1234'

    def test_Misional_docencia_1(self):
        '''
        creacion minima
        '''
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.MisionalDocencia(
            materia = 'Orquestación I',
            code = '123498',
            programa = 'Música',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.MisionalDocencia).filter_by(id_person=p.id).first()
        assert r.materia == 'Orquestación I'
        assert r.code == '123498'
        assert r.programa == 'Música'

    def test_Misional_docencia_2(self):
        '''
        creacion con status_done
        '''
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.MisionalDocencia(
            materia = 'Orquestación II',
            code = '12349812',
            programa = 'Música',
            status_done = True,
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.MisionalDocencia).filter_by(id_person=p.id, code='12349812').first()
        assert r.materia != 'Orquestación I'
        assert r.code == '12349812'
        assert r.programa == 'Música'
        assert r.status_done == True

    def test_Misional_docencia_3(self):
        '''
        modificacion de informacion
        '''
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        r = self.session.query(models.MisionalDocencia).filter_by(id_person=p.id, code='12349812').first()
        r.estudiantes_total = 12
        r.observaciones = 'estan son observaciones de prueba que pueden ser o no ser'
        r.contenidos_especiales = 'la materia no contiene elementos de este tipo'
        r.estudiantes_pass = 5
        self.session.commit()
        t = self.session.query(models.MisionalDocencia).filter_by(id_person=p.id, code='12349812').first()
        assert t.materia != 'Orquestación I'
        assert t.materia == 'Orquestación II'
        assert t.estudiantes_total == 12
        assert t.estudiantes_pass == 5
        assert t.status_done == True
        assert r.observaciones == 'estan son observaciones de prueba que pueden ser o no ser'
        assert r.contenidos_especiales == 'la materia no contiene elementos de este tipo'


    def test_Part_ProcesosCurriculares(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.Part_ProcesosCurriculares(
            name_proceso = 'C',
            program_misional = 'programa',
            status_done = False,
            observaciones = 'estan son observaciones de prueba que pueden ser o no ser',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.Part_ProcesosCurriculares).filter_by(id_person=p.id).first()
        assert r.name_proceso == 'C'
        assert r.program_misional == 'programa'
        assert r.status_done == False
        assert r.observaciones == 'estan son observaciones de prueba que pueden ser o no ser'

    def test_GruposInvestigacion(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.GruposInvestigacion(
            grupo = 'Feliza Nosequien',
            linea_investiga = 'creación digital',
            programa = 'música',
            actividades = 'todas las actividades que pueden ser o no ser',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.GruposInvestigacion).filter_by(id_person=p.id).first()
        assert r.grupo == 'Feliza Nosequien'
        assert r.linea_investiga == 'creación digital'
        assert r.programa == 'música'
        assert r.actividades == 'todas las actividades que pueden ser o no ser'

    def test_RedesAcademicas(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.RedesAcademicas(
            name_red = 'C',
            link = 'www.link_red_academica.com/user',
            update_date = date(2023, 12, 23),
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.RedesAcademicas).filter_by(id_person=p.id).first()
        assert r.name_red == 'C'
        assert r.link == 'www.link_red_academica.com/user'
        assert r.update_date == date(2023, 12, 23)

    def test_ProyectosInvestigacionCreacion(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.ProyectosInvestigacionCreacion(
            grupo = 'sam',
            code = '12323',
            tipo_convocatoria = 'I',
            nombre_convocatoria = 'este es el nombre de la convocatoria',
            elegido = True,
            financiamiento = 'entidad que financia',
            co_investigadores = '',
            ods = False,
            software = False,
            idi5 = True,
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.ProyectosInvestigacionCreacion).filter_by(id_person=p.id).first()
        assert r.grupo == 'sam'
        assert r.code == '12323'
        assert r.tipo_convocatoria == 'I'
        assert r.nombre_convocatoria == 'este es el nombre de la convocatoria'
        assert r.elegido == True
        assert r.financiamiento == 'entidad que financia'
        assert r.co_investigadores == ''
        assert r.ods == False
        assert r.software == False
        assert r.idi5 == True

    def test_ProductosCreacion(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.ProductosCreacion(
            tipo_producto = 'evento',
            nombre_producto = 'este es el nombre',
            institucion = 'esta es la institucion',
            alcance = 'L',
            fecha = date(2023, 12, 23),
            link = 'www.link.com/adsfa',
            categoria = 'A',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.ProductosCreacion).filter_by(id_person=p.id).first()
        assert r.tipo_producto == 'evento'
        assert r.nombre_producto == 'este es el nombre'
        assert r.institucion == 'esta es la institucion'
        assert r.alcance == 'L'
        assert r.fecha == date(2023, 12, 23)
        assert r.link == 'www.link.com/adsfa'
        assert r.categoria == 'A'

    def test_PublicacionArticulos(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.PublicacionArticulos(
            titulo = 'titulo trabajo',
            autores = 'autores',
            revista = 'esta es la revista',
            link = 'link de',
            fecha = date(2023, 12, 23) ,
            issn = '12340129341234',
            index_revista = 'A',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.PublicacionArticulos).filter_by(id_person=p.id).first()
        assert r.titulo == 'titulo trabajo'
        assert r.autores == 'autores'
        assert r.revista == 'esta es la revista'
        assert r.link == 'link de'
        assert r.fecha == date(2023, 12, 23) 
        assert r.issn == '12340129341234'
        assert r.index_revista == 'A'

    def test_PublicacionLibros(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.PublicacionLibros(
            titulo = 'titulo trabajo',
            autores = 'autores',
            editorial = 'esta es la editorial',
            fecha = date(2023, 12, 23),
            issn = '12340129341234',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.PublicacionLibros).filter_by(id_person=p.id).first()
        assert r.titulo == 'titulo trabajo'
        assert r.autores == 'autores'
        assert r.editorial == 'esta es la editorial'
        assert r.fecha == date(2023, 12, 23) 
        assert r.issn == '12340129341234'

    def test_ParticipacionEventos(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.ParticipacionEventos(
            titulo = 'titulo evento',
            evento = 'este es el nombre del evento',
            lugar = 'este es el lugar',
            fecha = date(2023, 12, 23),
            tipo_participacion = 'este es el tipo de participacion',
            modalidad = 'P',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.ParticipacionEventos).filter_by(id_person=p.id).first()
        assert r.titulo == 'titulo evento'
        assert r.evento == 'este es el nombre del evento'
        assert r.lugar == 'este es el lugar'
        assert r.fecha == date(2023, 12, 23)
        assert r.tipo_participacion == 'este es el tipo de participacion'
        assert r.modalidad == 'P'

    def test_ConveniosInterinstitucionales(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.ConveniosInterinstitucionales(
            convenio = 'este es el convenio',
            producto = 'este es el producto',
            grupo = 'este es el grupo',
            impacto = 'este es el impacto',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.ConveniosInterinstitucionales).filter_by(id_person=p.id).first()
        assert r.convenio == 'este es el convenio'
        assert r.producto == 'este es el producto'
        assert r.grupo == 'este es el grupo'
        assert r.impacto == 'este es el impacto'
    
    def test_Patentes(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.Patentes(
            tipo_producto = 'este es el tipo de producto',
            registro = 'este es el registro',
            fecha = date(2023, 12, 23),
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.Patentes).filter_by(id_person=p.id).first()
        assert r.tipo_producto == 'este es el tipo de producto'
        assert r.registro == 'este es el registro'
        assert r.fecha == date(2023, 12, 23)
    
    def test_DireccionTesis(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.DireccionTesis(
            titulo = 'este es el titulo de la tesis',
            estudiante = 'este es el nomvre del estudiante',
            nivel_formacion = 'P',
            programa = 'musica',
            institucion = 'aca fue',
            status = 'ok',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.DireccionTesis).filter_by(id_person=p.id).first()
        assert r.titulo == 'este es el titulo de la tesis'
        assert r.estudiante == 'este es el nomvre del estudiante'
        assert r.nivel_formacion == 'P'
        assert r.programa == 'musica'
        assert r.institucion == 'aca fue'
        assert r.status == 'ok'

    
    def test_EvaluacionTesis(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.EvaluacionTesis(
            titulo = 'este es el titulo de la tesis',
            estudiante = 'este es el nomvre del estudiante',
            asesor = 'este es el nombre del asesor',
            nivel_formacion = 'P',
            programa = 'musica',
            institucion = 'aca fue',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.EvaluacionTesis).filter_by(id_person=p.id).first()
        assert r.titulo == 'este es el titulo de la tesis'
        assert r.estudiante == 'este es el nomvre del estudiante'
        assert r.asesor == 'este es el nombre del asesor'
        assert r.nivel_formacion == 'P'
        assert r.programa == 'musica'
        assert r.institucion == 'aca fue'
    
    def test_CoordSemilleros(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.CoordSemilleros(
            nombre = 'Nombre de la persona',
            total_integrantes = 9,
            nuevos_integrantes = 2,
            grupo = 'sam',
            programa = 'musica',
            update_SIA = False,
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.CoordSemilleros).filter_by(id_person=p.id).first()
        assert r.nombre == 'Nombre de la persona'
        assert r.total_integrantes == 9
        assert r.nuevos_integrantes == 2
        assert r.grupo == 'sam'
        assert r.programa == 'musica'
        assert r.update_SIA == False
    
    def test_ConvocatoriasSemilleros(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.ConvocatoriasSemilleros(
            semillero = 'nombre del semillero',
            tipo_convovatoria = 'I',
            nombre = 'nombre de la convocatoria',
            proyecto = 'nombre del proyecto',
            participantes = 'nombre de todos los participantes',
            fecha = date(2023, 12, 23),
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.ConvocatoriasSemilleros).filter_by(id_person=p.id).first()
        assert r.semillero == 'nombre del semillero'
        assert r.tipo_convovatoria == 'I'
        assert r.nombre == 'nombre de la convocatoria'
        assert r.proyecto == 'nombre del proyecto'
        assert r.participantes == 'nombre de todos los participantes'
        assert r.fecha == date(2023, 12, 23)
    
    def test_MovilidadEstudiantesSemilleros(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.MovilidadEstudiantesSemilleros(
            semillero = 'nombre del semillero',
            evento = 'nombre del evento',
            proyecto = 'nombre del proyecto',
            lugar = 'lugar de la movilidad',
            fecha = date(2023,12,12),
            estudiantes = 'nombre de todos los estudiantes',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.MovilidadEstudiantesSemilleros).filter_by(id_person=p.id).first()
        assert r.semillero == 'nombre del semillero'
        assert r.evento == 'nombre del evento'
        assert r.proyecto == 'nombre del proyecto'
        assert r.lugar == 'lugar de la movilidad'
        assert r.fecha == date(2023,12,12)
        assert r.estudiantes == 'nombre de todos los estudiantes'
    
    def test_JovenesInvestigadores(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.JovenesInvestigadores(
            convocatoria = 'nombre de la convocatoria',
            estudiantes = 'nombre de los estudiantes',
            programa = 'musica',
            tutor = 'nombre del tutor',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.JovenesInvestigadores).filter_by(id_person=p.id).first()
        assert r.convocatoria == 'nombre de la convocatoria'
        assert r.estudiantes == 'nombre de los estudiantes'
        assert r.programa == 'musica'
        assert r.tutor == 'nombre del tutor'
    
    def test_OtrasInvestigacion(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.OtrasInvestigacion(
            tipo_actividad = 'este es el tipo de actividad',
            nombre = 'este es el nombre del producto',
            institucion = 'esta es la institucion',
            actividades = 'esta es la actividad',
            detalles = 'estos son los detalles',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.OtrasInvestigacion).filter_by(id_person=p.id).first()
        assert r.tipo_actividad == 'este es el tipo de actividad'
        assert r.nombre == 'este es el nombre del producto'
        assert r.institucion == 'esta es la institucion'
        assert r.actividades == 'esta es la actividad'
        assert r.detalles == 'estos son los detalles'
    
    def test_OtrasRecursos(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.OtrasRecursos(
            tipo_recurso = 'D',
            programa = 'nombre del programa',
            nombre = 'nombre del recurso',
            impacto = 'definicion del impacto',
            fecha = date(2023, 12, 12),
            detalles = 'estas son detalles',
            ofertado_por = 'este es quien oferta',
            finalizado = False,
            alcance = 'N',
            observaciones = 'estas son observaciones',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.OtrasRecursos).filter_by(id_person=p.id).first()
        assert r.tipo_recurso == 'D'
        assert r.programa == 'nombre del programa'
        assert r.nombre == 'nombre del recurso'
        assert r.impacto == 'definicion del impacto'
        assert r.fecha == date(2023, 12, 12)
        assert r.detalles == 'estas son detalles'
        assert r.ofertado_por == 'este es quien oferta'
        assert r.finalizado == False
        assert r.alcance == 'N'
        assert r.observaciones == 'estas son observaciones'
    
    def test_PropuestasEducacion(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.PropuestasEducacion(
            nombre = 'Nombre de la propuesta',
            tipo_propuesta = 'T',
            fecha_inicio = date(2023,10,12),
            fecha_fin = date(2023,12,14),
            modalidad = 'S',
            internacional = True,
            diferencial = '',
            entidad_convenio = 'nombre de la entidad con el convenio',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.PropuestasEducacion).filter_by(id_person=p.id).first()
        assert r.nombre == 'Nombre de la propuesta'
        assert r.tipo_propuesta == 'T'
        assert r.fecha_inicio == date(2023,10,12)
        assert r.fecha_fin == date(2023,12,14)
        assert r.modalidad == 'S'
        assert r.internacional == True
        assert r.diferencial == ''
        assert r.entidad_convenio == 'nombre de la entidad con el convenio'
        assert r.id_person == p.id
    
    def test_GestionConvenios(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.GestionConvenios(
            entidad = 'nombre de la entidad',
            actividades = 'nombre de la actividad',
            tipo_vinculo = 'C',
            beneficiarios = 'D',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.GestionConvenios).filter_by(id_person=p.id).first()
        assert r.entidad == 'nombre de la entidad'
        assert r.actividades == 'nombre de la actividad'
        assert r.tipo_vinculo == 'C'
        assert r.beneficiarios == 'D'
    
    def test_ProyeccionPoblacionPriorizada(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.ProyeccionPoblacionPriorizada(
            nombre_proyecto = 'este es el nombre del proyecto',
            fecha_inicio = date(2023, 12, 12),
            beneficiarios = 'estos son los beneficiarios',
            participantes = 'estos son los participantes',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.ProyeccionPoblacionPriorizada).filter_by(id_person=p.id).first()
        assert r.nombre_proyecto == 'este es el nombre del proyecto'
        assert r.fecha_inicio == date(2023, 12, 12)
        assert r.beneficiarios == 'estos son los beneficiarios'
        assert r.participantes == 'estos son los participantes'
    
    def test_AsignacionMisionalBienestar(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.AsignacionMisionalBienestar(
            representante_misional = True,
            tutor_rendimiento = False,
            tutor_SAT = False,
            coordinador = False,
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.AsignacionMisionalBienestar).filter_by(id_person=p.id).first()
        assert r.representante_misional == True
        assert r.tutor_rendimiento == False
        assert r.tutor_SAT == False
        assert r.coordinador == False
    
    def test_AtendidosBienestar(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.AtendidosBienestar(
            tipo_atencion = 'R',
            nombre_persona = 'este es el nombre de la persona',
            superado = False,
            detalles = 'estos son los detalles',
            remision = True,
            estrategias = 'estas son las estrategias',
            observaciones = 'estas son las observaciones',
            id_person = p.id
        )
        self.session.add(valid_data)
        self.session.commit()
        r = self.session.query(models.AtendidosBienestar).filter_by(id_person=p.id).first()
        assert r.tipo_atencion == 'R'
        assert r.nombre_persona == 'este es el nombre de la persona'
        assert r.superado == False
        assert r.detalles == 'estos son los detalles'
        assert r.remision == True
        assert r.estrategias == 'estas son las estrategias'
        assert r.observaciones == 'estas son las observaciones'
    
