from paycomuz.methods_subscribe_api import Paycom
paycom = Paycom()

# Create Card
amount = 5000.00
card = paycom.create_cards(card_number='8600 0691 9540 6311', expire='03/99', amount=amount, save=False)
print(card)
#token1 = 'NTg0YTg0ZDYyYWJiNWNhYTMxMDc5OTE0X1VnYU02ME92IUttWHVHRThJODRJNWE0Xl9EYUBPQCZjNSlPRlpLIWNWRz1PNFp6VkIpZU0kQjJkayoyVUVtUuKElmt4JTJYWj9VQGNAQyVqT1pOQ3VXZ2NyajBEMSYkYj0kVj9NXikrJE5HNiN3K25pKHRQOEVwOGpOcUYxQ2dtemk9dDUwKDNATjd2XythbibihJYoJispJUtuREhlaClraGlJWTlLMihrLStlRjd6MFI3VCgjVDlpYjQ1ZThaMiojPVNTZylYJlFWSjlEZGFuSjZDNDJLdlhXP3YmV1B2dkRDa3g5X2l4N28oU0pOVEpSeXZKYnkjK0h3ViZfdmlhUHMp'
token = card['token']
verify = paycom.cards_verify(code='code', token=token)
print(verify)

# Create Transaction
# result = paycom.create_transaction(token=token, order_id=1, amount=amount)
# print(result)