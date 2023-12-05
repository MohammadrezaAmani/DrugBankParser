class DrugType:
    SMALLMOLECULE = "small molecule"
    BIOTECH = "biotech"


class State:
    SOLID = "solid"
    LIQUID = "liquid"
    GAS = "gas"


class Group:
    """Drugs are grouped into a category like approved, experimental, illicit."""

    APPROVED = "approved"
    ILLICIT = "illicit"
    EXPERIMENTAL = "experimental"
    WITHDRAWN = "withdrawn"
    NUTRACEUTICAL = "nutraceutical"
    INVESTIGATIONAL = "investigational"
    VET_APPROVED = "vet_approved"


class Calculatedpropertysource:
    CHEMAXON = "ChemAxon"
    ALOGPS = "ALOGPS"


class Calculatedpropertykind:
    LOGP = "logP"
    LOGS = "logS"
    WATERSOLUBILITY = "Water Solubility"
    IUPACNAME = "IUPAC Name"
    TRADITIONALIUPACNAME = "Traditional IUPAC Name"
    MOLECULARWEIGHT = "Molecular Weight"
    MONOISOTOPICWEIGHT = "Monoisotopic Weight"
    SMILES = "SMILES"
    MOLECULARFORMULA = "Molecular Formula"
    INCHI = "InChI"
    INCHIKEY = "InChIKey"
    POLARSURFACEAREA_PSA = "Polar Surface Area (PSA)"
    REFRACTIVITY = "Refractivity"
    POLARIZABILITY = "Polarizability"
    ROTATABLEBONDCOUNT = "Rotatable Bond Count"
    HBONDACCEPTORCOUNT = "H Bond Acceptor Count"
    HBONDDONORCOUNT = "H Bond Donor Count"
    PKA_STRONGESTACIDIC = "pKa (strongest acidic)"
    PKA_STRONGESTBASIC = "pKa (strongest basic)"
    PHYSIOLOGICALCHARGE = "Physiological Charge"
    NUMBEROFRINGS = "Number of Rings"
    BIOAVAILABILITY = "Bioavailability"
    RULEOFFIVE = "Rule of Five"
    GHOSEFILTER = "Ghose Filter"
    MDDRLIKERULE = "MDDR-Like Rule"
    VEBERSRULE = "Veber's Rule"


class Externalidentifierresource:
    UNIPROTKB = "UniProtKB"
    WIKIPEDIA = "Wikipedia"
    CHEBI = "ChEBI"
    CHEMBL = "ChEMBL"
    PUBCHEMCOMPOUND = "PubChem Compound"
    PUBCHEMSUBSTANCE = "PubChem Substance"
    DRUGSPRODUCTDATABASE_DPD = "Drugs Product Database (DPD)"
    KEGGCOMPOUND = "KEGG Compound"
    KEGGDRUG = "KEGG Drug"
    CHEMSPIDER = "ChemSpider"
    BINDINGDB = "BindingDB"
    NATIONALDRUGCODEDIRECTORY = "National Drug Code Directory"
    GENBANK = "GenBank"
    THERAPEUTICTARGETSDATABASE = "Therapeutic Targets Database"
    PHARMGKB = "PharmGKB"
    PDB = "PDB"
    IUPHAR = "IUPHAR"
    GUIDETOPHARMACOLOGY = "Guide to Pharmacology"
    ZINC = "ZINC"
    RXCUI = "RxCUI"


class Externallinkresource:
    RXLIST = "RxList"
    PDRHEALTH = "PDRhealth"
    DRUGS_COM = "Drugs.com"


class Polypeptideexternalidentifierresource:
    UNIPROTKB = "UniProtKB"
    UNIPROTACCESSION = "UniProt Accession"
    HUGOGENENOMENCLATURECOMMITTEE_HGNC = "HUGO Gene Nomenclature Committee (HGNC)"
    HUMANPROTEINREFERENCEDATABASE_HPRD = "Human Protein Reference Database (HPRD)"
    GENATLAS = "GenAtlas"
    GENECARDS = "GeneCards"
    GENBANKGENEDATABASE = "GenBank Gene Database"
    GENBANKPROTEINDATABASE = "GenBank Protein Database"
    CHEMBL = "ChEMBL"
    IUPHAR = "IUPHAR"
    GUIDETOPHARMACOLOGY = "Guide to Pharmacology"


class Knownaction:
    YES = "yes"
    NO = "no"
    UNKNOWN = "unknown"


class Productcountry:
    """Drug products are currently only imported from the U.S. (FDA) and Canada (Canadian Drug Product Database, or DPD)."""

    US = "US"
    CANADA = "Canada"
    EU = "EU"


class Productsource:
    """Drug products are currently only imported from the FDA and the Canadian Drug Product Database, or DPD."""

    FDANDC = "FDA NDC"
    DPD = "DPD"
    EMA = "EMA"


class Experimentalpropertykind:
    WATERSOLUBILITY = "Water Solubility"
    MELTINGPOINT = "Melting Point"
    BOILINGPOINT = "Boiling Point"
    LOGP = "logP"
    LOGS = "logS"
    HYDROPHOBICITY = "Hydrophobicity"
    ISOELECTRICPOINT = "Isoelectric Point"
    CACO2PERMEABILITY = "caco2 Permeability"
    PKA = "pKa"
    MOLECULARWEIGHT = "Molecular Weight"
    MOLECULARFORMULA = "Molecular Formula"
    RADIOACTIVITY = "Radioactivity"
