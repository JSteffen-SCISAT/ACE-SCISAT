#################################################################################################

                      README FILE FOR ACE CLIMATOLOGIES (in ASCII format)

#################################################################################################

Climatology fields IS produced in matlab (V2008b) and IS converted  into ASCII,
NetCDF and hdf formats. This readme file concerns those made in ASCII ONLY. 

ACE climatologies are produced on a monthly and a three-monthly basis,

DJF MAM JJA SON

Climatologies are also produced on latitudes as well as equivalent latitude
coordinates (-90 90). The vertical coordinate used is pressure (1000-0.1 hpa). Data considered run from
February 2004 until February 2009 using ACE-FTS v2.2 (including updates for O3 and N2O5) data
products.


#########################################################################################################

STRUCTURE

The structure of the ASCII file for the monthly climatology fields is described in
the following section. The three-monthly file structures are explained later.  This case shows latitude
coordinates, but equivalent latitude also uses the same structure.

#########################################################################################################


For all 14 baseline species the structure of the file is as follows:


10 data fields are combined to produce one large matrix. Climatological data
are given for each pressure level (1000-0.1 hPa; measurements from ACE-FTS do
not extend lower than 300 hPa) and latitude bin (labelled by centre of each 5 degree bin from -87.5 to
87.5).  Latitudes in the southern hemisphere are indicated by negative values.

The format is as follows,



|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS FIRST SECTION IS THE ZONAL MEAN VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS SECOND SECTION IS THE STANDARD DEVIATION (VARIANCE) IN EACH BIN
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS THIRD SECTION IS THE AVERAGE MEASUREMENT ERROR VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS FOURTH SECTION IS THE MEDIAN LST VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS FIFTH SECTION IS THE MEAN LST VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS SIXTH SECTION IS THE MAX LST VALUES
|.                         |
|.                         |
|0.1                       |


|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS SEVENTH SECTION IS THE MIN LST VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS EIGHTH SECTION IS THE STANDARD DEVIATION LST VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS NINTH SECTION IS THE MEDIAN AVERAGE DEVIATION LST VALUES
|.                         |
|.                         |
|0.1                       |

nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS TENTH SECTION IS THE TOTAL NUMBER OF VALUES PER BIN
|.                         |
|.                         |
|0.1                       |

In total, the size of the matrix 340 x 37


####################################################################################################################
####################################################################################################################


Three-monthly climatologies

Because of the highly inclined orbit of the ACE satellite, only certain latitudes
will be measured during any one month.  Thus, during a three-month period for a given latitude, there may not be
measurements from each month included in the climatological average.  This could produce climatology fields that may
appear odd, especially near the regions of the polar vortex during late winter/early spring months.

The structure of the three-monthly files is as follow;

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS FIRST SECTION IS THE ZONAL MEaAN VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS SECOND SECTION IS THE STANDARD DEVIATION (VARIANCE) IN EACH BIN
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS THIRD SECTION IS THE AVERAGE MEASUREMENT ERROR VALUES
|.                         |
|.                         |
|0.1                       |

|nan   -87.5 ..........87.5|
|1000                           | 
|.                         |
|.                         |        34 x 37  THIS FOURTH SECTION IS THE TOTAL NUMBER OF VALUES PER BIN
|.                         |
|.                         |
|0.1                       |

In total, the size of the matrix 136 x 37

###################################################################################################################
###################################################################################################################

If there are any questions, please contact

ASHLEY JONES (ajones@atmosp.physics.utoronto.ca)
KALEY WALKER (kwalker@atmosp.physics.utoronto.ca)

2012-05-04
