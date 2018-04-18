#################################################################################################

		      README FILE FOR ACE NOy CLIMATOLOGIES (in ASCII format)

#################################################################################################

NOy climatology fields are produced in matlab (V2008b) and are converted  into ASCII, NetCDF and hdf formats.  
This readme file concerns those made in ASCII ONLY. 

ACE NOy climatologies are produced on a monthly and a three-monthly basis,

DJF MAM JJA SON

NOy climatologies are produced on latitude coordinates (-90 90). The vertical coordinate used is pressure (1000-0.1 hpa). Data considered run from February 2004 until February 2009 using the ACE-FTS v2.2 data products.


#########################################################################################################

STRUCTURE

The structure of the ASCII file for the monthly climatology fields is described in the following section. 
The three-monthly file structures are explained later.  

#########################################################################################################

 
Three data fields are combined to produce one large matrix.  These data fields correspond to: 
the VMR climatology values, the variability of the VMR values, and the average measurement uncertainty
and are given for each pressure level (1000-0.1 hPa; measurements from ACE-FTS do not extend lower than 
300 hPa) and latitude bin (labelled by centre of each 5 degree bin from -87.5 to 87.5).  Latitudes in the 
southern hemisphere are indicated by negative values.


9 data fields are combined to produce one large matrix.  Given for each pressure level (1000 - 0.1 hPa) and latitude bin (-87.5 - 87.5).  The format is as follows,

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
|.                         |	34 x 37  THIS THIRD SECTION ARE THE AVERAGE VARIANCE VALUES EXPRESSED AS A PERCENTAGE
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS FOURTH SECTION ARE THE TOTAL NUMBER OF OBSERVATIONS PER GRID CELL FOR NO
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS FIFTH SECTION ARE THE TOTAL NUMBER OF OBSERVATIONS PER GRID CELL FOR NO2
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS SIXTH SECTION ARE THE TOTAL NUMBER OF OBSERVATIONS PER GRID CELL FOR HNO3
|.                         |
|.                         |
|0.1                       |


|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS SEVENTH SECTION ARE THE TOTAL NUMBER OF OBSERVATIONS PER GRID CELL FOR N2O5
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS EIGHTH SECTION ARE THE TOTAL NUMBER OF OBSERVATIONS PER GRID CELL FOR ClONO2
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000			   | 
|.                         |
|.                         |	34 x 37  THIS NINTH SECTION ARE THE TOTAL NUMBER OF OBSERVATIONS PER GRID CELL FOR HNO4
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
of the polar vortex during late winter/early spring months.

###################################################################################################################
###################################################################################################################

If there are any questions, please contact

ASHLEY JONES (ajones@atmosp.physics.utoronto.ca)
KALEY WALKER (kwalker@atmosp.physics.utoronto.ca)

2011-12-16