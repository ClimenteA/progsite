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


psiholog_cabinet_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="Daniela Popescu",
        business_type=BizzType.PSIHOLOG,
        main_cta="Te voi ajuta sa te cunosti",
        secondary_cta="Ai ajuns bine aici si esti pe calea cea buna. Primul pas a fost facut. Fa-l pe urmatorul.",
        picture_cta="https://images.pexels.com/photos/2471301/pexels-photo-2471301.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    services=[
        BizzServiceModel(
            name="Sedinta individuala",
            description="""
                O sedinta de 60 de minute in care incercam sa te redescoperim.
                """,
            picture="https://images.pexels.com/photos/4846087/pexels-photo-4846087.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=150,
            currency="RON",
        ),
        BizzServiceModel(
            name="Sedinta de cuplu",
            description="""
                O sedinta de 60 de minute in care incercam sa va redescoperiti.
                """,
            picture="https://images.pexels.com/photos/5217833/pexels-photo-5217833.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=200,
            currency="RON",
        ),
    ],
    testimonials=[
        BizzTestimonial(
            person_name="Alina Dandana",
            occupation="Software developer",
            testimonial="Am scapat de atacurile de panica.",
        ),
        BizzTestimonial(
            person_name="Lidia Lacramioara",
            occupation="Agent comercial",
            testimonial="Am scapat sa-mi tot spuna lumea sa nu mai fiu paranoica :))",
        ),
        BizzTestimonial(
            person_name="Dan Trecusi",
            occupation="Agent Vanzari",
            testimonial="Am reusit sa-mi ating potentialul prin vizitele la doamna pshiholog. Recomand!",
        ),
    ],
    about=AboutModel(
        about_us="""
    Nu as schimba ce fac pentru nimic in lume. Sa ajut oamenii este pasiunea mea.
    """,
        team_picture="https://images.pexels.com/photos/19557233/pexels-photo-19557233/free-photo-of-young-woman-in-a-black-dress-with-open-back-standing-outside.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/jefiR8fiFFJmb1r47",
        google_maps_location_picture="/public/crm/gmaps-iasi-palas.png",
        location_picture="https://images.pexels.com/photos/323705/pexels-photo-323705.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        address="Str. Einstein, Nr. 286, Iasi",
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
