import pandas as pd
from astropy.table import Table
import numpy as np


def collect_data(file = 'osc+otc-Assembled.fits'):
    """ 
    Sets up Data Object using data from a passed in fits file
    :param file: FITS file of transient/galaxy data
    """
    dat = Table.read(file, format='fits')
    df_bytes = dat.to_pandas()  # Convert to pandas dataframe
    df = pd.DataFrame()     # Init empty dataframe for converted types

    # Convert byte columns to strings
    for column in df_bytes:
        if df_bytes[column].dtype == np.dtype('object'):
            df[column + "_str"] = df_bytes[column].str.decode("utf-8")
            df[column] = df[column + "_str"].copy()
            df.drop(column + "_str", axis = 1, inplace = True)
        else:
            df[column] = df_bytes[column]

    # Prints sum of NULL values by column
    # df.isnull().sum().to_csv(output_dir + "Missing_Values.csv")
    return df