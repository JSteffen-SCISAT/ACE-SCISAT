###############################################################################

      README FILE FOR ACE-FTS VERSION 3.5 CLIMATOLOGIES (in netCDF format)

###############################################################################


1. Brief summary:

- Climatology fields are produced in matlab (V2013b) and are converted into netCDF format. 
ACE-FTS climatologies are produced on a monthly and a three-monthly basis (DJF MAM JJA SON).

- Climatologies are also produced on latitudes as well as equivalent latitude coordinates (-90 90). 

- The vertical coordinate used is pressure (1000-0.0001 hpa). 

- Data considered run from February 2004 until February 2013 using ACE-FTS v3.5 data products. 

- Temperature climatology is also included in the same calculation method as trace gas climatology.

- For nitrogen-containing species (e.g. NO, NO2, HNO3, ClONO2, and N2O5), diurnal variation is considered. So the climatologies during am (before local noon) and pm (after local noon) are also provided.  Local solar time information is provided for these climatological fields.


2. FILE NAME:  "ACE_[1]_zm_[2]_hpa_[3]_[4]_[5].nc"

  - "zm" means zonal mean, "hpa" means the climatology for pressure height
  - [1] the average time period: "monthly" or "3monthly"
  - [2] showing species name: e.g., C2H2, CO, HCN, etc. 
        We have total 21 species + temperature (see the text)
  - [3] latitude ("lat") or equivalent latitude ("eql") bins
  - [4] date information
        For monthly mean: "Jan", "Feb", "Mar", ... "Dec" 
          (12 months - time = 1..12)
        For 3monthly mean: "Dec-Jan-Feb", "Mar-Apr-May", "Jun-Jul-Aug", 
          "Sep-Oct-Nov" (4 cases - time = 1..4)
  - [5] considering diurnal variation: 
        "am" means the climatology during only am (before local solar noon)
        "pm" means the climatology during only pm (after local solar noon)
        "all" means am/pm together


3. FILE STRUCTURE:  


- The structure of the netCDF file for the monthly climatology fields is described in the following example (The three-monthly file structures are explained later). This case shows latitude coordinates, but equivalent latitude files also use the same structure.

- For all trace gas species, the structure of the file is as follows (example for O3);

  netcdf ACE_monthly_zm_O3_hpa_lat_Jan_all {

  dimensions:
        lat = 36 ;
        plev = 48 ;
        time = 1 ;

  variables:
	double lat(lat), shape = [36]
		lat:long_name = "latitude" 
		lat:axis = "Y" 
		lat:units = "degrees_north" 
	double plev(plev), shape = [48]
		plev:long_name = "air pressure" 
		plev:axis = "Z" 
		plev:units = "hPa" 
	double time(time), shape = [1]
		time:long_name = "time" 
		time:axis = "T" 
		time:units = "month value" 
	double O3(lat,plev), shape = [36 48]
		O3:long_name = "O3" 
		O3:description = "volume mixing ratio of O3 in air" 
		O3:units = "ppv" 
	double O3_var(lat,plev), shape = [36 48]
		O3_var:long_name = "O3 variability" 
		O3_var:description = "volume mixing ratio of O3 in air standard deviation" 
		O3_var:units = "ppv" 
	double O3_err(lat,plev), shape = [36 48]
		O3_err:long_name = "O3 measurement uncertainty" 
		O3_err:description = "volume mixing ratio of measurement uncertainties of O3 in air" 
		O3_err:units = "ppv" 
	double O3_grid_count(lat,plev), shape = [36 48]
		O3_grid_count:long_name = "O3 accumulation per grid cell" 
		O3_grid_count:description = "Total number of observations per grid cell " 
		O3_grid_count:units = "Integer" 
//global attributes:
		:Experiment = "ACE-FTS" 
		:Version = "3.5" 
		:Organisation = "CSA" 
		:Type_of_Data = "MEASUREMENTS" 
		:Platform = "SATELLITE" 
		:Name_of_platform = "SCISAT-1" 
		:Projct_PI_name = "Prof. Kaley Walker" 
		:creation_date = "29-Jun-2016 05:17:09"
		:Fields = "T2Mz: Monthly-mean zonal mean 2-d atmosphere" 
		:Climatology_version = "2.0" 
		:Author = "Ja-Ho Koo" 
		:Institute = "University of Toronto" 
		:Address = "60 St George Street, M5S 1A7, ON, Toronto, CA" 
		:Email = "kwalker@atmosp.physics.utoronto.ca,jahokoo@atmosp.physics.utoronto.ca" 
		:Project_id = "ACE-FTS climatology data" 
		:Comment = "5 Points are required for a Monthly-Zonal-Average" 
		:Scaling_of_data = "None" 
}

- For temperature, the structure of the file is as follows;

