#################################################################################################

                      README FILE FOR ACE CLIMATOLOGIES (in netCDF format)

#################################################################################################

Climatology fields are produced in matlab (V2008b) and are converted into netCDF and
hdf formats.

This readme file concerns those made in netCDF ONLY. IT SHOULD ALSO BE NOTED THAT
THESE FILES WERE COMPILED ON A 64 BIT WINDOWS VISTA COMPUTER. Users who utilise a 32 bit machine may
be able to dump the file but not extract any data. If this is the case, we advise the user to
utilise the ascii data which contain the same information. 

ACE climatologies are produced on a monthly and a three-monthly basis,

DJF MAM JJA SON

Climatologies are also produced on latitudes as well as equivalent latitude
coordinates (-90 90). The vertical coordinate used is pressure (1000-0.1 hpa). Data considered run from
February 2004 until February 2009 using ACE-FTS v2.2 (including updates for O3 and N2O5) data
products.

#########################################################################################################

STRUCTURE

The structure of the netCDF file for the monthly climatology fields is described in
the following section. The three-monthly file structures are explained later. This case shows latitude
coordinates, but equivalent latitude also use the same structure.

#########################################################################################################

For the all baseline species the structure of the file
is as follows:


File dump...
netcdf ACE_monthly_zm_O3_V2.2_vmr_press_lat_Sep_all.nc { 

dimensions:
	lat = 36 ;
	plev = 33 ;
	time = 1 ;


variables:
	double lat(lat), shape = [36]
		lat:long_name = "latitude" 
		lat:axis = "Y" 
		lat:units = "degrees_north" 
	double plev(plev), shape = [33]
		plev:long_name = "air pressure" 
		plev:axis = "Z" 
		plev:units = "hPa" 
	double time(time), shape = [1]
		time:long_name = "time" 
		time:axis = "T" 
		time:units = "month value" 
	double O3(lat,plev), shape = [36 33]
		O3:long_name = "O3" 
		O3:description = "volume mixing ratio of O3 in air" 
		O3:units = "ppv" 
	double O3_var(lat,plev), shape = [36 33]
		O3_var:long_name = "O3 variability" 
		O3_var:description = "volume mixing ratio of O3 in air standard deviation" 
		O3_var:units = "ppv" 
	double O3_err(lat,plev), shape = [36 33]
		O3_err:long_name = "O3 measurement uncertainty" 
		O3_err:description = "volume mixing ratio of measurement uncertainties of O3 in air" 
		O3_err:units = "ppv" 
	double O3_median_lst(lat,plev), shape = [36 33]
		O3_median_lst:long_name = "O3 median LST" 
		O3_median_lst:description = "zonal median of Local Solar Time" 
		O3_median_lst:units = "Hour of day" 
	double O3_mean_lst(lat,plev), shape = [36 33]
		O3_mean_lst:long_name = "O3 mean LST" 
		O3_mean_lst:description = " zonal mean of Local Solar Time" 
		O3_mean_lst:units = "Hour of day" 
	double O3_max_lst(lat,plev), shape = [36 33]
		O3_max_lst:long_name = "O3 maximum LST" 
		O3_max_lst:description = " zonal maximum of Local Solar Time" 
		O3_max_lst:units = "Hour of day" 
	double O3_min_lst(lat,plev), shape = [36 33]
		O3_min_lst:long_name = "O3 minimum LST" 
		O3_min_lst:description = " zonal minimum of Local Solar Time" 
		O3_min_lst:units = "Hour of day" 
	double O3_std_lst(lat,plev), shape = [36 33]
		O3_std_lst:long_name = "O3 standard deviation of LST" 
		O3_std_lst:description = " zonal mean standard deviation of Local Solar Time" 
		O3_std_lst:units = "Hour of day" 
	double O3_mad_lst(lat,plev), shape = [36 33]
		O3_mad_lst:long_name = "O3 median deviation of LST" 
		O3_mad_lst:description = " zonal median deviation of Local Solar Time" 
		O3_mad_lst:units = "Hour of day" 
	double O3_grid_count(lat,plev), shape = [36 33]
		O3_grid_count:long_name = "O3 accumulation per grid cell" 
		O3_grid_count:description = "Total number of observations per grid cell " 
		O3_grid_count:units = "Integer" 


//global attributes:
		:Experiment = "ACE-FTS" 
		:Version = "2.2" 
		:Organisation = "CSA" 
		:Type_of_Data = "MEASUREMENTS" 
		:Platform = "SATELLITE" 
		:Name_of_platform = "SCISAT-1" 
		:Projct_PI_name = "Prof. Kaley Walker" 
		:File_creation_time = "2012-3-1 19:51:9.818" 
		:file_modification_time = "2012-3-1 19:51:9.818" 
		:Fields = "T2Mz: Monthly-mean zonal mean 2-d atmosphere" 
		:Climatology_version = "1.0" 
		:Author = "Ashley Jones" 
		:Institute = "University of Toronto" 
		:Address = "60 St George Street, M5S 1A7, ON, Toronto, CA" 
		:Email = "kwalker@atmosp.physics.utoronto.ca,ajones@atmosp.physics.utoronto.ca" 
		:Project_id = "ACE-FTS climatology data" 
		:Comment = "5 Points are required for an Monthly-Zonal-Average" 
		:Scaling_of_data = "None" 
		:history = "01-Mar-2012 19:51:09:  Creating netCDF" 
}


