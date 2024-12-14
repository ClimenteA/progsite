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


optica_medicala_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="OpticFreak",
        business_type=BizzType.OPTICA,
        main_cta="Hai sa vezi mai bine",
        secondary_cta="Vino la noi sa-ti faci o pereche noua de ochelari de vedere.",
        picture_cta="https://images.pexels.com/photos/975668/pexels-photo-975668.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    services=[
        BizzServiceModel(
            name="Consultatie",
            description="""
                Intai trebuie sa vedem ce dioptrii ai nevoie.
                """,
            picture="https://images.pexels.com/photos/5752309/pexels-photo-5752309.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=0,
            currency="RON",
        ),
        BizzServiceModel(
            name="Ochelari de vedere",
            description="""
                Preturile pentru ochelarii de vedere pleaca de la 450 RON. 
                """,
            picture="https://images.pexels.com/photos/5766609/pexels-photo-5766609.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=450,
            currency="RON",
        ),
    ],
    testimonials=[
        BizzTestimonial(
            person_name="Adrian Repodan",
            occupation="Instalator",
            testimonial="Acum vad 3D si in High Definition. Recomand! Totul a fost foarte rapid si eficient.",
        ),
        BizzTestimonial(
            person_name="George Barves",
            occupation="Manager Kaufland",
            testimonial="Stam cu ochii in ecrane toata ziua. Din fericire avem metode de a imbunatatii vederea. Recomand!",
        ),
        BizzTestimonial(
            person_name="Costi Ionescu",
            occupation="Agent Vanzari",
            testimonial="Recomand!",
        ),
        BizzTestimonial(
            person_name="Alin Dragdin",
            occupation="Software Developer",
            testimonial="Aici voi veni si urmatoarea data cand voi avea nevoie de ochelari!",
        ),
    ],
    about=AboutModel(
        about_us="""
        Tratam cu grija fiecare caz. Toti clientii pe care i-am avut sunt multumiti. 
        """,
        team_picture="https://images.pexels.com/photos/6749753/pexels-photo-6749753.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/jefiR8fiFFJmb1r47",
        google_maps_location_picture="/public/crm/gmaps-iasi-palas.png",
        location_picture="https://images.pexels.com/photos/65438/pexels-photo-65438.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        address="Str. Cuacazelor, Nr. 56, Iasi",
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
