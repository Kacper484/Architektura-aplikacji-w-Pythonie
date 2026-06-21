# Project for "Architektóra aplikacji w Python"
Author Kacper Kaszuba

### Requirements
requirements.txt is in repo it contains every used library
runtime environment was Google Colab

## How to Run
1. Download dataset from the link above and place CSV files in the same directory as the notebook
2. Open `Projekt_ML_Kacper_Kaszuba.ipynb` in Google Colab
3. Run all cells in order

### Dataset
**PHYLACINE 1.2** — The Phylogenetic Atlas of Mammal Macroecology
- 5,831 known mammal species
- Two key files:
  - `Trait_data.csv` — body mass (`Mass.g`), diet, habitat type, taxonomic order, IUCN status (`IUCN.Status.1.2`)
  - `Spatial_metadata.csv` — geographic range size (`Number.Cells.Current.Range`, `Number.Cells.Present.Natural.Range`)
- Files are merged on `Binomial.1.2` (species name)

Link to dataset:  https://datadryad.org/dataset/doi:10.5061/dryad.bp26v20

### Thesis
> **"Body mass and geographic range size are the dominant biological predictors of extinction risk in mammals, independent of taxonomic order."**

This thesis is confronted using **Random Forest feature importance** — if `Log.Mass` and `Log.Range.Current` rank highest, thesis is confirmed. If `Order.Encoded` (taxonomic order) ranks high, it suggests taxonomy matters more than claimed.


### Key Features
**Main:**
  1. `Log.Mass`: Log-transformed body mass  in grams
  2. `Log.Range.Current`: Log-transformed current  geographic range
  3. `Log.Range.Natural `: Range without human pressure
  4. `Order.Encoded`: Taxonomic order (label encoded)

**Additional:**
  1. `Diet.Plant/Vertebrate/Invertebrate`: Diet composition
  2. `Terrestrial/Marine/Freshwater/Aerial`: Habitat type
  3. `Island.Endemicity`: Island vs mainland species

## Models

### 1. Logistic Regression
- Baseline model
- Needs `StandardScaler` applied first
- Use `class_weight='balanced'` (because  data set have  many more LC species then threatened)

### 2. Random Forest
- Main model for thesis confrontation
- Does **not** need scaling
- Use `class_weight='balanced'`
- Feature importance plot is the key output - this is where thesis is confronted

### 3. Neural Network (PyTorch)
Architecture:
Input → Linear(64) → ReLU → Dropout(0.3)
      → Linear(32) → ReLU → Dropout(0.2)
      → Linear(1)  [raw logit]
- Loss: BCEWithLogitsLoss with `pos_weight` (handles class imbalance)
- Optimizer: `Adam, lr=1e-3`
- Manual training loop with early stopping (patience=5)

###  4. PCA (not a model - just analysis tool)
- Used on data  analysis phase for  EDA visualization
- Reduces features to 2D to  visualize species clustering by threat status

## Libraries
pandas, numpy                    — data
matplotlib, seaborn              — visualization
scikit-learn                     — preprocessing, LR, RF, PCA, metrics
torch, torch.nn, torch.utils.data — neural network

# Results
By analyzing feature importance of **Random Forest** we can confirm the thesis. The best model (out of 3) for identifying endangered species is **Neural Network**.
LR: AUC=0.92 | RF: AUC=0.91 | NN: AUC=0.92
