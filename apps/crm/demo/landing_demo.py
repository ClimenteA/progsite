from apps.crm.models.sitedata import (
    TIMEUNIT,
    BizzServiceModel,
    SiteDataModel,
    ExternalLinkModel,
    BizzType,
    CTAModel,
    AboutModel,
    ContactModel,
    WorkingScheduleModel,
    TimeFrameModel,
)


landing_site_data = SiteDataModel(
    call_to_action=CTAModel(
        business_name="progsite",
        business_type=BizzType.SITE_PREZENTARE,
        main_cta="Site + programări online pentru afacerea ta 🚀",
        secondary_cta="Ajută clienții să te aleagă pe tine mai ușor. Îți oferim un website de prezentare cu programări online incluse!",
        picture_cta="/public/crm/landing-hero.png",
    ),
    services=[
        BizzServiceModel(
            name="Site prezentare de bază",
            description="""
                Cu doar 15 EURO pe lună, ai inclus un website de prezentare al afacerii tale. 
                Îți poți personaliza website-ul cum dorești (imagini, text). 
                Suma se plătește pentru pachetul de 1 an (REDUCERE 10 EURO pe lună pentru pachetul de 2 ani).
                Gazduirea websitului este inclusa.
                """,
            picture="/public/crm/wireframe.jpg",
            price=15,
            currency="EUR",
            time_unit=TIMEUNIT.MINUTES,
            time_value=30,
        ),
        BizzServiceModel(
            name="Programări online direct pe site",
            description="""
                Clienții pot face programări online direct de pe site. 
                Astfel, vei avea toate programările într-un singur loc pentru tine sau toată echipa ta. 
                Clienții pot face programări și în afara orelor de program - gata cu întreruperile în timp ce lucrezi. 
                Acest beneficiu este inclus în site-ul de prezentare de bază!
                """,
            picture="/public/crm/women-on-phone.jpg",
            price=0,
            currency="EUR",
        ),
        BizzServiceModel(
            name="Banner Anunțuri",
            description="""
                Poți pune pe site diverse anunțuri, de exemplu: Promoții, program de sărbători sau alte comunicări. 
                Anunțurile pot avea o dată de expirare. Acest beneficiu este inclus în site-ul de prezentare de bază!
                """,
            picture="/public/crm/megaphone-yell.jpg",
            price=0,
            currency="EUR",
        ),
        BizzServiceModel(
            name="Website de prezentare personalizat",
            description="""
                Website-ul inclus în pachet este de cele mai multe ori suficient. 
                Însă, dacă vă doriți un website care să reprezinte și mai mult valoarea pe care o puteți oferi clienților, 
                vă putem ajuta cu un website special făcut pentru afacerea dumneavoastră.
                """,
            picture="/public/crm/html-code-link.jpg",
            price=5000,
            currency="EUR",
        ),
    ],
    testimonials=None,
    about=AboutModel(
        about_us="""
        Suntem o echipă din Iași, activând în mediul online de câțiva ani. 
        Am putea spune că ne pricepem la ce facem, 
        dar asta depinde pe cine întrebați 😂. 
        În loc să ne lăudăm noi, preferăm să lăsăm produsele noastre să vorbească de la sine. 
        De exemplu, 
        acest website este un exemplu concret al expertizei și angajamentului nostru 🤓.
        """,
        team_picture="/public/crm/simal.jpg",
    ),
    contact=ContactModel(
        google_maps_location_link="https://maps.app.goo.gl/k7oM9NDqbshboqu98",
        google_maps_location_picture="/public/crm/iasi.png",
        location_picture="/public/crm/earth-from-moon.jpg",
        address="Iasi",
        phone=None,
        email="alinclimente@softgata.com",
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
    external_links=[
        ExternalLinkModel(
            name="Service Auto",
            link="/crm/site-demo/auto-repair",
        ),
        ExternalLinkModel(
            name="Cabinet Dentar",
            link="/crm/site-demo/dentist-cabinet",
        ),
        ExternalLinkModel(
            name="Cabinet Veterinar",
            link="/crm/site-demo/veterinary-cabinet",
        ),
        ExternalLinkModel(
            name="Salon Beauty",
            link="/crm/site-demo/salon-beauty",
        ),
        ExternalLinkModel(
            name="Barber Shop",
            link="/crm/site-demo/barber-shop",
        ),
        ExternalLinkModel(
            name="Salon Tatuaje",
            link="/crm/site-demo/tatoo",
        ),
        ExternalLinkModel(
            name="Cabinet Pshiholog",
            link="/crm/site-demo/psiholog-cabinet",
        ),
        ExternalLinkModel(
            name="Optica Medicala",
            link="/crm/site-demo/optica-medicala",
        ),
        ExternalLinkModel(
            name="Recuperare Medicala",
            link="/crm/site-demo/recuperare-medicala",
        ),
    ],
)
