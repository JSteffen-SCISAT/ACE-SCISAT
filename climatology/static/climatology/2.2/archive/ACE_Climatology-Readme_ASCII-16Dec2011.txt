#################################################################################################

		      README FILE FOR ACE CLIMATOLOGIES (in ASCII format)

#################################################################################################

Climatology fields are produced in matlab (V2008b) and are converted  into ASCII, NetCDF and hdf formats.  
This readme file concerns those made in ASCII ONLY. 

ACE climatologies are produced on a monthly and a three-monthly basis,

DJF MAM JJA SON

Climatologies are also produced on latitudes as well as equivalent latitude coordinates (-90 90). 
The vertical coordinate used is pressure (1000-0.1 hpa). Data considered run from February
2004 until February 2009 using ACE-FTS v2.2 (including updates for O3 and N2O5) data products.

At present, the structure of ASCII files will vary for the preliminary version, such that those species that
are known to have a strong diurnal variation will contain 6 extra fields that concern the Local Solar Time (LST).
This way the user will be able to ascertain which LSTs are present for a given bin containing ACE data. Also for
these species we create seperate zonal averages for AM and PM LSTs. It is our intention that for the final 
product that all species shall contain this information and formatting.


#########################################################################################################

STRUCTURE

The structure of the ASCII file for the monthly climatology fields is described in the following section. 
The three-monthly file structures are explained later.  This case shows latitude coordinates, but 
equivalent latitude also uses the same structure.

#########################################################################################################

CASE 1:

For the following species : O3, HCl, H2O, CH4, CO, N2O, CFC-11, CFC-12, and HF, the structure of the file
is as follows:


Three data fields are combined to produce one large matrix.  These data fields correspond to: 
the VMR climatology values, the variability of the VMR values, and the average measurement uncertainty
and are given for each pressure level (1000-0.1 hPa; measurements from ACE-FTS do not extend lower than 
300 hPa) and latitude bin (labelled by centre of each 5 degree bin from -87.5 to 87.5).  Latitudes in the 
southern hemisphere are indicated by negative values.

The format is as follows,

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

9 data fields are combined to produce one large matrix.  As above in Case 1, these are given for each 
pressure level (1000 - 0.1 hPa) and latitude bin (-87.5 - 87.5).  The format is as follows,

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


A note on three-monthly climatologies

Because of the highly inclined orbit of the ACE satellite, only certain latitudes will be measured during any one 
month.  Thus, during a three-month period for a given latitude, there may not be measurements from each month included 
in the climatological average.  This could produce climatology fields that may appear odd, especially near the regions 
of the polar vortex during late winter/early spring months.  In order to account for this, ACE seasonal climatology 
values are only created if a given latitude is represented by at least two months of data.  This will mean a reduction 
in total coverage produced in each field, especially when considering latitude as the geolocation coordinate. 
However, this is less of a concern when using equivalent latitude.

The structure of the three-monthly files is the same as for CASE 1, such that LST is not stored in these files.

###################################################################################################################
###################################################################################################################

If there are any questions, please contact

ASHLEY JONES (ajones@atmosp.physics.utoronto.ca)
KALEY WALKER (kwalker@atmosp.physics.utoronto.ca)

2011-12-16