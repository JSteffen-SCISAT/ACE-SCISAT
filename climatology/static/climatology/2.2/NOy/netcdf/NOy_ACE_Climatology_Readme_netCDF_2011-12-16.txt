#################################################################################################

		      README FILE FOR ACE NOy CLIMATOLOGIES (in netCDF format)

#################################################################################################

The NOy climatology fields are produced in matlab (V2008b) and are converted into netCDF and hdf formats.

This readme file concerns those made in netCDF ONLY. IT SHOULD ALSO BE NOTED THAT THESE FILES WERE 
COMPILED ON A 64 BIT WINDOWS VISTA COMPUTER. Users who utilise a 32 bit machine may be able to dump 
the file but not extract any data. If this is the case, we advise the user to utilise the ascii data 
which contain the same information. 

ACE NOy climatologies are produced on a monthly and a three-monthly basis,

DJF MAM JJA SON

NOy climatologies are produced on latitudes coordinates (-90 90). 
The vertical coordinate used is pressure (1000-0.1 hpa). Data considered run from February
2004 until February 2009 using the ACE-FTS v2.2 data products.


#########################################################################################################

STRUCTURE

The structure of the netCDF file for the monthly NOy climatology fields is described in the following section. 
The three-monthly file structures are explained later. 

#########################################################################################################


nc_dump('ACE_monthly_zm_NOy_V2.2_vmr_press_lat_Apr_all.nc')
netcdf ACE_monthly_zm_NOy_V2.2_vmr_press_lat_Apr_all.nc { 

dimensions:
	lat = 36 ;
	nlev = 33 ;
	species = 6 ;


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
	double species(lat,nlev), shape = [36 33]
		species:long_name = "NOy" 
		species:standard_name = "Volume mixing ratio" 
		species:cell_methods = "lon:mean (zonal median), time:mean (of calender months)" 
		species:units = "VMR" 
	double species_var(lat,nlev), shape = [36 33]
		species_var:long_name = "NOy variability" 
		species_var:standard_name = "Volume mixing ratio" 
		species_var:cell_methods = " 1 standard deviation of the spread of profiles in each bin" 
		species_var:units = "VMR" 
	double species_var_pct(lat,nlev), shape = [36 33]
		species_var_pct:long_name = "NOy variability in %" 
		species_var_pct:standard_name = "%" 
		species_var_pct:cell_methods = " lon:mean (zonal median) of measurement uncertainty, time:mean (of calender months)" 
		species_var_pct:units = "%" 
	double species_grid_count(lat,nlev,species), shape = [36 33 6]
		species_grid_count:long_name = "NOy accumulation per grid cell" 
		species_grid_count:standard_name = "Accumalation" 
		species_grid_count:cell_methods = "Total number of observations per grid cell, per species : NO(1), NO2(2), HNO3(3), N2O5(4), ClONO2(5), HNO4(6) (respectively)" 
		species_grid_count:units = "Integer" 


//global attributes:
		:history = "25-May-2011 06:30:08:  Creating netCDF" 
}

It can be seen that there are 6 parameters stored; an array of latitudes, an array of pressures, 
and 3 matrix fields.

The matrix fields correspond to the VMR climatology values, the variability of the VMR values, the 
variability of the VMR values expressed as a percentage, and the number of observations per grid cell
for each individual species. Pressure levels (1000-0.1 hPa; measurements from ACE-FTS do not extend 
lower than 300 hPa) and latitude bin (labelled by centre of each 5 degree bin 
from -87.5 to 87.5).  Latitudes in the southern hemisphere are indicated by negative values.


#########################################################################################################
#########################################################################################################

A note on three-monthly climatologies

Because of the highly inclined orbit of the ACE satellite, only certain latitudes will be measured during any one 
month.  Thus, during a three-month period for a given latitude, there may not be measurements from each month included 
in the climatological average.  This could produce climatology fields that may appear odd, especially near the regions 
of the polar vortex during late winter/early spring months. 

#########################################################################################################
#########################################################################################################

If there are any questions please contact

ASHLEY JONES (ajones@atmosp.physics.utoronto.ca)
KALEY WALKER (kwalker@atmosp.physics.utoronto.ca)

2011-12-16