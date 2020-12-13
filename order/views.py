# from rest_framework.response import Response
# from rest_framework.views import APIView
# from paycomuz.status import ORDER_FOUND, ORDER_NOT_FOND, INVALID_AMOUNT
# from paycomuz.methods_subscribe_api import Paycom
#
# class PayPay:
#     def __init__(self, order_id=None, order_type=None, amount=None):
#         self.order_id = None  # buyurtmaning raqami
#         self.order_type = None  # buyurtmaning turi yozilmasayam boladi
#         self.amount = None  # buyurtmaning narxi
#
#     def check_order(self):
#         print(self.order_id)
#         print(self.order_type)
#         print(self.amount)
#
#         return ORDER_FOUND
#         # if self.order == True:  # bazada xudi wunday buyurtma bor narxi xam tori keladi
#         #     return ORDER_FOUND
#         # else:  # agar bunday buyurtma bolmasa
#         #     return ORDER_NOT_FOND  # yoki INVALID_AMOUNT #narxi tori kelmadi
#
# class Payment(APIView):
#     def get(self, request):
#         token = 'NTg0YTg0ZDYyYWJiNWNhYTMxMDc5OTE0X1VnYU02ME92IUttWHVHRThJODRJNWE0Xl9EYUBPQCZjNSlPRlpLIWNWRz1PNFp6VkIpZU0kQjJkayoyVUVtUuKElmt4JTJYWj9VQGNAQyVqT1pOQ3VXZ2NyajBEMSYkYj0kVj9NXikrJE5HNiN3K25pKHRQOEVwOGpOcUYxQ2dtemk9dDUwKDNATjd2XythbibihJYoJispJUtuREhlaClraGlJWTlLMihrLStlRjd6MFI3VCgjVDlpYjQ1ZThaMiojPVNTZylYJlFWSjlEZGFuSjZDNDJLdlhXP3YmV1B2dkRDa3g5X2l4N28oU0pOVEpSeXZKYnkjK0h3ViZfdmlhUHMp'
#         data = Paycom(order_id=123, amount=5000.00, token=token).cards_verify()
#         print(data)
#         return Response(data)

from paycomuz.views import MerchantAPIView
from paycomuz.methods_subscribe_api import Paycom


class CheckOrder(Paycom):
    def check_order(self, amount, account):
        return self.ORDER_FOUND

class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder

# paycom = Paycom()
#
# # Create Card
# amount = 5000.00
# card = paycom.create_cards(card_number='8600 0691 9540 6311', expire='03/99', amount=amount, save=False)
# print(card)
# #token1 = 'NTg0YTg0ZDYyYWJiNWNhYTMxMDc5OTE0X1VnYU02ME92IUttWHVHRThJODRJNWE0Xl9EYUBPQCZjNSlPRlpLIWNWRz1PNFp6VkIpZU0kQjJkayoyVUVtUuKElmt4JTJYWj9VQGNAQyVqT1pOQ3VXZ2NyajBEMSYkYj0kVj9NXikrJE5HNiN3K25pKHRQOEVwOGpOcUYxQ2dtemk9dDUwKDNATjd2XythbibihJYoJispJUtuREhlaClraGlJWTlLMihrLStlRjd6MFI3VCgjVDlpYjQ1ZThaMiojPVNTZylYJlFWSjlEZGFuSjZDNDJLdlhXP3YmV1B2dkRDa3g5X2l4N28oU0pOVEpSeXZKYnkjK0h3ViZfdmlhUHMp'
# token = card['token']
# verify = paycom.cards_verify(code='code', token=token)
# print(verify)

# Create Transaction
# result = paycom.create_transaction(token=token, order_id=1, amount=amount)
# print(result)