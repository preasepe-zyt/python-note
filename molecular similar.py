from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MACCSkeys

# Define a molecule (SMILES representation)
smiles = "CCO"  # Replace this with your molecule's SMILES string

# Convert SMILES to an RDKit molecule object
mol = Chem.MolFromSmiles(smiles)

# Calculate RDKit fingerprint (Morgan fingerprint with radius 2)
rdk_fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2)

# Calculate ECFP4 fingerprint (Circular fingerprint with radius 2)
ecfp4_fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)

# Calculate MACCS fingerprint
maccs_fp = MACCSkeys.GenMACCSKeys(mol)

# Convert the fingerprints to binary strings or bit vectors
rdk_fp_str = rdk_fp.ToBitString()
ecfp4_fp_str = ecfp4_fp.ToBitString()
maccs_fp_str = ''.join(map(str, maccs_fp))

# Print the fingerprint descriptors
print("RDKit Fingerprint:")
print(rdk_fp_str)
print("ECFP4 Fingerprint:")
print(ecfp4_fp_str)
print("MACCS Fingerprint:")
print(maccs_fp_str)