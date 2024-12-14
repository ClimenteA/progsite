from apps.crm.models.sitedata import (
    AnnouncementModel,
    BizzServiceModel,
    BizzTestimonial,
    BizzType,
    ExternalLinkModel,
    SiteDataModel,
    CTAModel,
    AboutModel,
    ContactModel,
    WorkingScheduleModel,
    TimeFrameModel,
)


build_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="BestAuto",
        business_type=BizzType.AUTO,
        main_cta="Reparam autovehicule de cat.B",
        secondary_cta="Probabil cei mai buni din Iasi la treaba asta :)",
        picture_cta="https://images.unsplash.com/photo-1615906655593-ad0386982a0f?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    ),
    services=[
        BizzServiceModel(
            name="Diagnosticare",
            description="""
                Nu am fost noi la Facultatea de Medicina sa ne facem doctori, dar putem spune ca suntem doctori pentru autovehicule. 
                Suspectezi o problema la masina hai sa identificam problema si sa o rezolvam.
                """,
            picture="https://images.unsplash.com/photo-1618445902270-40c36803f5b0?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            price=125,
            currency="RON",
        ),
        BizzServiceModel(
            name="Reparatii mecanice",
            description="""
                Dispunem de echipamente de ultima generatie. Nu exista defectiune pe care sa nu o putem remedia.
                """,
            picture="https://images.unsplash.com/photo-1625047509168-a7026f36de04?q=80&w=2080&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ),
        BizzServiceModel(
            name="Reglare geometrie roti",
            description="""
                Tii volanul drept si autovehiculul vrea sa mearga la dreapta? Trebuie neaparat sa-ti faci o programare la noi!
                """,
            picture="https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ),
    ],
    testimonials=[
        BizzTestimonial(
            person_name="Andrei Costarca",
            occupation="Software developer",
            testimonial="Sunt niste profesionisti!",
        ),
        BizzTestimonial(
            person_name="Raluca Cimpoiesu",
            occupation="Manager Kaufland",
            testimonial="Nici o reclamatie de facut. Recomand acest service auto!",
        ),
        BizzTestimonial(
            person_name="Jorche Mandelas",
            occupation="Director",
            testimonial="Nu stiu prea bene romena, dar problema s-a rezolvat! Multumesc!",
        ),
        BizzTestimonial(
            person_name="Dani Disco",
            occupation="Proprietar Club",
            testimonial="Am o masina scumpa.. un Aston Martin. Baietii au fost TOP si au reusit sa-mi rezolve problema. Recomand!",
        ),
        BizzTestimonial(
            person_name="Marian Sapanta",
            occupation="Manager Regional",
            testimonial="E adevarat dureaza un pic mai mult, dar de fiecare data si-au facut treaba foarte bine.",
        ),
    ],
    about=AboutModel(
        about_us="""
        Suntem pe piata din 2010. Avem deja experienta cu sute de clienti. 
        Multi dintre ei s-au reintors la noi datorita serviciilor de inalta calitate oferite.
        """,
        team_picture="https://images.pexels.com/photos/14908958/pexels-photo-14908958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/jefiR8fiFFJmb1r47",
        google_maps_location_picture="/public/crm/gmaps-iasi-palas.png",
        location_picture="https://images.pexels.com/photos/10131851/pexels-photo-10131851.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        address="Str. Coacazelor, Nr. 123, Iasi",
        phone="074545454545",
        email="bestauto@gmail.com",
    ),
    working_schedule=WorkingScheduleModel(
        monday_entries=[
            TimeFrameModel(
                start="08:00",
                stop="17:00",
            )
        ],
        tuesday_entries=[
            TimeFrameModel(
                start="08:00",
                stop="17:00",
            )
        ],
        wednesday_entries=[
            TimeFrameModel(
                start="08:00",
                stop="17:00",
            )
        ],
        thursday_entries=[
            TimeFrameModel(
                start="08:00",
                stop="17:00",
            )
        ],
        friday_entries=[
            TimeFrameModel(
                start="08:00",
                stop="17:00",
            )
        ],
        saturday_entries=None,
        sunday_entries=None,
        mentions="Inchis in zilele libere de la stat.",
    ),
    external_links=[
        ExternalLinkModel(
            name="Reparatii alternatoare",
            link="https://www.youtube.com/watch?v=LGB6ZEjGm7Q&list=RDQMajeSP3P2mGo&start_radio=1",
        ),
        ExternalLinkModel(
            name="Schimbare curea distributie",
            link="https://www.youtube.com/watch?v=heBAwFB1_Ys",
        ),
    ],
)
