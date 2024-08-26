import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

country_codes = ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC', 'SV', 'EE', 'FI', 'FR', 'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI', 'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']

country_names = [
  'andorra', 'argentina', 'australia', 'austria', 'belgium', 'bolivia', 'brazil', 
  'bulgaria', 'canada', 'chile', 'colombia', 'costa rica', 'cyprus', 'czech republic', 
  'denmark', 'dominican republic', 'ecuador', 'el salvador', 'estonia', 'finland', 
  'france', 'germany', 'greece', 'guatemala', 'honduras', 'hong kong', 'hungary', 
  'iceland', 'indonesia', 'ireland', 'italy', 'japan', 'latvia', 'liechtenstein', 
  'lithuania', 'luxembourg', 'malaysia', 'malta', 'mexico', 'monaco', 'netherlands', 
  'new zealand', 'nicaragua', 'norway', 'panama', 'paraguay', 'peru', 'philippines', 
  'poland', 'portugal', 'singapore', 'spain', 'slovakia', 'sweden', 'switzerland', 
  'taiwan', 'turkey', 'united kingdom', 'united states', 'uruguay'
]

country_code_dict = {name: code for name, code in zip(country_codes, country_names)}
print(country_code_dict)
# print(country_code_dict)

country_playlist_ids = {
  'AD': '37i9dQZF1DWSjMbpDBYPob',  # Andorra
  'AR': '37i9dQZEVXbMMy2roB9myp',  # Argentina
  'AU': '37i9dQZF1DX5dSF6LrYhT6',  # Australia
  'AT': '37i9dQZF1DX8Kgdykz6OKj',  # Austria
  'BE': '37i9dQZF1DWWEJlAGA9gs0',  # Belgium
  'BO': '37i9dQZEVXbJqfMFK4d691',  # Bolivia
  'BR': '37i9dQZEVXbMOkSwx5Yb1w',  # Brazil
  'BG': '37i9dQZF1DX7F6T2n2fegs',  # Bulgaria
  'CA': '37i9dQZEVXbKj23U1GF4IR',  # Canada
  'CL': '37i9dQZEVXbL0GavIqMTeb',  # Chile
  'CO': '37i9dQZEVXbOa2lmxNORXQ',  # Colombia
  'CR': '37i9dQZEVXbMZAjGMynsQX',  # Costa Rica
  'CY': '37i9dQZEVXbJlfUljuZExa',  # Cyprus
  'CZ': '37i9dQZEVXbIP3c3fqVrJY',  # Czech Republic
  'DK': '37i9dQZEVXbL3J0k32lWnN',  # Denmark
  'DO': '37i9dQZEVXbKAbrMR8uuf7',  # Dominican Republic
  'EC': '37i9dQZEVXbJlM6nvL1nD1',  # Ecuador
  'SV': '37i9dQZEVXbLxoIml4MYkT',  # El Salvador
  'EE': '37i9dQZEVXbLesry2Qw2xS',  # Estonia
  'FI': '37i9dQZEVXbMxcczTSoGwZ',  # Finland
  'FR': '37i9dQZEVXbIPWwFssbupI',  # France
  'DE': '37i9dQZEVXbJiZcmkrIHGU',  # Germany
  'GR': '37i9dQZEVXbJqdarpmTJDL',  # Greece
  'GT': '37i9dQZEVXbLy5tBFyQvd4',  # Guatemala
  'HN': '37i9dQZEVXbJp9wcIM9Eo5',  # Honduras
  'HK': '37i9dQZEVXbKzcPqZd5gzt',  # Hong Kong
  'HU': '37i9dQZEVXbNHwMxAkvmF8',  # Hungary
  'IS': '37i9dQZEVXbKM896FDX8L1',  # Iceland
  'ID': '37i9dQZEVXbObFQZ3JLcXt',  # Indonesia
  'IE': '37i9dQZEVXbKM896FDX8L1',  # Ireland
  'IT': '37i9dQZEVXbIQnj7RRhdSX',  # Italy
  'JP': '37i9dQZEVXbKXQ4mDTEBXq',  # Japan
  'LV': '37i9dQZEVXbJWuzDrTxbKS',  # Latvia
  'LI': '37i9dQZEVXbKxATQATvTDp',  # Liechtenstein
  'LT': '37i9dQZEVXbMx56Rdq5lwc',  # Lithuania
  'LU': '37i9dQZEVXbKGcyg6TFGx6',  # Luxembourg
  'MY': '37i9dQZEVXbJlfUljuZExa',  # Malaysia
  'MT': '37i9dQZEVXbKD3Gg4q51GG',  # Malta
  'MX': '37i9dQZEVXbO3qyFxbkOE1',  # Mexico
  'MC': '37i9dQZEVXbLiRSasKsNU9',  # Monaco
  'NL': '37i9dQZEVXbKCF6dqVpDkS',  # Netherlands
  'NZ': '37i9dQZEVXbM8SIrkERIYl',  # New Zealand
  'NI': '37i9dQZEVXbKxrZ9z1RwRk',  # Nicaragua
  'NO': '37i9dQZEVXbJvfa0Yxg7E7',  # Norway
  'PA': '37i9dQZEVXbKXQHCU3hNAo',  # Panama
  'PY': '37i9dQZEVXbNXrTQE3bKy4',  # Paraguay
  'PE': '37i9dQZEVXbJfdy5b0KP7W',  # Peru
  'PH': '37i9dQZEVXbNBz9cRCSFkY',  # Philippines
  'PL': '37i9dQZEVXbN6itCcaL3Tt',  # Poland
  'PT': '37i9dQZEVXbKyJS56d1pgi',  # Portugal
  'SG': '37i9dQZEVXbK4gjvS1FjPY',  # Singapore
  'SK': '37i9dQZEVXbKIVTPX9a2Sb',  # Slovakia
  'ES': '37i9dQZEVXbNFJfN1Vw8d9',  # Spain
  'SE': '37i9dQZEVXbLoATJ81JYXz',  # Sweden
  'CH': '37i9dQZEVXbJiyhoAPEfMK',  # Switzerland
  'TW': "37i9dQZEVXbMnZEatlMSiu",  # Taiwan
  'TR': "37i9dQZEVXbM0uI5o1buC5",  # Turkey
  'GB': "37i9dQZEVXbLnolsZ8PSNw",  # United Kingdom
  'US': "37i9dQZEVXbLRQDuF5jeBp",  # United States
  'UY': "37i9dQZEVXbMshHA8tQdF2",  # Uruguay
}

