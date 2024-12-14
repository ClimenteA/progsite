from apps.crm.demo.auto_repair_demo import auto_repair_site_data
from apps.crm.demo.dentist_cabinet_demo import dentist_cabinet_site_data
from apps.crm.demo.veterinary_cabinet_demo import veterinary_cabinet_site_data
from apps.crm.demo.salon_beauty_demo import salon_beauty_site_data
from apps.crm.demo.barber_shop_demo import barber_shop_site_data
from apps.crm.demo.tatoo_demo import tatoo_site_data
from apps.crm.demo.psiholog_cabinet_demo import psiholog_cabinet_site_data
from apps.crm.demo.optica_medicala_demo import optica_medicala_site_data
from apps.crm.demo.recuperare_medicala_demo import recuperare_medicala_site_data
from apps.crm.demo.landing_demo import landing_site_data
from apps.crm.demo.build_demo import build_site_data

demo_sites_mapper = {
    "auto-repair": auto_repair_site_data.model_dump(),
    "dentist-cabinet": dentist_cabinet_site_data.model_dump(),
    "veterinary-cabinet": veterinary_cabinet_site_data.model_dump(),
    "salon-beauty": salon_beauty_site_data.model_dump(),
    "barber-shop": barber_shop_site_data.model_dump(),
    "tatoo": tatoo_site_data.model_dump(),
    "psiholog-cabinet": psiholog_cabinet_site_data.model_dump(),
    "optica-medicala": optica_medicala_site_data.model_dump(),
    "recuperare-medicala": recuperare_medicala_site_data.model_dump(),
    "landing": landing_site_data.model_dump(),
    "build-site": build_site_data.model_dump(),
}


demo_sites_mapper_ro = {
    "SERVICE AUTO": demo_sites_mapper["auto-repair"],
    "CABINET DENTAR": demo_sites_mapper["dentist-cabinet"],
    "CABINET VETERINAR": demo_sites_mapper["veterinary-cabinet"],
    "SALON BEAUTY": demo_sites_mapper["salon-beauty"],
    "BARBER SHOP": demo_sites_mapper["barber-shop"],
    "TATUAJE": demo_sites_mapper["tatoo"],
    "CABINET PSIHOLOGIC": demo_sites_mapper["psiholog-cabinet"],
    "OPTICA MEDICALA": demo_sites_mapper["optica-medicala"],
    "RECUPERARE MEDICALA": demo_sites_mapper["recuperare-medicala"],
}
