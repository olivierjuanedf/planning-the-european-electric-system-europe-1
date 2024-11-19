from typing import Dict, List

from long_term_uc.common.fuel_sources import FuelSources


gps_coords = (13.4137, 52.5181)


def get_generators(country_trigram: str, fuel_sources: Dict[str, FuelSources],
                   wind_on_shore_data, wind_off_shore_data, solar_pv_data) -> List[dict]:
    """
    Get list of generators to be set on a given node of a PyPSA model
    :param country_trigram: name of considered country, as a trigram (ex: "ben", "fra", etc.)
    :param fuel_sources
    """
    # List to be completed
    generators = [{"name": f"Hard-Coal_{country_trigram}", "carrier": "Coal", "p_nom": 27473.24,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Coal"].primary_cost * 0.37,
        "efficiency": 0.37, "committable": False},
        {"name": f"Gas_{country_trigram}", "carrier": "Gas", "p_nom": 32541.30,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Gas"].primary_cost * 0.5,
        "efficiency": 0.5, "committable": False},
        {"name": f"Oil_{country_trigram}", "carrier": "Oil", "p_nom": 2821.33,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Oil"].primary_cost * 0.4,
        "efficiency": 0.4, "committable": False},
        {"name": f"Other-non-renewable_{country_trigram}",
        "carrier": "Other-non-renewable", "p_nom": 9080.02, "p_min_pu": 0,
        "p_max_pu": 1, "marginal_cost": fuel_sources["Biomass"].primary_cost * 0.4,
        "efficiency": 0.4, "committable": False},
        {"name": f"Wind-on-shore_{country_trigram}", "carrier": "Wind",
        "p_nom": 69017.40, "p_min_pu": 0, "p_max_pu": wind_on_shore_data["value"].values,
        "marginal_cost": fuel_sources["Wind"].primary_cost, "efficiency": 1,
        "committable": False},
        {"name": f"Wind-off-shore_{country_trigram}", "carrier": "Wind",
        "p_nom": 11105.00, "p_min_pu": 0, "p_max_pu": wind_off_shore_data["value"].values,
        "marginal_cost": fuel_sources["Wind"].primary_cost, "efficiency": 1,
        "committable": False},
        {"name": f"Solar-pv_{country_trigram}", "carrier": "Solar", "p_nom": 88447.85,
        "p_min_pu": 0, "p_max_pu": solar_pv_data["value"].values,
        "marginal_cost": fuel_sources["Solar"].primary_cost, "efficiency": 1,
        "committable": False},
        {"name": f"Other-renewable_{country_trigram}", "carrier": "Other-renewable",
        "p_nom": 11056.79, "p_min_pu": 0, "p_max_pu": 1, "marginal_cost": 0,
        "efficiency": 1, "committable": False},
        {"name": f"Hydro-Pump-Storage-Closed-Loop_{country_trigram}", "carrier": "Pump-Storage-Closed-Loop", "p_nom": 6409.84,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Hydro"].primary_cost * 0.37,
        "efficiency": 0.37, "committable": False},
        {"name": f"Hydro-Pump-Storage-Open-Loop_{country_trigram}", "carrier": "Pump-Storage-Open-Loop", "p_nom": 2141.10,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Hydro"].primary_cost * 0.37,
        "efficiency": 0.37, "committable": False},
        {"name": f"Hydro-Reservoir_{country_trigram}", "carrier": "Pump-Reservoir", "p_nom": 819.00,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Hydro"].primary_cost * 0.37,
        "efficiency": 0.37, "committable": False},
        {"name": f"Hydro-Run-Of-River_{country_trigram}", "carrier": "Hydro-Run-Of-River", "p_nom": 3933.90,
        "p_min_pu": 0, "p_max_pu": 1,
        "marginal_cost": fuel_sources["Hydro"].primary_cost * 0.37,
        "efficiency": 0.37, "committable": False},        
        # QUESTION: what is this - very necessary - last fictive asset?
        {"name": f"Failure_{country_trigram}", "carrier": "Failure",
        "p_nom": 1e10, "p_min_pu": 0, "p_max_pu": 1, "marginal_cost": 1e5,
        "efficiency": 1, "committable": False}]
    return generators