# Replace these with your own credentials
client_id = 'c1299277f7fe442983cd14475743bd9f'
client_secret = '5b59d926cdf246d2a48ace23294317c1'








# Authenticate
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
urls = []
def getTopInCountry(country_code, amount=10):
  #"37i9dQZEVXbMDoHDwVN2tF")  # Daily top 50 global playlist ID
  country = country_code_dict[country_code]
  # country_code = country_code_dict[country]
  id = country_playlist_ids[country_code]
  top_tracks = sp.playlist_tracks(id)

  raw_url = sp.playlist(id)['uri']
  # spotify:playlist:37i9dQZEVXbJiyhoAPEfMK
  # https://open.spotify.com/playlist/37i9dQZEVXbJiyhoAPEfMK
  url = "https://open.spotify.com/playlist/" + raw_url[17:]  
  urls.append(url)
  top_ten_tracks = []
  for i, track in enumerate(top_tracks['items']):
    if i < amount:
      top_ten_tracks.append((track['track']['name'], track['track']['artists'][0]['name'], country))

    else:
      break
  return top_ten_tracks

countries = ["JP", "US","TW"]
playlists = []

def getTopInCountries(countries):
  playlists = []
  final_playlist = []
  for c in countries:
    playlists.append(getTopInCountry(c))

  while len(final_playlist) < 10:
    for pl in playlists:
      while True:
        song = pl.pop(0)
        print(song)
        if song not in final_playlist:
          final_playlist.append(song)
          break
        else:
          continue
  final_playlist = final_playlist[:11]
  return final_playlist
final_playlist = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
# final_playlist = (getTopInCountries(countries))
print(urls)





from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def hello_world():
    print(request.headers)

    data = {
      "song1":final_playlist[0][0],
      "song2":final_playlist[1][0],
      "song3":final_playlist[2][0],
      "song4":final_playlist[3][0],
      "song5":final_playlist[4][0],
      "song6":final_playlist[5][0],
      "song7":final_playlist[6][0],
      "song8":final_playlist[7][0],
      "song9":final_playlist[8][0],
      "song10":final_playlist[9][0],

    }
    return render_template('index.html', data=data)


@app.route('/button_click', methods=['POST'])
def button_click():
  # Call your Python function when the button is clicked
  data = request.get_json()
  print(data)
  countries = data['countries']
  print("staring generating playlist",countries)
  getTopInCountries(countries)
  
  return hello_world()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

