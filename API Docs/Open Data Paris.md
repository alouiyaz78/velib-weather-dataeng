# Vélib API - Bikes and stations - Real-time availability

We will restrict ourselves to stations located in Paris only. The data is refreshed every minute.
The API imposes a limit of 100 results per request, so multiple requests are needed to retrieve data for all stations, using pagination based on the `offset` parameter.

URL: `https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?order_by=capacity%20DESC&limit=100&offset=0&refine=nom_arrondissement_communes%3A%22Paris%22&timezone=Europe%2FParis`

- `stationcode`: station code
- `name`: station name
- `is_installed`: whether the station is installed or not
- `capacity`: total number of docks at the station
- `numdocksavailable`: number of docks available to return a bike
- `numbikesavailable`: number of bikes available for rental
- `mechanical`: number of mechanical bikes available
- `ebike`: number of electric bikes available
- `is_renting`: binary flag indicating whether the station can rent out bikes (is_renting=1 if the station status is Operative)
- `is_returning`: binary flag indicating whether the station can accept returned bikes (is_renting=1 if the station status is Operative)
- `duedate`: timestamp of the last data update
- `lon` and `lat`: geographic coordinates of the station
- `nom_arrondissement_communes`: name of the municipality or district (arrondissement) where the station is located
- `code_insee_commune`: INSEE code of the municipality where the station is located

## Response

```json
{
  "total_count": 994,
  "results": [
    {
      "stationcode": "12507",
      "name": "Hippodrome de Paris Vincennes",
      "is_installed": "OUI",
      "capacity": 105,
      "numdocksavailable": 97,
      "numbikesavailable": 3,
      "mechanical": 2,
      "ebike": 1,
      "is_renting": "NON",
      "is_returning": "NON",
      "duedate": "2026-02-22T18:30:40+00:00",
      "coordonnees_geo": {
        "lon": 2.4502807724015,
        "lat": 48.820484866661
      },
      "nom_arrondissement_communes": "Paris",
      "code_insee_commune": "75056",
      "station_opening_hours": null
    },
    {
      "stationcode": "15104",
      "name": "Hôpital Européen Georges Pompidou",
      "is_installed": "OUI",
      "capacity": 78,
      "numdocksavailable": 0,
      "numbikesavailable": 75,
      "mechanical": 67,
      "ebike": 8,
      "is_renting": "OUI",
      "is_returning": "OUI",
      "duedate": "2026-04-02T07:37:37+00:00",
      "coordonnees_geo": {
        "lon": 2.2753742337227,
        "lat": 48.837695319163
      },
      "nom_arrondissement_communes": "Paris",
      "code_insee_commune": "75056",
      "station_opening_hours": null
    },
    ...
  ]
}
```