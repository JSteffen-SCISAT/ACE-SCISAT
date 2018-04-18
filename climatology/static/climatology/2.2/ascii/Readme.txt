#################################################################################################

		      README FILE FOR ACE CLIMATOLOGIES (in ASCII format)

#################################################################################################

Climatology fields are produced in matlab (V2008b) and are converted  into ASCII, netcdf and hdf formats. 
This readme file concerns those made in ASCII ONLY. 

ACE climatologies are produced on a monthly and a seasonal basis,

DJF MAM JJA SON

Climatologies are also produced on latitudes as well as equivalent latitude
coordinates (-90 90). The vertical coordinate used is pressure (1000-0.1 hpa). Data considered run from January
2004 until February 2009 using v2.2 observations

At present the structure of ascii files will vary for the preliminary version, such that those species that
are known to have a strong diurnal variation will contain 6 extra fields that concern the Local Solar Time (LST).
This way the user will be able to ascertain which LSTs are present for a given bin containing ACE data. Also for
these species we create seperate zonal averages for AM and PM LSTs. It is our intention that for the final 
product that all species shall contain this information and formatting.


#########################################################################################################

STRUCTURE

The structure of the ASCII file looks the following and concerns monthly climatology fields. Seasonal is explained later.

#########################################################################################################

CASE 1:

For the following species : O3, HCl, H2O, CH4, CO, HF, CFC-11, CFC-12, and HF, the structure of the file
looks as follows:


3 fields of data are combined to produce one large matrix. The format is as follows,



|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS FIRST SECTION ARE THE ZONAL MEDIAN VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS SECOND SECTION ARE THE AVERAGE VARIANCE VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS FIRST SECTION ARE THE AVERAGE MEASUREMENT ERROR VALUES
|.                         |
|.                         |
|0.1                       |

In total, the size of the matrix 102 x 37


#########################################################################################################
#########################################################################################################

CASE 2:

For the following species : N2O, HNO3, NO, ClONO2, and N2O5 the structure of the file
looks as follows:

9 fields of data are combined to produce one large matrix. The format is as follows,

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS FIRST SECTION ARE THE ZONAL MEDIAN VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS SECOND SECTION ARE THE AVERAGE VARIANCE VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS THIRD SECTION ARE THE AVERAGE MEASUREMENT ERROR VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS FOURTH SECTION ARE THE MEDIAN LST VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS FIFTH SECTION ARE THE MEAN LST VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS SIXTH SECTION ARE THE MAX LST VALUES
|.                         |
|.                         |
|0.1                       |


|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS SEVENTH SECTION ARE THE MIN LST VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS EIGHTH SECTION ARE THE STANDARD DEVIATION LST VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS NINTH SECTION ARE THE MEDIAN AVERAGE DEVIATION LST VALUES
|.                         |
|.                         |
|0.1                       |

In total, the size of the matrix 306 x 37


####################################################################################################################
####################################################################################################################


A note on seasonal climatologies

As the ACE satellite maintains a repeatable orbit it means that only certain latitudes will be covered 
during anyone month. It may mean that during a season only one month of data may represent a given location.
This could produce climatology fields that may appear odd, especially near the regions of the polar vortex during
late winter/early spring months. In order to account for this ACE seasonal climatology values are only created 
if a given location is represented by atleast 2 months of data. This will mean a reduction in total coverage 
produced in each field, especially when considering latitude as the geolocation coordinate. 
This is of course less of a problem when using equivalent latitude.

The structure of the seasonal files is the same for CASE 1, such that LST is not stored in these files.

###################################################################################################################
###################################################################################################################

If there are any questions please contact

ASHLEY JONES

ajones@atmosp.physics.utoronto.ca

2010-05-19
 


