from scholarly import GoogleSearch


params = {
    "engine": "google_scholar_profiles",
    "mauthors: "Ma.Cecilia A. Venal",
    "api_key": "secret_api_key",
}

search = GoogleSearch(params)
profiles = search.get_hash[:profiles]