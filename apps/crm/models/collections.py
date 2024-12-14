from common.collections import get_collection, Col


class CRMCol(Col):
    MessagesAdmin = "CRMMessagesAdmin"
    Users = "CRMUsers"
    SiteData = "CRMSiteData"
    TokenBlackList = "CRMTokenBlackList"
    Appointment = "CRMAppointments"


MessagesAdminCol = get_collection(CRMCol.MessagesAdmin)
UsersCol = get_collection(CRMCol.Users)
SiteDataCol = get_collection(CRMCol.SiteData)
AppointmentCol = get_collection(CRMCol.Appointment)