It can be seen that there are 13 parameters stored; an array of latitudes, an array
of pressures, time (simply expressed as an integer for the corresponding month), and 10 matrix fields.

The matrix fields correspond to the VMR climatology values, the variability of the
VMR values, the average measurement uncertainty, median LST, mean LST, maximum LST, minimum LST,
standard deviation LST, median average deviation LST and the total number of values per bin for each pressure level (1000-0.1 hPa;measurements from ACE-FTS do not extend lower than 300 hPa) and latitude bin (labelled by centre of each 5 degree bin from -87.5 to 87.5).  Latitudes in the southern hemisphere are indicated by negative
values.



#########################################################################################################
#########################################################################################################


A note on three-monthly climatologies

Because of the highly inclined orbit of the ACE satellite, only certain latitudes
will be measured during any one month.  Thus, during a three-month period for a given latitude, there may not be
measurements from each month included in the climatological average.  This could produce climatology fields that may appear odd, especially near the regions of the polar vortex during late winter/early spring months.

The structure of the three-monthly files is as follows;

File dump...
netcdf ACE_monthly_zm_O3_V2.2_vmr_press_lat_Sep-Oct-Nov_all.nc { 

dimensions:
	lat = 36 ;
	plev = 33 ;
	time = 1 ;


variables:
	double lat(lat), shape = [36]
		lat:long_name = "latitude" 
		lat:axis = "Y" 
		lat:units = "degrees_north" 
	double plev(plev), shape = [33]
		plev:long_name = "air pressure" 
		plev:axis = "Z" 
		plev:units = "hPa" 
	double time(time), shape = [1]
		time:long_name = "time" 
		time:axis = "T" 
		time:units = "month value" 
	double O3(lat,plev), shape = [36 33]
		O3:long_name = "O3" 
		O3:description = "volume mixing ratio of O3 in air" 
		O3:units = "ppv" 
	double O3_var(lat,plev), shape = [36 33]
		O3_var:long_name = "O3 variability" 
		O3_var:description = "volume mixing ratio of O3 in air standard deviation" 
		O3_var:units = "ppv" 
	double O3_err(lat,plev), shape = [36 33]
		O3_err:long_name = "O3 measurement uncertainty" 
		O3_err:description = "volume mixing ratio of measurement uncertainties of O3 in air" 
		O3_err:units = "ppv" 
	double O3_grid_count(lat,plev), shape = [36 33]
		O3_grid_count:long_name = "O3 accumulation per grid cell" 
		O3_grid_count:description = "Total number of observations per grid cell " 
		O3_grid_count:units = "Integer" 


//global attributes:
		:Experiment = "ACE-FTS" 
		:Version = "2.2" 
		:Organisation = "CSA" 
		:Type_of_Data = "MEASUREMENTS" 
		:Platform = "SATELLITE" 
		:Name_of_platform = "SCISAT-1" 
		:Projct_PI_name = "Prof. Kaley Walker" 
		:File_creation_time = "2012-3-1 19:51:37.633" 
		:file_modification_time = "2012-3-1 19:51:37.633" 
		:Fields = "T2Mz: Monthly-mean zonal mean 2-d atmosphere" 
		:Climatology_version = "1.0" 
		:Author = "Ashley Jones" 
		:Institute = "University of Toronto" 
		:Address = "60 St George Street, M5S 1A7, ON, Toronto, CA" 
		:Email = "kwalker@atmosp.physics.utoronto.ca,ajones@atmosp.physics.utoronto.ca" 
		:Project_id = "ACE-FTS climatology data" 
		:Comment = "5 Points are required for an Monthly-Zonal-Average" 
		:Scaling_of_data = "None" 
		:history = "01-Mar-2012 19:51:37:  Creating netCDF" 
}

#########################################################################################################
#########################################################################################################

If there are any questions please contact

ASHLEY JONES (ajones@atmosp.physics.utoronto.ca)
KALEY WALKER (kwalker@atmosp.physics.utoronto.ca)

2012-05-04
