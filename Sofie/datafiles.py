
import xarray as xr

# ds_ERA5_pl=xr.open_dataset('/Iran_data/ERA5_05_DewPoints_Iran_pl_2025-07-31_06UTC.nc')
# ds_ERA5_sfc=xr.open_dataset('/Users/sofiehedetoft/Library/CloudStorage/OneDrive-Personligt/KU/Msc Climate Change/Kurser Bern/Seminar in Climatology/Iran_data/ERA5_05_DewPoints_Iran_sfc_2025-07-31_06UTC.nc')
# ds_AIFS_pl=xr.open_dataset('/Users/sofiehedetoft/Library/CloudStorage/OneDrive-Personligt/KU/Msc Climate Change/Kurser Bern/Seminar in Climatology/Iran_data/AIFS-ENS_05_DewPoints_Iran_pl_2025-07-31_06UTC.nc')
# ds_AIFS_sfc=xr.open_dataset('/Users/sofiehedetoft/Library/CloudStorage/OneDrive-Personligt/KU/Msc Climate Change/Kurser Bern/Seminar in Climatology/Iran_data/AIFS-ENS_05_DewPoints_Iran_sfc_2025-07-31_06UTC.nc')

ds_ERA5_pl=xr.open_dataset('/Users/sofiehedetoft/Library/CloudStorage/OneDrive-Personligt/KU/Msc Climate Change/Kurser Bern/Seminar_in _Climatology/Iran_data/ERA5_05_DewPoints_Iran_pl_2025-07-31_06UTC.nc')
ds_ERA5_sfc=xr.open_dataset('/Users/sofiehedetoft/Library/CloudStorage/OneDrive-Personligt/KU/Msc Climate Change/Kurser Bern/Seminar_in _Climatology/Iran_data/ERA5_05_DewPoints_Iran_sfc_2025-07-31_06UTC.nc')
ds_AIFS_pl=xr.open_dataset('/Users/sofiehedetoft/Library/CloudStorage/OneDrive-Personligt/KU/Msc Climate Change/Kurser Bern/Seminar_in _Climatology/Iran_data/AIFS-ENS_05_DewPoints_Iran_pl_2025-07-31_06UTC.nc')
ds_AIFS_sfc=xr.open_dataset('/Users/sofiehedetoft/Library/CloudStorage/OneDrive-Personligt/KU/Msc Climate Change/Kurser Bern/Seminar_in _Climatology/Iran_data/AIFS-ENS_05_DewPoints_Iran_sfc_2025-07-31_06UTC.nc')

##change from Kelvin to Celcius
# ds_AIFS_sfc=ds_AIFS_sfc.assign(d2m_C=lambda ds_AIFS_sfc: (ds_AIFS_sfc.d2m-273.15))
# ds_AIFS_pl=ds_AIFS_pl.assign(t_C=lambda ds_AIFS_pl: (ds_AIFS_pl.t-273.15))
# ds_ERA5_pl=ds_ERA5_pl.assign(t_C=lambda ds_ERA5_pl: (ds_ERA5_pl.t-273.15))
# ds_ERA5_sfc=ds_ERA5_sfc.assign(d2m_C=lambda ds_ERA5_sfc: (ds_ERA5_sfc.d2m-273.15))

