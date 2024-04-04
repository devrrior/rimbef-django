import logging
from io import StringIO
from typing import Any, List
from fauna.apps.species import models

import pandas as pd

logger = logging.getLogger(__name__)


def _generate_species_data_from_file_record(file: Any) -> List[dict]:
    df = pd.read_excel(file, engine="openpyxl", header=0, sheet_name='ESPECIES')
    # df = df.fillna("")
    df = df.apply(lambda x: x.astype(str).str.strip())
    df = df.apply(lambda x: x.astype(str).str.upper())

    writer_file = StringIO()
    df.to_csv(writer_file)
    writer_file.seek(0)

    return df.to_dict("records")


def add_massive_data(data):
    success_rows = 0
    errors_rows = 0

    for item in data:
        try:
            taxon_id = int(item["TAXON_ID"])
            scientific_name = item["NOMBRE_CIENTIFICO"].upper()
            common_name = item["NOMBRE_COMUN"].upper()
            uicn = item["UICN"]
            distribution = item["DISTRIBUCION"]
            invasion = item["INVASION"]
            specie = models.Specie.objects.filter(scientific_name=scientific_name).last()

            if specie is None:

                # agregar validaciones de datos obligatorios

                kingdom, kingdom_created = models.Kingdom.objects.get_or_create(name=item["REINO"].upper())
                kingdom = kingdom if kingdom else kingdom_created

                phylum, phylum_created = models.Phylum.objects.get_or_create(name=item["PHYLUM"].upper(), kingdom=kingdom)
                phylum = phylum if phylum else phylum_created

                specie_class, specie_class_created = models.SpecieClass.objects.get_or_create(name=item["CLASE"].upper(),
                                                                                              ecology_group=item["GRUPO_ECOLOGICO"].upper(),
                                                                                              phylum=phylum)
                specie_class = specie_class if specie_class else specie_class_created

                order, order_created = models.Order.objects.get_or_create(name=item["ORDEN"].upper(), specie_class=specie_class)
                order = order if order else order_created

                family, family_created = models.Family.objects.get_or_create(name=item["FAMILIA"].upper(), order=order)
                family = family if family else family_created

                genus, genus_created = models.Genus.objects.get_or_create(name=item["GENERO"].upper(), family=family)
                genus = genus if genus else genus_created

                social_structure, social_structure_created = models.SocialStructure.objects.get_or_create(name=item["ESTRUCTURA_SOCIAL"].upper())
                social_structure = social_structure if social_structure else social_structure_created

                trophic_guild, trophic_guild_created = models.TrophyGuild.objects.get_or_create(name=item["GREMIO_TROFICO"].upper())
                trophic_guild = trophic_guild if trophic_guild else trophic_guild_created

                models.Specie.objects.create(scientific_name=scientific_name,
                                             common_name=common_name,
                                             uicn=uicn,
                                             distribution=distribution,
                                             invasion=invasion,
                                             genus=genus,
                                             social_structure=social_structure,
                                             trophic_guild=trophic_guild,
                                             taxon_id_rimfeb=taxon_id
                                             )

                success_rows += 1
        except Exception as e:
            print(e)
            print("--------------------------")
            errors_rows += 1
            continue

    return {"success": success_rows, "errors": errors_rows}
