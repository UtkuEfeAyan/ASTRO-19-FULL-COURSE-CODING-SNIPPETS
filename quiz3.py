from astropy.io import fits
import numpy as np

def main():
    fname = "Gaia_1kpc.fits"
    
    # open the FITS file
    hdul = fits.open(fname)
    
    # data is usually in extension 1
    data = hdul[1].data
    
    # extract parallax column
    parallax = data["parallax"]
    
    # compute mean
    mean_parallax = np.mean(parallax)
    
    print(mean_parallax)

if __name__ == "__main__":
    main()