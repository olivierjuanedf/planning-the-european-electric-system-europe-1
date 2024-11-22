
#Deactivate (useless in pandas) warnings

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

AGG_PROD_TYPES_DEF = {
    "res_capa-factors": {
        "solar_pv": ["lfsolarpv"],
        "solar_thermal": ["csp_nostorage"],
        "wind_offshore": ["wind_offshore"],
        "wind_onshore": ["wind_onshore"]
    },
    "generation_capas": {
        "batteries": ["batteries"],
        "biofuel": ["biofuel"],
        "coal": ["coal", "hard_coal", "lignite"],
        "dsr": ["demand_side_response_capacity"],
        "gas": ["gas"],
        "hydro_pondage": ["hydro_pondage"],
        "hydro_pump_storage_closed_loop": ["hydro_pump_storage_closed_loop"],
        "hydro_pump_storage_open_loop": ["hydro_pump_storage_open_loop"],
        "hydro_reservoir": ["hydro_reservoir"],
        "hydro_run_of_river": ["hydro_run_of_river"],
        "nuclear": ["nuclear"], "oil": ["oil"],
        "others_fatal": ["others_non-renewable", "others_renewable"],
        "solar_pv": ["solar_photovoltaic"],
        "solar_thermal": ["solar_thermal"],
        "wind_offshore": ["wind_offshore"], "wind_onshore": ["wind_onshore"]
    }
}