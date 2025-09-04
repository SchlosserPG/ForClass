######################################################
import geopandas as gpd ##to handle shapefile
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize #Standardize values and map them to colormaps.
from matplotlib.cm import ScalarMappable, get_cmap #Standardize values and map them to colormaps.

# ---- local shapefile path (relative to working directory) ----

##Citation: U.S. Census Bureau. (2023). TIGER/Line shapefile, 2023, U.S., county and equivalent (machine-readable data file). 
## U.S. Department of Commerce, Census Bureau. https://www2.census.gov/geo/tiger/TIGER2023/COUNTY/tl_2023_us_county.zip
shapefile = "data/tl_2023_us_county.zip"

# Read all US counties and filter to Virginia (STATEFP = "51")
gdf = gpd.read_file(shapefile)
va = gdf[gdf["STATEFP"] == "51"].to_crs(3857)

# Generating fake sales data for 2025 to show comparisons
np.random.seed(42)
centroids = va.geometry.centroid
x, y = centroids.x.to_numpy(), centroids.y.to_numpy()
base = 0.6*np.sin((x-x.mean())/2e5) + 0.4*np.cos((y-y.mean())/2e5) + 0.2*np.random.normal(size=len(va))
sales = (base - base.min()) / (base.max() - base.min())
va["sales_2025"] = (100*sales).round(1)

# BAD vs GOOD comparison for Virginia counties
fig, axes = plt.subplots(1, 2, figsize=(14,7))
for ax in axes: ax.set_axis_off()

# BAD rainbow: oversaturated, no boundaries, "jet" colormap
va.plot(
    column="sales_2025", 
    cmap="jet",            # jet is a bit harsher than rainbow
    linewidth=0.0,         # no county borders visual mush
    ax=axes[0] #
)
axes[0].set_title("BAD: Oversaturated rainbow (confusing, non-monochromatic)", pad=8)

norm = Normalize(vmin=0, vmax=100)
cb1 = fig.colorbar(ScalarMappable(norm=norm, cmap=get_cmap("jet")), ax=axes[0], fraction=0.035, pad=0.02)
cb1.set_label("fake sales (%)", rotation=90)

# GOOD viridis: clear sequential
va.plot(
    column="sales_2025", 
    cmap="viridis", 
    linewidth=0.3, 
    edgecolor="white", 
    ax=axes[1]
)
axes[1].set_title("GOOD: Sequential viridis (monochromatic, readable)", pad=8)

cb2 = fig.colorbar(ScalarMappable(norm=norm, cmap=get_cmap("viridis")), ax=axes[1], fraction=0.035, pad=0.02)
cb2.set_label("fake sales (%)", rotation=90)

plt.tight_layout()
plt.show()
