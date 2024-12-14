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


tatoo_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="Tattat",
        business_type=BizzType.TATOO,
        main_cta="Mereu tatuaje profesionale ♠️",
        secondary_cta="Artistii nostri iti pot imprima orice tatuaj preferat",
        picture_cta="https://images.unsplash.com/photo-1620705921541-5b276d7dcdd9?q=80&w=1949&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    ),
    services=[
        BizzServiceModel(
            name="Tatuaj Negru Gri",
            description="""
                Pretul minim este de 180 RON si creste cu 4 RON pe centrimetru patrat de piele
                """,
            picture="https://images.unsplash.com/photo-1513078094721-e7b6e0394a6a?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            price=180,
            currency="RON",
        ),
        BizzServiceModel(
            name="Reimprospatare Tatuaj",
            description="""
                Pretul de 4 RON este pe centrimetru patrat de piele
                """,
            picture="https://images.unsplash.com/photo-1594091360183-4793f2dac6e6?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            price=4,
            currency="RON",
        ),
    ],
    testimonials=[
        BizzTestimonial(
            person_name="Adrian Repodan",
            occupation="Instalator",
            testimonial="De mult vroiam sa-mi fac un tatuaj. Am fost foarte multumit de treaba facuta!",
        ),
        BizzTestimonial(
            person_name="Bogdan Barves",
            occupation="Manager Kaufland",
            testimonial="Foarte buni. Recomand!",
        ),
        BizzTestimonial(
            person_name="Alexandra Privieru",
            occupation="Manager corporatie",
            testimonial="Mi-a placut foarte mult cum a iesit tatuajul. E exact ce vroiam!",
        ),
    ],
    about=AboutModel(
        about_us="""
        Suntem artisti. Un tatuaj este modul nostru de a ne exprima. 
        """,
        team_picture="https://images.unsplash.com/photo-1511632765486-a01980e01a18?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/jefiR8fiFFJmb1r47",
        google_maps_location_picture="/public/crm/gmaps-iasi-palas.png",
        location_picture="https://images.pexels.com/photos/65438/pexels-photo-65438.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        address="Str. Capsunilor, Nr. 10, Iasi",
        phone="074545454545",
        email="tattat@gmail.com",
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
