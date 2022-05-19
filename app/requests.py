from .models import Quote
import urllib.request, json 

Random_Quote_Url='http://quotes.stormconsultancy.co.uk/random.json'


def get_quote():
    '''Function that fetches the random json quote'''

    url = Random_Quote_Url

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    quote_details = []

    author = data.get('author')
    quote = data.get('quote')

    new_quote = Quote(author,quote)
    quote_details.append(new_quote)

    return quote_details