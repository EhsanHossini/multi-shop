import ghasedakpack
from kavenegar import *
from multi_shop.settings import kavenegar_API
from random import randint
from zeep import Client
#
# sms = ghasedakpack.Ghasedak("638689bb41fa5eae0252c1196953aedd319255aefc9116c099fdf49c0b6de6de")
# sms.verification({'receptor': '09029423024', 'type': '1', 'template': 'Your Template', 'param1': '1234', 'param2': 'Hi'})

#
# def send_otp(mobile, otp):
#     mobile = [mobile, ]
#     try:
#         api = KavenegarAPI(kavenegar_API)
#         params = {
#             'sender': '09029423024',  # optional
#             'receptor': 'mobile',  # multiple mobile number, split by comma
#             'message': 'Your OTP is {}'.format(otp),
#         }
#         response = api.sms_send(params)
#         print("OTP: ", otp)
#         print(response)
#     except APIException as e:
#         print(e)
#     except HTTPException as e:
#         print(e)

# #
# def send_otp_soap(mobile, otp):
#     client = Client('http://api.kavenegar.com/soap/v1.asmx?WSDL')
#     receptor = [mobile, ]
#
#     empty_array_placeholder = client.get_type('ns0:Arrayofstring')
#     receptors = empty_array_placeholder()
#     for item in receptor:
#         receptors['string'].append(item)
#
#     api_key = kavenegar_API
#     message = 'Your OTP is {}'.format(otp),
#     sender = '09029423024'
#     status = 0
#     status_message = ''
#
#     result = client.service.SendSimpleByApiKey(api_key, sender, message, receptors, 0, 1, status, status_message)
#     print(result)
#     print("OTP: ", otp)

#
# def get_random_otp():
#     return randint(1000, 9999)
#
#
# def send_otp_soap(mobile, otp):
#     return None