#################################################################################################

		      README FILE FOR ACE CLIMATOLOGIES (in netCDF format)

#################################################################################################

Climatology fields are produced in matlab (V2008b) and are converted into netCDF and hdf formats.

This readme file concerns those made in netCDF ONLY. IT SHOULD ALSO BE NOTED THAT THESE FILES WERE 
COMPILED ON A 64 BIT WINDOWS VISTA COMPUTER. Users who utilise a 32 bit machine may be able to dump 
the file but not extract any data. If this is the case, we advise the user to utilise the ascii data 
which contain the same information. 

ACE climatologies are produced on a monthly and a three-monthly basis,

DJF MAM JJA SON

Climatologies are also produced on latitudes as well as equivalent latitude coordinates (-90 90). 
The vertical coordinate used is pressure (1000-0.1 hpa). Data considered run from February
2004 until February 2009 using ACE-FTS v2.2 (including updates for O3 and N2O5) data products.

At present the structure of netCDF files will vary for the preliminary version, such that those species that
are known to have a strong diurnal variation will contain 6 extra fields that concern the Local Solar Time (LST).
This way the user will be able to ascertain which LSTs are present for a given bin containing ACE data. Also for
these species we create seperate zonal averages for AM and PM LSTs. It is our intention that for the final 
product that all species shall contain this information and formatting.

#########################################################################################################

STRUCTURE

The structure of the netCDF file for the monthly climatology fields is described in the following section. 
The three-monthly file structures are explained later. This case shows latitude coordinates, but equivalent 
latitude also use the same structure.

#########################################################################################################

CASE 1:

For the following species : O3, HCl, H2O, CH4, CO, N2O, CFC-11, CFC-12, and HF, the structure of the file
is as follows:


File dump...
netCDF C:\ace_climat\netCDF\netCDF\ACE_monthly_zm_O3_V2.2_vmr_press_lat_Jan.nc { 

dimensions:
	lat = 36 ;
	nlev = 33 ;
	time = 1 ;


variables:
	double lat(lat), shape = [36]
		lat:long_name = "Latitude" 
		lat:standard_name = "latitude" 
		lat:axis = "Y" 
		lat:units = "degrees_north" 
	double nlev(nlev), shape = [33]
		nlev:long_name = "Pressure" 
		nlev:standard_name = "air_pressure" 
		nlev:axis = "Z" 
		nlev:units = "hPa" 
	double time(time), shape = [1]
		time:long_name = "time" 
		time:standard_name = "time" 
		time:calender = "standard" 
		time:axis = "T" 
		time:units = "month value" 
	double species(lat,nlev), shape = [36 33]
		species:long_name = "O3" 
		species:standard_name = "Volume mixing ratio" 
		species:cell_methods = "lon:mean (zonal mean), time:mean (of calender months)" 
		species:units = "VMR" 
	double species_var(lat,nlev), shape = [36 33]
		species_var:long_name = "O3 variability" 
		species_var:standard_name = "Volume mixing ratio" 
		species_var:cell_methods = " 1 standard deviation of the spread of profiles in each bin" 
		species_var:units = "VMR" 
	double species_err(lat,nlev), shape = [36 33]
		species_err:long_name = "O3 Error" 
		species_err:standard_name = "Volume mixing ratio" 
		species_err:cell_methods = " lon:mean (zonal mean) of measurement uncertainty, time:mean (of calender months)" 
		species_err:units = "VMR" 


//global attributes:
		:history = "29-Apr-2009 09:09:44:  Creating netCDF"


It can be seen that there are 6 parameters stored; an array of latitudes, an array of pressures, 
time (simply expressed as an integer for the corresponding month), and 3 matrix fields.

The matrix fields correspond to the VMR climatology values, the variability of the VMR values, 
and the average measurement uncertainty given for each pressure level (1000-0.1 hPa; measurements from 
ACE-FTS do not extend lower than 300 hPa) and latitude bin (labelled by centre of each 5 degree bin 
from -87.5 to 87.5).  Latitudes in the southern hemisphere are indicated by negative values.


#########################################################################################################
#########################################################################################################

CASE 2:

For the following species : N2O, HNO3, NO, ClONO2, and N2O5 the structure of the file
looks as follows:

File dump...
netCDF C:\ace_climat\netCDF\netCDF\ACE_monthly_zm_HNO3_V2.2_vmr_press_lat_Jan_all.nc { 

dimensions:
	lat = 36 ;
	nlev = 33 ;
	time = 1 ;


variables:
	double lat(lat), shape = [36]
		lat:long_name = "Eqv latitude" 
		lat:standard_name = "Eqv latitude" 
		lat:axis = "Y" 
		lat:units = "degrees_north" 
	double nlev(nlev), shape = [33]
		nlev:long_name = "Pressure" 
		nlev:standard_name = "air_pressure" 
		nlev:axis = "Z" 
		nlev:units = "hPa" 
	double time(time), shape = [1]
		time:long_name = "time" 
		time:standard_name = "time" 
		time:calender = "standard" 
		time:axis = "T" 
		time:units = "month value" 
	double species(lat,nlev), shape = [36 33]
		species:long_name = "HNO3" 
		species:standard_name = "Volume mixing ratio" 
		species:cell_methods = "lon:mean (zonal mean), time:mean (of calender months)" 
		species:units = "VMR" 
	double species_var(lat,nlev), shape = [36 33]
		species_var:long_name = "HNO3 variability" 
		species_var:standard_name = "Volume mixing ratio" 
		species_var:cell_methods = " 1 standard deviation of the spread of profiles in each bin" 
		species_var:units = "VMR" 
	double species_err(lat,nlev), shape = [36 33]
		species_err:long_name = "HNO3 Error" 
		species_err:standard_name = "Volume mixing ratio" 
		species_err:cell_methods = " lon:mean (zonal mean) of measurement uncertainty, time:mean (of calender months)" 
		species_err:units = "VMR" 
	double species_median_lst(lat,nlev), shape = [36 33]
		species_median_lst:long_name = "HNO3 median LST" 
		species_median_lst:standard_name = "Local Solar Time" 
		species_median_lst:cell_methods = " lon:mean (zonal median) of Local Solar Time, time:mean (of calender months)" 
		species_median_lst:units = "Hour of day" 
	double species_mean_lst(lat,nlev), shape = [36 33]
		species_mean_lst:long_name = "HNO3 mean LST" 
		species_mean_lst:standard_name = "Local Solar Time" 
		species_mean_lst:cell_methods = " lon:mean (zonal mean) of Local Solar Time, time:mean (of calender months)" 
		species_mean_lst:units = "Hour of day" 
	double species_max_lst(lat,nlev), shape = [36 33]
		species_max_lst:long_name = "HNO3 maximum LST" 
		species_max_lst:standard_name = "Local Solar Time" 
		species_max_lst:cell_methods = " lon:mean (zonal maximum) of Local Solar Time, time:mean (of calender months)" 
		species_max_lst:units = "Hour of day" 
	double species_min_lst(lat,nlev), shape = [36 33]
		species_min_lst:long_name = "HNO3 minimum LST" 
		species_min_lst:standard_name = "Local Solar Time" 
		species_min_lst:cell_methods = " lon:mean (zonal minimum) of Local Solar Time, time:mean (of calender months)" 
		species_min_lst:units = "Hour of day" 
	double species_std_lst(lat,nlev), shape = [36 33]
		species_std_lst:long_name = "HNO3 standard deviation of LST" 
		species_std_lst:standard_name = "Local Solar Time" 
		species_std_lst:cell_methods = " lon:mean (zonal mean standard deviation) of Local Solar Time, time:mean (of calender months)" 
		species_std_lst:units = "Hour of day" 
	double species_mad_lst(lat,nlev), shape = [36 33]
		species_mad_lst:long_name = "HNO3 median deviation of LST" 
		species_mad_lst:standard_name = "Local Solar Time" 
		species_mad_lst:cell_methods = " lon:mean (zonal median deviation) of Local Solar Time, time:mean (of calender months)" 
		species_mad_lst:units = "Hour of day" 


//global attributes:
		:history = "04-Aug-2009 12:37:22:  Creating netCDF" 
}

It can be seen that there are 12 parameters stored; an array of latitudes, an array of pressures, 
time (simply expressed as an integer for the corresponding month), and 9 matrix fields.

The matrix fields correspond to the VMR climatology values, the variability of the VMR values, 
the average measurement uncertainty, median LST, mean LST, maximum LST, minimum LST, standard deviation LST, 
and median average deviation LST  given for each pressure level (1000-0.1 hPa; measurements from 
ACE-FTS do not extend lower than 300 hPa) and latitude bin (labelled by centre of each 5 degree bin 
from -87.5 to 87.5).  Latitudes in the southern hemisphere are indicated by negative values.


#########################################################################################################
#########################################################################################################

A note on three-monthly climatologies

Because of the highly inclined orbit of the ACE satellite, only certain latitudes will be measured during any one 
month.  Thus, during a three-month period for a given latitude, there may not be measurements from each month included 
in the climatological average.  This could produce climatology fields that may appear odd, especially near the regions 
of the polar vortex during late winter/early spring months.  In order to account for this, ACE seasonal climatology 
values are only created if a given latitude is represented by at least two months of data.  This will mean a reduction 
in total coverage produced in each field, especially when considering latitude as the geolocation coordinate. 
However, this is less of a concern when using equivalent latitude.

The structure of the three-monthly files is the same as for CASE 1, such that LST is not stored in these files.

#########################################################################################################
#########################################################################################################

If there are any questions please contact

ASHLEY JONES (ajones@atmosp.physics.utoronto.ca)
KALEY WALKER (kwalker@atmosp.physics.utoronto.ca)

2011-12-16