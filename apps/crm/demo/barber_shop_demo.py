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


barber_shop_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="Barbes",
        business_type=BizzType.BARBER_SHOP,
        main_cta="Hai sa te imbarbatam 💪",
        secondary_cta="Cum te ingrijesti poate lasa o impresie buna sau rea. Noi vom face in asa fel incat sa lasi o impresie buna oriunde te-ai duce.",
        picture_cta="https://images.unsplash.com/photo-1529947708452-a843ff7e74f6?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    ),
    services=[
        BizzServiceModel(
            name="Tuns spalat si frezat",
            description="""
                Setul complet de ingrijire par.
                """,
            picture="https://images.pexels.com/photos/1570807/pexels-photo-1570807.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=85,
            currency="RON",
        ),
        BizzServiceModel(
            name="Trim si barbierit",
            description="""
                Iti facem barba de razboinic
                """,
            picture="https://images.pexels.com/photos/897262/pexels-photo-897262.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=60,
            currency="RON",
        ),
    ],
    testimonials=[
        BizzTestimonial(
            person_name="Adrian Repodan",
            occupation="Instalator",
            testimonial="Femeia mea nu ma mai lasa sa ies din casa dupa ce am fost la ei.",
        ),
        BizzTestimonial(
            person_name="Bogdan Barves",
            occupation="Manager Kaufland",
            testimonial="Am luat interviul la un job. Cred ca si din cauza ca am aratat top. Recomand!",
        ),
        BizzTestimonial(
            person_name="Costi Ionescu",
            occupation="Agent Vanzari",
            testimonial="Am fost in multe locuri sa ma tund, dar de acum doar aici voi veni!",
        ),
        BizzTestimonial(
            person_name="Alin Dragdin",
            occupation="Software Developer",
            testimonial="Nu va mai tundeti acasa baieti! Veniti aici!",
        ),
    ],
    about=AboutModel(
        about_us="""
        Ne place sa aratam bine pentru orice situatie. Suntem cei mai buni in domeniu.
        """,
        team_picture="https://images.pexels.com/photos/1813272/pexels-photo-1813272.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/jefiR8fiFFJmb1r47",
        google_maps_location_picture="/public/crm/gmaps-iasi-palas.png",
        location_picture="https://images.pexels.com/photos/65438/pexels-photo-65438.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        address="Str. Cireselor, Nr. 10, Iasi",
        phone="074545454545",
        email="barbes@gmail.com",
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
