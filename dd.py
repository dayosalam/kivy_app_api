import requests
import pandas as pd

class InfaktAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.infakt.pl/v3/clients.json"
        self.headers = {
            "X-inFakt-ApiKey": api_key,
            "Content-Type": "application/json"
        }

    def get_clients_data(self):
        response = requests.get(self.url, headers=self.headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
            return None

    def extract_data(self, response_data):
        id = []
        company_name = []
        street = []
        street_number = []
        flat_number = []
        city = []
        country = []
        postal_code = []
        nip = []
        phone_number = []
        web_site = []
        email = []
        note = []
        receiver = []
        mailing_company_name = []
        mailing_street = []
        mailing_city = []
        mailing_postal_code = []
        days_to_payment = []
        payment_method = []
        invoice_note = []
        same_forward_address = []
        first_name = []
        last_name = []
        business_activity_kind = []

        for item in response_data['entities']:
            id.append(item['id'])
            company_name.append(item['company_name'])
            street.append(item['street'])
            street_number.append(item['street_number'])
            flat_number.append(item['flat_number'])
            city.append(item['city'])
            country.append(item['country'])
            postal_code.append(item['postal_code'])
            nip.append(item['nip'])
            phone_number.append(item['phone_number'])
            web_site.append(item['web_site'])
            email.append(item['email'])
            note.append(item['note'])
            receiver.append(item['receiver'])
            mailing_company_name.append(item['mailing_company_name'])
            mailing_street.append(item['mailing_street'])
            mailing_city.append(item['mailing_city'])
            mailing_postal_code.append(item['mailing_postal_code'])
            days_to_payment.append(item['days_to_payment'])
            payment_method.append(item['payment_method'])
            invoice_note.append(item['invoice_note'])
            same_forward_address.append(item['same_forward_address'])
            first_name.append(item['first_name'])
            last_name.append(item['last_name'])
            business_activity_kind.append(item['business_activity_kind'])

            data = {
    'id': id,
    'company_name': company_name,
    'street': street,
    'street_number': street_number,
    'flat_number': flat_number,
    'city': city,
    'country': country,
    'postal_code': postal_code,
    'nip': nip,
    'phone_number': phone_number,
    'web_site': web_site,
    'email': email,
    'note': note,
    'receiver': receiver,
    'mailing_company_name': mailing_company_name,
    'mailing_street': mailing_street,
    'mailing_city': mailing_city,
    'mailing_postal_code': mailing_postal_code,
    'days_to_payment': days_to_payment,
    'payment_method': payment_method,
    'invoice_note': invoice_note,
    'same_forward_address': same_forward_address,
    'first_name': first_name,
    'last_name': last_name,
    'business_activity_kind': business_activity_kind
}
        return data

    def create_dataframe(self, data):
        df = pd.DataFrame(data)
        return df

    def save_to_csv(self, df, file_path='clients_data.csv'):
        df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # Initialize the API client
    api_key = "7834d6a3c32107f015127e06cd8c95f7c5b5b015"
    infakt_api_client = InfaktAPIClient(api_key)

    # Get data from the API
    api_response_data = infakt_api_client.get_clients_data()

    if api_response_data:
        # Extract and organize data
        extracted_data = infakt_api_client.extract_data(api_response_data)

        # Create a DataFrame
        df = infakt_api_client.create_dataframe(extracted_data)

        # Save the DataFrame to a CSV file
        infakt_api_client.save_to_csv(df)
