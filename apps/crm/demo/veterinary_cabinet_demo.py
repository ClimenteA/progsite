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


veterinary_cabinet_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="HappyPet",
        business_type=BizzType.VETERINARY,
        main_cta="Pai.. nu-s si ei oameni? 😊",
        secondary_cta="Daca crezi ca animalutzul tau se simte rau vino cu el la noi sa-l facem bine.",
        picture_cta="https://images.unsplash.com/photo-1453227588063-bb302b62f50b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    ),
    services=[
        BizzServiceModel(
            name="Consultatie",
            description="""
                Primul pas este sa vedem care este problema si cum o putem rezolva.
                """,
            picture="https://images.pexels.com/photos/6235241/pexels-photo-6235241.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=35,
            currency="RON",
        ),
        BizzServiceModel(
            name="Deparazitari",
            description="""
                Hai la noi sa-ti scapam micul prieten de vizitatorii nedoriti.
                """,
            picture="https://images.unsplash.com/photo-1574342467132-e25a78ed99b8?q=80&w=1938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            price=150,
            currency="RON",
        ),
        BizzServiceModel(
            name="Vaccinari caini si pisici",
            description="""
                O data pe an este recomandat ca animalele de casa sa fie vaccinate pentru sanatatea ambelor parti.
                """,
            picture="https://images.pexels.com/photos/3825529/pexels-photo-3825529.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=100,
            currency="RON",
        ),
        BizzServiceModel(
            name="Castrare caini si pisici",
            description="""
                Atunci cand animalutul intra in calduri este va fi foarte greu de controlat. 
                Este recomandat sa veniti cu animalutul cat mai curand (daca a ajuns la 6 luni puteti veni cu el/ea). 
                """,
            picture="https://images.unsplash.com/photo-1547955922-85912e223015?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            price=230,
            currency="RON",
        ),
    ],
    testimonials=[
        BizzTestimonial(
            person_name="Alina Dandana",
            occupation="Software developer",
            testimonial="Au fost foarte atenti cu pisicuta mea. Pisicuta s-a simtit ca acasa.",
        ),
        BizzTestimonial(
            person_name="Lidia Lacramioara",
            occupation="Agent comercial",
            testimonial="""Nu stiam ce are pisicul meu. Tot mieuna prin casa si nu mai facea la litiera. 
            Dupa ce l-am castrat totul a fost ok si pentru mine, dar si pentru el.""",
        ),
        BizzTestimonial(
            person_name="Dan Trecusi",
            occupation="Agent Vanzari",
            testimonial="Vizita la veterinar acum nu mai este asa infricosatoare.",
        ),
    ],
    about=AboutModel(
        about_us="""
    Iubim necuvantatoarele si ii tratam cu cea mai mare placere. Vream ca fiecare animalut sa plece mult mai bine de la noi.
    """,
        team_picture="https://images.pexels.com/photos/7465698/pexels-photo-7465698.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/jefiR8fiFFJmb1r47",
        google_maps_location_picture="/public/crm/gmaps-iasi-palas.png",
        location_picture="https://images.pexels.com/photos/323705/pexels-photo-323705.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        address="Str. Ciurbei, Nr. 286, Iasi",
        phone="0745454545",
        email="contact@gmail.com",
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
