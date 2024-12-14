from apps.crm.models.sitedata import (
    BizzServiceModel,
    BizzTestimonial,
    AnnouncementModel,
    SiteDataModel,
    BizzType,
    CTAModel,
    AboutModel,
    ContactModel,
    WorkingScheduleModel,
    TimeFrameModel,
)


dentist_cabinet_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="CariiPA",
        business_type=BizzType.DENTIST,
        main_cta="Hai sa-ti aducem zambetul inapoi",
        secondary_cta="Te scapam fara durere de problemele dentare",
        picture_cta="https://images.unsplash.com/photo-1606811841689-23dfddce3e95?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    ),
    services=[
        BizzServiceModel(
            name="Consultatie",
            description="""
                Primul pas este sa vedem care este problema si cum o putem rezolva.
                """,
            picture="https://images.unsplash.com/photo-1606811971618-4486d14f3f99?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            price=100,
            currency="RON",
        ),
        BizzServiceModel(
            name="Tratare carie superficiala",
            description="""
                Cariile superficiale nu au ajuns inca sa afecteze radacina dintelui acestea se pot trata din fericire intr-o singura sedinta.
                """,
            picture="https://img.freepik.com/free-vector/cartoon-teeth-decay-with-bacteria-white-background_1308-94182.jpg?w=1380&t=st=1704012602~exp=1704013202~hmac=17944272a711a03f360045211f765e293433c8426e2cf1f1cbf4fb448350326f",
            price=150,
            currency="RON",
        ),
        BizzServiceModel(
            name="Tratare carie si canale dentare",
            description="""
                Cariile adanci afecteaza din pacate si radacina dintelui. 
                In functie de pozitia dintelui va trebui sa tratam de la 1 la 3 canale pentru fiecare dinte. 
                """,
            picture="https://img.freepik.com/free-vector/caries-inflammation-gums-white-background_1308-105594.jpg?w=740&t=st=1704012830~exp=1704013430~hmac=1edf1233d190cfc23a93fffcaf5063c4bbc270d7ed1d8b2fd86cd75682363fbe",
            price=500,
            currency="RON",
        ),
        BizzServiceModel(
            name="Coroana dentara metalo-ceramica",
            description="""
                Cariile poti distruge din pacate tot dintele. 
                Daca radacina dintelui este sanatoasa putem aplica o coroana dentara.
                """,
            picture="https://img.freepik.com/free-vector/caries-inflammation-gums-white-background_1308-105594.jpg?w=740&t=st=1704012830~exp=1704013430~hmac=1edf1233d190cfc23a93fffcaf5063c4bbc270d7ed1d8b2fd86cd75682363fbe",
            price=780,
            currency="RON",
        ),
        BizzServiceModel(
            name="Coroana dentara ceramica",
            description="""
                Cariile poti distruge din pacate tot dintele. 
                Daca radacina dintelui este sanatoasa putem aplica o coroana dentara.
                """,
            picture="https://img.freepik.com/free-vector/caries-inflammation-gums-white-background_1308-105594.jpg?w=740&t=st=1704012830~exp=1704013430~hmac=1edf1233d190cfc23a93fffcaf5063c4bbc270d7ed1d8b2fd86cd75682363fbe",
            price=1750,
            currency="RON",
        ),
        BizzServiceModel(
            name="Implant dentar",
            description="""
                In unele cazuri dintele este complet distrus de carii si nu mai poate fi recuperat.
                In aceasta situatie daca osul maxilar sau mandibula este sanatos putem face un implant dentar.
                """,
            picture="https://img.freepik.com/free-vector/dental-implant-tooth-set-closeup-model_1284-15060.jpg?w=826&t=st=1704013091~exp=1704013691~hmac=4033879d32664b81ce94be1b9800285daf49c249192be667579148bbe57a27c5",
            price=2800,
            currency="RON",
        ),
        BizzServiceModel(
            name="Detartraj si Periaj profesional",
            description="""
                Acest serviciu te scapa de respiratia urat mirositoare, dintii galbeni si riscul de carii.
                """,
            picture="https://images.unsplash.com/photo-1626736985932-c0df2ae07a2e?q=80&w=1931&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            price=250,
            currency="RON",
        ),
        BizzServiceModel(
            name="Extractie dentara",
            description="""
                Daca dintele nu mai poate fi recuperat trebuie sa-l scoatem pentru a prevenii o infectie.
                """,
            picture="https://images.pexels.com/photos/19557431/pexels-photo-19557431/free-photo-of-closeup-of-a-woman-at-having-dental-treatment.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            price=70,
            currency="RON",
        ),
        BizzServiceModel(
            name="Proteza dentara",
            description="""
                Proteza dentara este o alternativa mai ieftina a implantului dentar.
                """,
            picture="https://images.unsplash.com/photo-1612736777093-461fb48101d7?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            price=4600,
            currency="RON",
        ),
    ],
    testimonials=[
        BizzTestimonial(
            person_name="Alin Randas",
            occupation="Software developer",
            testimonial="Surprinzator nu m-a durut nimic!",
        ),
        BizzTestimonial(
            person_name="Lidia Lacramioara",
            occupation="Agent comercial",
            testimonial="Acum pot sa sparg samburi de masline cu dintii noi!",
        ),
        BizzTestimonial(
            person_name="Dan Trecusi",
            occupation="Agent Vanzari",
            testimonial="Vizita la dentist acum nu mai este asa infricosatoare.",
        ),
        BizzTestimonial(
            person_name="Cornelia Gurmand",
            occupation="Compliance Agent",
            testimonial="Mergeti cu incredere! Totul a fost peste asteptari!",
        ),
        BizzTestimonial(
            person_name="Georgiana Dorof",
            occupation="Manager Regional",
            testimonial="Sper sa nu mai vin, dar imi plac dulciurile asa ca inevitabil voi alege sa vin din nou tot aici!",
        ),
    ],
    about=AboutModel(
        about_us="""
    Activam din 2003 si de atunci multi pacienti ne-au trecut pragul. 
    Putem spune ca toti au plecat cu zambetul pe buze si fara dureri.     
    """,
        team_picture="https://images.pexels.com/photos/3845723/pexels-photo-3845723.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/jefiR8fiFFJmb1r47",
        google_maps_location_picture="/public/crm/gmaps-iasi-palas.png",
        location_picture="https://images.pexels.com/photos/3800464/pexels-photo-3800464.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        address="Str. Ciurbei, Nr. 286, Iasi",
        phone="0745454545",
        email="cariipa@gmail.com",
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
    external_links=None,
)
