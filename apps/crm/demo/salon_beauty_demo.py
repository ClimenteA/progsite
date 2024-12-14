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


salon_beauty_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="Adela",
        business_type=BizzType.SALON_BEAUTY,
        main_cta="Ne ocupam de frumusete ❤️",
        secondary_cta="Te vom trata cu atentie si delicatete",
        picture_cta="https://images.pexels.com/photos/620074/pexels-photo-620074.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    services=[
        BizzServiceModel(
            name="Masaj facial",
            description="""
                Masajul facial ajuta la elasticitatea pielii.
                """,
            picture="https://images.pexels.com/photos/3738344/pexels-photo-3738344.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=60,
            currency="RON",
        ),
        BizzServiceModel(
            name="Epilare totala",
            description="""
                Putem inlatura firele de par nedorite din varful picioarelor pana in crestetul capului
                """,
            picture="https://images.pexels.com/photos/5886533/pexels-photo-5886533.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=350,
            currency="RON",
        ),
        BizzServiceModel(
            name="Manichiura",
            description="""
                Punem unghii si iti putem face unghiile.
                """,
            picture="https://images.pexels.com/photos/3997353/pexels-photo-3997353.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=60,
            currency="RON",
        ),
        BizzServiceModel(
            name="Vopsit par",
            description="""
                Alege-ti culoarea dorita din catalogul nostru si noi o vom aplica. 
                """,
            picture="https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=450,
            currency="RON",
        ),
        BizzServiceModel(
            name="Tuns par",
            description="""
                De la un pic din varfuri pana la tunsoare bob. 
                Iti poti alege tunsoarea dorita din catalogul nostru si noi o vom face.
                """,
            picture="https://images.pexels.com/photos/3268732/pexels-photo-3268732.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=300,
            currency="RON",
        ),
    ],
    testimonials=[
        BizzTestimonial(
            person_name="Alexandra Babesu",
            occupation="Software developer",
            testimonial="Prietenul meu nu m-a mai recunoscut! Nu a vrut sa mai iesim la plimbare de teama sa nu ma fure cineva :))",
        ),
        BizzTestimonial(
            person_name="Cosmina Carliont",
            occupation="Manager Kaufland",
            testimonial="Am venit muma padurii si am plecat de la salon Afrodita. Recomand!",
        ),
        BizzTestimonial(
            person_name="Daniela Uitas",
            occupation="Agent Comercial",
            testimonial="Foarte bune fetele! Mergeti cu incredere!",
        ),
    ],
    about=AboutModel(
        about_us="""
        Suntem pasionati de cosmetica si frumusete. 
        De-a lungul anilor multe doamne si domnisoare ne-au trecut pragul si au plecat si mai frumoase.
        """,
        team_picture="https://images.pexels.com/photos/7610405/pexels-photo-7610405.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/jefiR8fiFFJmb1r47",
        google_maps_location_picture="/public/crm/gmaps-iasi-palas.png",
        location_picture="https://images.pexels.com/photos/87223/pexels-photo-87223.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        address="Str. Cireselor, Nr. 10, Iasi",
        phone="074545454545",
        email="adela@gmail.com",
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
