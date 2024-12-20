from typing import Dict, List

from long_term_uc.common.fuel_sources import FuelSources


gps_coords = (0, 0)  # Your choice!


def get_generators(country_trigram: str, fuel_sources: Dict[str, FuelSources],
                   wind_on_shore_data, wind_off_shore_data, solar_pv_data) -> List[dict]:
    """
    Get list of generators to be set on a given node of a PyPSA model
    :param country_trigram: name of considered country, as a trigram (ex: "ben", "fra", etc.)
    :param fuel_sources
    """
    
    # 2025 data by hand
    generators = [
        
    ]
    
    # 2025 data
    generators = [
    {"name": f"Hard-Coal_{country_trigram}", "carrier": "Coal", "p_nom": 866.6,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Coal"].primary_cost * 0.37,
        "efficiency": 0.37, "committable": False},
    {"name": f"Gas_{country_trigram}", "carrier": "Gas", "p_nom": 3324.86,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Gas"].primary_cost * 0.5,
        "efficiency": 0.5, "committable": False},
    {"name": f"Oil_{country_trigram}", "carrier": "Oil", "p_nom": 1580.0,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Oil"].primary_cost * 0.4,
        "efficiency": 0.4, "committable": False},
    # {"name": f"Other-non-renewables_{country_trigram}",
    #     "carrier": "Other-non-renewables", "p_nom": 735.5, "p_min_pu": 0,
    #     "p_max_pu": 1, "marginal_cost": fuel_sources["Other-non-renewables"].primary_cost * 0.4,
    #     "efficiency": 0.4, "committable": False},
    {"name": f"Wind-on-shore_{country_trigram}", "carrier": "Wind",
        "p_nom": 39318.31, "p_min_pu": 0, "p_max_pu": wind_on_shore_data["value"].values,
        "marginal_cost": fuel_sources["Wind"].primary_cost, "efficiency": 1,
        "committable": False},
    {"name": f"Wind-off-shore_{country_trigram}", "carrier": "Wind",
        "p_nom": 2447.3, "p_min_pu": 0, "p_max_pu": wind_off_shore_data["value"].values,
        "marginal_cost": fuel_sources["Wind"].primary_cost, "efficiency": 1,
        "committable": False},
    {"name": f"Solar-pv_{country_trigram}", "carrier": "Solar", "p_nom": 12108.45,
        "p_min_pu": 0, "p_max_pu": solar_pv_data["value"].values,
        "marginal_cost": fuel_sources["Solar"].primary_cost, "efficiency": 1,
        "committable": False},
    # {"name": f"Other-renewables_{country_trigram}", "carrier": "Other-renewables",
    #     "p_nom": 6988.23, "p_min_pu": 0, "p_max_pu": 1, "marginal_cost": 0,
    #     "efficiency": 1, "committable": False},
    {"name": f"Nuclear_{country_trigram}", "carrier": "nuclear", "p_nom": 11277.0,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Uranium"].primary_cost * 0.33,
        "efficiency": 0.33, "committable": False},
    {"name": f"Hydro-reservoir_{country_trigram}", "carrier": "Hydro",
        "p_nom": 44482.06, "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": 0, "efficiency": 1, "committable": False},
    {"name": f"Hydro-run-of-river_{country_trigram}", "carrier": "Hydro",
        "p_nom": 7204.48, "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": 0, "efficiency": 1, "committable": False},
    {"name": f"Hydro-pump-storage_{country_trigram}", "carrier": "Hydro",
        "p_nom": 709.32, "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": 0, "efficiency": 1, "committable": False},
    # {"name": f"Batteries_{country_trigram}", "carrier": "Battery",
    #     "p_nom": 100.0, "p_min_pu": 0, "p_max_pu": 1,
    #     "marginal_cost": fuel_sources["Battery"].primary_cost, "efficiency": 0.95,
    #     "committable": False},
    {"name": f"Failure_{country_trigram}", "carrier": "Failure",
        "p_nom": 1e10, "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": 1e5, "efficiency": 1, "committable": False}
    ]
    
    
    # 2033 data
    # generators = [
    #     {"name": f"Hard-Coal_{country_trigram}", "carrier": "Coal", "p_nom": 183.6,
    #      "p_min_pu": 0, "p_max_pu": 1,
    #      "marginal_cost": fuel_sources["Coal"].primary_cost * 0.37,
    #      "efficiency": 0.37, "committable": False},
    #     {"name": f"Gas_{country_trigram}", "carrier": "Gas", "p_nom": 1891.75,
    #      "p_min_pu": 0, "p_max_pu": 1,
    #      "marginal_cost": fuel_sources["Gas"].primary_cost * 0.5,
    #      "efficiency": 0.5, "committable": False},
    #     {"name": f"Oil_{country_trigram}", "carrier": "Oil", "p_nom": 747.9,
    #      "p_min_pu": 0, "p_max_pu": 1,
    #      "marginal_cost": fuel_sources["Oil"].primary_cost * 0.4,
    #      "efficiency": 0.4, "committable": False},
    #     # {"name": f"Other-non-renewables_{country_trigram}",
    #     #  "carrier": "Other-non-renewables", "p_nom": 570.5, "p_min_pu": 0,
    #     #  "p_max_pu": 1, "marginal_cost": fuel_sources["Other-non-renewables"].primary_cost * 0.4,
    #     #  "efficiency": 0.4, "committable": False},
    #     {"name": f"Wind-on-shore_{country_trigram}", "carrier": "Wind",
    #      "p_nom": 71700.96, "p_min_pu": 0, "p_max_pu": wind_on_shore_data["value"].values,
    #      "marginal_cost": fuel_sources["Wind"].primary_cost, "efficiency": 1,
    #      "committable": False},
    #     {"name": f"Wind-off-shore_{country_trigram}", "carrier": "Wind",
    #      "p_nom": 26643.29, "p_min_pu": 0, "p_max_pu": wind_off_shore_data["value"].values,
    #      "marginal_cost": fuel_sources["Wind"].primary_cost, "efficiency": 1,
    #      "committable": False},
    #     {"name": f"Solar-pv_{country_trigram}", "carrier": "Solar", "p_nom": 49644.53,
    #      "p_min_pu": 0, "p_max_pu": solar_pv_data["value"].values,
    #      "marginal_cost": fuel_sources["Solar"].primary_cost, "efficiency": 1,
    #      "committable": False},
    #     # {"name": f"Other-renewables_{country_trigram}", "carrier": "Other-renewables",
    #     #  "p_nom": 6857.23, "p_min_pu": 0, "p_max_pu": 1, "marginal_cost": 0,
    #     #  "efficiency": 1, "committable": False},
    #     {"name": f"Nuclear_{country_trigram}", "carrier": "nuclear", "p_nom": 11277.0,
    #      "p_min_pu": 0, "p_max_pu": 1,
    #      "marginal_cost": fuel_sources["Uranium"].primary_cost * 0.33,
    #      "efficiency": 0.33, "committable": False},
    #     {"name": f"Hydro-reservoir_{country_trigram}", "carrier": "Hydro",
    #      "p_nom": 46678.27, "p_min_pu": 0, "p_max_pu": 1,
    #      "marginal_cost": 0, "efficiency": 1, "committable": False},
    #     {"name": f"Hydro-run-of-river_{country_trigram}", "carrier": "Hydro",
    #      "p_nom": 7586.41, "p_min_pu": 0, "p_max_pu": 1,
    #      "marginal_cost": 0, "efficiency": 1, "committable": False},
    #     {"name": f"Hydro-pump-storage_{country_trigram}", "carrier": "Hydro",
    #      "p_nom": 709.32, "p_min_pu": 0, "p_max_pu": 1,
    #      "marginal_cost": 0, "efficiency": 1, "committable": False},
    #     # {"name": f"Batteries_{country_trigram}", "carrier": "Battery",
    #     #  "p_nom": 1841.13, "p_min_pu": 0, "p_max_pu": 1,
    #     #  "marginal_cost": fuel_sources["Battery"].primary_cost, "efficiency": 0.95,
    #     #  "committable": False},
    #     {"name": f"Failure_{country_trigram}", "carrier": "Failure",
    #      "p_nom": 1e10, "p_min_pu": 0, "p_max_pu": 1,
    #      "marginal_cost": 1e5, "efficiency": 1, "committable": False}
    # ]
    return generators
