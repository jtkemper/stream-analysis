# Input and Output filepath
INPUT_filepath = "../INPUT/"
geospat_data_filepath = INPUT_filepath+"00_geospatial_data/"
ancillary_data_filepath = INPUT_filepath+"00_ancillary_data/"
basin_atlas_filepath = INPUT_filepath+"04_static_catchment_characteristics/"
metadata_filepath = INPUT_filepath+"01_metadata/"
shapefile_filepath = INPUT_filepath+'03_shapefiles/'
water_quality_filepath = INPUT_filepath + "02_waterquality_timeseries/"
discharge_filepath = INPUT_filepath + "08_streamflow_discharge/"
landuse_filepath = INPUT_filepath + "06_dynamic_lulc/"
OUTPUT_filepath = "../OUTPUT/"

# Style guides
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

solutes = ['DO_mgL', 'SpC_uScm', 'Turb_FNU', 'WTemp_C', 'NO3_mgNL', 'fDOM_QSU']
solute_pretty = {"DO_mgL":"DO (mg/L)",
                 "SpC_uScm":"SpC (µS/cm)",
                 "Turb_FNU":"Turbidity (FNU)",
                 "WTemp_C":"Temp ($^{o}$C)",
                 "NO3_mgNL":"NO$_{3}$-N (mg/L)",
                 "fDOM_QSU":"fDOM (QSU)"
                }
    
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASE = "#c3c2b7"
SURFACE = "#ffffff"

PARAM_COLORS = {
    'DO_mgL':    {'fill': '#FEDCBB', 'edge': '#7F2704', 'cmap':'Oranges'}, 
    'SpC_uScm':  {'fill': '#E2EDF8', 'edge': '#08306B', 'cmap':'Blues'}, 
    'Turb_FNU':  {'fill': '#CEECC8', 'edge': '#00431A', 'cmap':'Greens'}, 
    'WTemp_C':   {'fill': '#DADAEB', 'edge': '#3F007D', 'cmap':'Purples'},
    'NO3_mgNL':  {'fill': '#FEE0D2', 'edge': '#67000D', 'cmap':'Reds'},
    'fDOM_QSU':  {'fill': '#D9F0A3', 'edge': '#238443', 'cmap':'YlGn'},
}

SEQ_BLUE = ["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7",
            "#3987e5", "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281",
            "#0d366b"]
CMAP_BLUE = LinearSegmentedColormap.from_list("seqblue", SEQ_BLUE)

# rcParams ---
def set_style():
    mpl.rcParams.update({
        "figure.dpi": 110,
        "savefig.dpi": 400,
        "savefig.facecolor": SURFACE,
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial"],
        "font.size": 8,
        "axes.titlesize": 9,
        "axes.labelsize": 8,
        "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5,
        "legend.fontsize": 7.5,
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": BASE,
        "axes.linewidth": 0.7,
        "xtick.color": INK2,
        "ytick.color": INK2,
        "axes.grid": False,
        "grid.color": GRID,
        "grid.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "axes.axisbelow": True,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

def despine_all(ax):
    for s in ax.spines.values():
        s.set_visible(False)

def panel_label(ax, letter, x=-0.08, y=1.05):
    ax.text(x, y, letter, transform=ax.transAxes, fontsize=11,
            fontweight="bold", va="bottom", ha="right", color=INK)
