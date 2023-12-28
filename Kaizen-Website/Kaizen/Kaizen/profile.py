from scholarly import GoogleSearch


params = {
    "engine": "google_scholar_profiles",
    "mauthors: "Ma.Cecilia A. Venal",
    "api_key": "secret_api_key",
}

search = GoogleSearch(params)
results = search.get_dict()
profiles = results["profiles"]