from apps.crm.models.sitedata import (
    BizzServiceModel,
    BizzTestimonial,
    SiteDataModel,
    BizzType,
    CTAModel,
    AboutModel,
    ContactModel,
    WorkingScheduleModel,
    TimeFrameModel,
)


recuperare_medicala_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="RestoreHealth",
        business_type=BizzType.RECUPERARE_MEDICALA,
        main_cta="Te facem ca nou",
        secondary_cta="Fie ca ai avut un accident si trebuie sa-ti recuperezi mobilitatea sau statul la birou iti provoaca dureri de spate - poti veni cu incredere la noi.",
        picture_cta="https://images.pexels.com/photos/2678059/pexels-photo-2678059.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    services=[
        BizzServiceModel(
            name="Consultatie",
            description="""
                Iti facem un consult si iti vom oferi un plan de actiune.
                """,
            picture="https://images.pexels.com/photos/5473223/pexels-photo-5473223.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=160,
            currency="RON",
        ),
        BizzServiceModel(
            name="Fizioterapie si kinetoterapie",
            description="""
                O sedinta personalizata pentru problemele tale alaturi de un specialist.
                """,
            picture="https://images.pexels.com/photos/6111616/pexels-photo-6111616.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=200,
            currency="RON",
        ),
    ],
    testimonials=[
        BizzTestimonial(
            person_name="Adrian Repodan",
            occupation="Instalator",
            testimonial="Statul la birou m-a costat cu o durere insuportabila de spate. Alaturi de specialistii de la RestoreHealth mi-am revenit!",
        ),
        BizzTestimonial(
            person_name="George Barves",
            occupation="Manager Kaufland",
            testimonial="Recomand! Am avut un accident cu bicicleta si nu mai puteam sa calc pe piciorul stang. Acum pot!",
        ),
    ],
    about=AboutModel(
        about_us="""
        Tratam cu grija fiecare caz. Toti clientii pe care i-am avut sunt multumiti. 
        """,
        team_picture="https://images.pexels.com/photos/4506107/pexels-photo-4506107.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/jefiR8fiFFJmb1r47",
        google_maps_location_picture="/public/crm/gmaps-iasi-palas.png",
        location_picture="https://images.pexels.com/photos/65438/pexels-photo-65438.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        address="Str. Caiselor, Nr. 56, Iasi",
        phone="074545454545",
        email="opticfreak@gmail.com",
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
    announcement=None,
    external_links=None,
)