netcdf ACE_monthly_zm_T_hpa_lat_Jan_all.nc { 
dimensions:
	lat = 36 ;
	plev = 48 ;
	time = 1 ;
variables:
	double lat(lat), shape = [36]
		lat:long_name = "latitude" 
		lat:axis = "Y" 
		lat:units = "degrees_north" 
	double plev(plev), shape = [48]
		plev:long_name = "air pressure" 
		plev:axis = "Z" 
		plev:units = "hPa" 
	double time(time), shape = [1]
		time:long_name = "time" 
		time:axis = "T" 
		time:units = "month value" 
	double T(lat,plev), shape = [36 48]
		T:long_name = "temperature" 
		T:description = "air temperature" 
		T:units = "K" 
	double T_var(lat,plev), shape = [36 48]
		T_var:long_name = "temperature variability" 
		T_var:description = "air temperature standard deviation" 
		T_var:units = "K" 
	double T_err(lat,plev), shape = [36 48]
		T_err:long_name = "T_fit parameter average" 
		T_err:description = "average of T_fit parameter (0=fixed; 1=retrieved)" 
		T_err:units = "K" 
	double T_grid_count(lat,plev), shape = [36 48]
		T_grid_count:long_name = "temperature accumulation per grid cell" 
		T_grid_count:description = "Total number of observations per grid cell " 
		T_grid_count:units = "Integer" 
//global attributes:
		:Experiment = "ACE-FTS" 
		:Version = "3.5" 
		:Organisation = "CSA" 
		:Type_of_Data = "MEASUREMENTS" 
		:Platform = "SATELLITE" 
		:Name_of_platform = "SCISAT-1" 
		:Projct_PI_name = "Prof. Kaley Walker" 
		:creation_date = "29-Jun-2016 05:17:09"
		:Fields = "T2Mz: Monthly-mean zonal mean 2-d atmosphere" 
		:Climatology_version = "2.0" 
		:Author = "Ja-Ho Koo" 
		:Institute = "University of Toronto" 
		:Address = "60 St George Street, M5S 1A7, ON, Toronto, CA" 
		:Email = "kwalker@atmosp.physics.utoronto.ca,jahokoo@atmosp.physics.utoronto.ca" 
		:Project_id = "ACE-FTS climatology data" 
		:Comment = "5 Points are required for a Monthly-Zonal-Average" 
		:Scaling_of_data = "None" 
}


- It can be seen that there are 7 parameters stored for the trace gas climatologies; an array of latitudes, an array of pressure heights, time (simply expressed as an integer for the corresponding month), plus matrix fields of the VMR climatology values, the variability of the VMR values, the average measurement uncertainty and the number of observations included in the average for each grid cell. 

- For the temperature climatologies, the 7 parameters are; an array of latitudes, an array of pressure heights, time (simply expressed as an integer for the corresponding month), plus matrix fields of the temperature climatology values, the variability of the temperature values, the average of the T_fit parameter and the number of observations included in the average for each grid cell. 

- For each pressure level (1000-0.0001 hPa; measurements from ACE-FTS do not extend lower than 300 hPa) and latitude bin (labelled by centre of each 5 degree bin from -87.5 to 87.5). 

- Latitudes in the southern hemisphere are indicated by negative values.


- For the diurnally varying species (e.g. NO, NO2, HNO3, ClONO2, and N2O5), 6 additional parameters are stored in each file; these are matrix fields for the local solar time zonal median, mean, maximum, minimum, standard deviation and median average deviation.

variables:
	double O3_median_lst(lat,plev), shape = [36 48]
		O3_median_lst:long_name = "O3 median LST" 
		O3_median_lst:description = "zonal median of Local Solar Time" 
		O3_median_lst:units = "Hour of day" 
	double O3_mean_lst(lat,plev), shape = [36 48]
		O3_mean_lst:long_name = "O3 mean LST" 
		O3_mean_lst:description = " zonal mean of Local Solar Time" 
		O3_mean_lst:units = "Hour of day" 
	double O3_max_lst(lat,plev), shape = [36 48]
		O3_max_lst:long_name = "O3 maximum LST" 
		O3_max_lst:description = " zonal maximum of Local Solar Time" 
		O3_max_lst:units = "Hour of day" 
	double O3_min_lst(lat,plev), shape = [36 48]
		O3_min_lst:long_name = "O3 minimum LST" 
		O3_min_lst:description = " zonal minimum of Local Solar Time" 
		O3_min_lst:units = "Hour of day" 
	double O3_std_lst(lat,plev), shape = [36 48]
		O3_std_lst:long_name = "O3 standard deviation of LST" 
		O3_std_lst:description = " zonal mean standard deviation of Local Solar Time" 
		O3_std_lst:units = "Hour of day" 
	double O3_mad_lst(lat,plev), shape = [36 48]
		O3_mad_lst:long_name = "O3 median deviation of LST" 
		O3_mad_lst:description = " zonal median deviation of Local Solar Time" 
		O3_mad_lst:units = "Hour of day" 


4. A note on three-monthly climatologies:

- Because of the highly inclined orbit of the ACE satellite, only certain latitudes will be measured during any one month.  

- Thus, during a three-month period for a given latitude, there may not be measurements from each month included in the climatological average.  This could produce climatology fields that may appear odd, especially near the regions of the polar vortex during late winter/early spring months.

- The structure of the three-monthly files are the same as those for the monthly climatologies - with the time field giving the season where DJF = 1; MAM = 2; JJA = 3 and SON = 4.



If there are any questions please contact:

KALEY WALKER (kwalker@atmosp.physics.utoronto.ca)
JA-HO KOO (jahokoo@atmosp.physics.utoronto.ca)

2016-07-12
