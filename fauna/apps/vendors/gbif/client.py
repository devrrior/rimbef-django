import pandas as pd
from pygbif import occurrences as occ
from fauna.apps.species import models as spc_models
from fauna.apps.observations import models as obs_models
import os
import requests
import json
import logging
import datetime

logger = logging.getLogger(__name__)


class Gbif:

    def __init__(self) -> None:
        self.user = os.environ["GBIF_USER"]
        self.password = os.environ["GBIF_PASSWORD"]
        self.email = os.environ["GBIF_EMAIL"]

    def set_data(self):
        yesterday_date = datetime.date.today() - datetime.timedelta(days=1)
        yesterday_date_str = str(yesterday_date)
        # active_phylums = spc_models.Phylum.objects.filter(status=1)
        phylums_codes = ['44', '52', '54']

        for item in phylums_codes:
            try:
                data = occ.search(phylumKey=item,
                                  eventDate=yesterday_date_str,
                                  country='CO',  # filtro por pais
                                  gadmLevel1Gid="COL.5_2",  # filtro por ciudad (bogotà)
                                )
                obs_models.Observation.objects.filter(observation_date=yesterday_date).delete()

                if "count" in data and data["count"] > 0:
                    results = data["results"]

                    for res in results:
                        specie = spc_models.Specie.objects.filter(scientific_name=res["scientificName"].upper(), status=1).last()
                        if specie is not None:
                            try:
                                observation = obs_models.Observation.objects.create(specie=specie,
                                                                                    observation_date=yesterday_date,
                                                                                    observation_type=res["basisOfRecord"],
                                                                                    place=res["verbatimLocality"],
                                                                                    latitude=str(res["decimalLatitude"]),
                                                                                    longitude=str(res["decimalLongitude"]),
                                                                                    url_web=res["references"],
                                                                                    url_photo=res["media"][0]["identifier"],
                                                                                    license=res["license"]
                                                                      )
                                source, source_created = obs_models.Source.objects.get_or_create(name=res["institutionCode"].upper())
                                source = source if source else source_created
                                observation.sources.add(source.id)
                            except Exception as e:
                                print(str(e))
                                continue
                        else:
                            print("---NO EXISTE LA ESPECIE: ", res["scientificName"].upper())
            except Exception as e:
                print(str(e))
                continue


