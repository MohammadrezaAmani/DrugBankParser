class DrugBankID:
    def __init__(
        self, primary: str = None, secondary: str = None, external: str = None
    ) -> None:
        self.primary = primary
        self.secondary = secondary
        self.external = external


class Name:
    def __init__(self, name: str = None) -> None:
        self.name = name


class Description:
    def __init__(self, description: str = None) -> None:
        self.description = description


class Drug:
    def __init__(
        self,
        drugbankid,
        name,
        description,
        casnumber,
        unii,
        averagemass,
        monoisotopicmass,
        state,
        groups,
        generalreferences,
        synthesisreference,
        indication,
        pharmacodynamics,
        mechanismofaction,
        toxicity,
        metabolism,
        absorption,
        halflife,
        proteinbinding,
        routeofelimination,
        volumeofdistribution,
        clearance,
        classification,
        salts,
        synonyms,
        products,
        internationalbrands,
        mixtures,
        packagers,
        manufacturers,
        prices,
        categories,
        affectedorganisms,
        dosages,
        atccodes,
        ahfscodes,
        pdbentries,
        fdalabel,
        msds,
        patents,
        foodinteractions,
        druginteractions,
        sequences,
        calculatedproperties,
        experimentalproperties,
        externalidentifiers,
        externallinks,
        pathways,
        reactions,
        snpeffects,
        snpadversedrugreactions,
        targets,
        enzymes,
        carriers,
        transporters,
        type_,
    ) -> None:
        self.drugbankid = drugbankid
        self.name = name
        self.description = description
        self.casnumber = casnumber
        self.unii = unii
        self.averagemass = averagemass
        self.monoisotopicmass = monoisotopicmass
        self.state = state
        self.groups = groups
        self.generalreferences = generalreferences
        self.synthesisreference = synthesisreference
        self.indication = indication
        self.pharmacodynamics = pharmacodynamics
        self.mechanismofaction = mechanismofaction
        self.toxicity = toxicity
        self.metabolism = metabolism
        self.absorption = absorption
        self.halflife = halflife
        self.proteinbinding = proteinbinding
        self.routeofelimination = routeofelimination
        self.volumeofdistribution = volumeofdistribution
        self.clearance = clearance
        self.classification = classification
        self.salts = salts
        self.synonyms = synonyms
        self.products = products
        self.internationalbrands = internationalbrands
        self.mixtures = mixtures
        self.packagers = packagers
        self.manufacturers = manufacturers
        self.prices = prices
        self.categories = categories
        self.affectedorganisms = affectedorganisms
        self.dosages = dosages
        self.atccodes = atccodes
        self.ahfscodes = ahfscodes
        self.pdbentries = pdbentries
        self.fdalabel = fdalabel
        self.msds = msds
        self.patents = patents
        self.foodinteractions = foodinteractions
        self.druginteractions = druginteractions
        self.sequences = sequences
        self.calculatedproperties = calculatedproperties
        self.experimentalproperties = experimentalproperties
        self.externalidentifiers = externalidentifiers
        self.externallinks = externallinks
        self.pathways = pathways
        self.reactions = reactions
        self.snpeffects = snpeffects
        self.snpadversedrugreactions = snpadversedrugreactions
        self.targets = targets
        self.enzymes = enzymes
        self.carriers = carriers
        self.transporters = transporters
        self.type_ = type_


class Groups:
    def __init__(self, group) -> None:
        self.group = group


class Classification:
    """Drug classification is obtained from ClassyFire (http://classyfire.wishartlab.com)."""

    def __init__(
        self,
        description,
        directparent,
        kingdom,
        superclass,
        class_,
        subclass,
        alternativeparent,
        substituent,
    ) -> None:
        self.description = description
        self.directparent = directparent
        self.kingdom = kingdom
        self.superclass = superclass
        self.class_ = class_
        self.subclass = subclass
        self.alternativeparent = alternativeparent
        self.substituent = substituent


class Synonyms:
    def __init__(self, synonym) -> None:
        self.synonym = synonym


class Synonym:
    def __init__(self, language, coder) -> None:
        self.language = language
        self.coder = coder


class Salts:
    def __init__(self, salt) -> None:
        self.salt = salt


class Salt:
    def __init__(
        self, drugbankid, name, unii, casnumber, inchikey, averagemass, monoisotopicmass
    ) -> None:
        self.drugbankid = drugbankid
        self.name = name
        self.unii = unii
        self.casnumber = casnumber
        self.inchikey = inchikey
        self.averagemass = averagemass
        self.monoisotopicmass = monoisotopicmass


class Drugbankdrugsaltid:
    """The DrugBank ID is used to uniquely identify a drug or salt entry. There is a primary ID and several secondary IDs that come from older ID formats or merged entries."""

    def __init__(self, primary) -> None:
        self.primary = primary


class Drugbankmetaboliteid:
    """The metabolite DrugBank ID uniquely identifies a metabolite entry. Multiple IDs indicate a merged entry."""

    def __init__(self, primary) -> None:
        self.primary = primary


class Article:
    def __init__(self, refid, pubmedid, citation) -> None:
        self.refid = refid
        self.pubmedid = pubmedid
        self.citation = citation


class Textbook:
    def __init__(self, refid, isbn, citation) -> None:
        self.refid = refid
        self.isbn = isbn
        self.citation = citation


class Link:
    def __init__(self, refid, title, url) -> None:
        self.refid = refid
        self.title = title
        self.url = url


class Attachment:
    def __init__(self, refid, title, url) -> None:
        self.refid = refid
        self.title = title
        self.url = url


class Articles:
    def __init__(self, article) -> None:
        self.article = article


class Textbooks:
    def __init__(self, textbook) -> None:
        self.textbook = textbook


class Links:
    def __init__(self, link) -> None:
        self.link = link


class Attachments:
    def __init__(self, attachment) -> None:
        self.attachment = attachment


class References:
    """Articles are typically PubMed references, although there are some references which do not have a PubMed ID."""

    def __init__(self, articles, textbooks, links, attachments) -> None:
        self.articles = articles
        self.textbooks = textbooks
        self.links = links
        self.attachments = attachments


class Internationalbrands:
    def __init__(self, internationalbrand) -> None:
        self.internationalbrand = internationalbrand


class Internationalbrand:
    def __init__(self, name, company) -> None:
        self.name = name
        self.company = company


class Products:
    def __init__(self, product) -> None:
        self.product = product


class Product:
    """EMA marketing authorisation number from the European Medicines Agency Database. Only present for products that are authorised by central procedure for marketing in the European Union."""

    def __init__(
        self,
        name,
        labeller,
        ndcid,
        ndcproductcode,
        dpdid,
        emaproductcode,
        emamanumber,
        startedmarketingon,
        endedmarketingon,
        dosageform,
        strength,
        route,
        fdaapplicationnumber,
        generic,
        overthecounter,
        approved,
        country,
        source,
    ) -> None:
        self.name = name
        self.labeller = labeller
        self.ndcid = ndcid
        self.ndcproductcode = ndcproductcode
        self.dpdid = dpdid
        self.emaproductcode = emaproductcode
        self.emamanumber = emamanumber
        self.startedmarketingon = startedmarketingon
        self.endedmarketingon = endedmarketingon
        self.dosageform = dosageform
        self.strength = strength
        self.route = route
        self.fdaapplicationnumber = fdaapplicationnumber
        self.generic = generic
        self.overthecounter = overthecounter
        self.approved = approved
        self.country = country
        self.source = source


class Mixtures:
    def __init__(self, mixture) -> None:
        self.mixture = mixture


class Mixture:
    def __init__(self, name, ingredients, supplementalingredients) -> None:
        self.name = name
        self.ingredients = ingredients
        self.supplementalingredients = supplementalingredients


class Packagers:
    def __init__(self, packager) -> None:
        self.packager = packager


class Packager:
    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url


class Manufacturers:
    def __init__(self, manufacturer) -> None:
        self.manufacturer = manufacturer


class Manufacturer:
    def __init__(self, generic, url) -> None:
        self.generic = generic
        self.url = url


class Prices:
    def __init__(self, price) -> None:
        self.price = price


class Price:
    """The price for the given drug in US or Canadian currency."""

    def __init__(self, description, cost, currency) -> None:
        self.description = description
        self.cost = cost
        self.currency = currency


class Categorys:
    def __init__(self, category) -> None:
        self.category = category


class Category:
    def __init__(self, category, meshid) -> None:
        self.category = category
        self.meshid = meshid


class Affectedorganisms:
    def __init__(self, affectedorganism) -> None:
        self.affectedorganism = affectedorganism


class Dosages:
    def __init__(self, dosage) -> None:
        self.dosage = dosage


class Dosage:
    def __init__(self, form, route, strength) -> None:
        self.form = form
        self.route = route
        self.strength = strength


class Atccodes:
    def __init__(self, atccode) -> None:
        self.atccode = atccode


class Atccode:
    def __init__(self, level, code) -> None:
        self.level = level
        self.code = code


class Atccodelevel:
    def __init__(self, code) -> None:
        self.code = code


class Ahfscodes:
    def __init__(self, ahfscode) -> None:
        self.ahfscode = ahfscode


class Pdbentrys:
    def __init__(self, pdbentry) -> None:
        self.pdbentry = pdbentry


class Patents:
    def __init__(self, patent) -> None:
        self.patent = patent


class Patent:
    def __init__(self, number, country, approved, expires, pediatricextension) -> None:
        self.number = number
        self.country = country
        self.approved = approved
        self.expires = expires
        self.pediatricextension = pediatricextension


class Foodinteractions:
    def __init__(self, foodinteraction) -> None:
        self.foodinteraction = foodinteraction


class Druginteractions:
    def __init__(self, druginteraction) -> None:
        self.druginteraction = druginteraction


class Druginteraction:
    def __init__(self, drugbankid, name, description) -> None:
        self.drugbankid = drugbankid
        self.name = name
        self.description = description


class Sequences:
    def __init__(self, sequence, format) -> None:
        self.sequence = sequence
        self.format = format


class Calculatedpropertys:
    def __init__(self, property) -> None:
        self.property = property


class Calculatedproperty:
    def __init__(self, kind, value, source) -> None:
        self.kind = kind
        self.value = value
        self.source = source


class Experimentalpropertys:
    def __init__(self, property) -> None:
        self.property = property


class Experimentalproperty:
    def __init__(self, kind, value, source) -> None:
        self.kind = kind
        self.value = value
        self.source = source


class Externalidentifiers:
    def __init__(self, externalidentifier) -> None:
        self.externalidentifier = externalidentifier


class Externalidentifier:
    def __init__(self, resource, identifier) -> None:
        self.resource = resource
        self.identifier = identifier


class Externallinks:
    def __init__(self, externallink) -> None:
        self.externallink = externallink


class Externallink:
    def __init__(self, resource, url) -> None:
        self.resource = resource
        self.url = url


class Pathways:
    def __init__(self, pathway) -> None:
        self.pathway = pathway


class Pathway:
    def __init__(self, smpdbid, name, category, drugs, enzymes) -> None:
        self.smpdbid = smpdbid
        self.name = name
        self.category = category
        self.drugs = drugs
        self.enzymes = enzymes


class Pathwaydrugs:
    def __init__(self, drug) -> None:
        self.drug = drug


class Pathwaydrug:
    def __init__(self, drugbankid, name) -> None:
        self.drugbankid = drugbankid
        self.name = name


class Pathwayenzymes:
    def __init__(self, uniprotid) -> None:
        self.uniprotid = uniprotid


class Reactions:
    def __init__(self, reaction) -> None:
        self.reaction = reaction


class Reaction:
    def __init__(self, sequence, leftelement, rightelement, enzymes) -> None:
        self.sequence = sequence
        self.leftelement = leftelement
        self.rightelement = rightelement
        self.enzymes = enzymes


class Reactionelement:
    def __init__(self, drugbankid, name) -> None:
        self.drugbankid = drugbankid
        self.name = name


class Reactionenzymes:
    def __init__(self, enzyme) -> None:
        self.enzyme = enzyme


class Reactionenzyme:
    def __init__(self, drugbankid, name, uniprotid) -> None:
        self.drugbankid = drugbankid
        self.name = name
        self.uniprotid = uniprotid


class Snpeffects:
    def __init__(self, effect) -> None:
        self.effect = effect


class Snpeffect:
    def __init__(
        self,
        proteinname,
        genesymbol,
        uniprotid,
        rsid,
        allele,
        definingchange,
        description,
        pubmedid,
    ) -> None:
        self.proteinname = proteinname
        self.genesymbol = genesymbol
        self.uniprotid = uniprotid
        self.rsid = rsid
        self.allele = allele
        self.definingchange = definingchange
        self.description = description
        self.pubmedid = pubmedid


class Snpadversedrugreactions:
    def __init__(self, reaction) -> None:
        self.reaction = reaction


class Snpadversedrugreaction:
    def __init__(
        self,
        proteinname,
        genesymbol,
        uniprotid,
        rsid,
        allele,
        adversereaction,
        description,
        pubmedid,
    ) -> None:
        self.proteinname = proteinname
        self.genesymbol = genesymbol
        self.uniprotid = uniprotid
        self.rsid = rsid
        self.allele = allele
        self.adversereaction = adversereaction
        self.description = description
        self.pubmedid = pubmedid


class Polypeptides:
    def __init__(self, polypeptide) -> None:
        self.polypeptide = polypeptide


class Polypeptide:
    def __init__(
        self,
        name,
        generalfunction,
        specificfunction,
        genename,
        locus,
        cellularlocation,
        transmembraneregions,
        signalregions,
        theoreticalpi,
        molecularweight,
        chromosomelocation,
        organism,
        ncbitaxonomyid,
    ) -> None:
        self.name = name
        self.generalfunction = generalfunction
        self.specificfunction = specificfunction
        self.genename = genename
        self.locus = locus
        self.cellularlocation = cellularlocation
        self.transmembraneregions = transmembraneregions
        self.signalregions = signalregions
        self.theoreticalpi = theoreticalpi
        self.molecularweight = molecularweight
        self.chromosomelocation = chromosomelocation
        self.organism = organism
        self.ncbitaxonomyid = ncbitaxonomyid


class Organism:
    def __init__(
        self,
        externalidentifiers,
        synonyms,
        aminoacidsequence,
        genesequence,
        pfams,
        goclassifiersid,
        source,
    ) -> None:
        self.externalidentifiers = externalidentifiers
        self.synonyms = synonyms
        self.aminoacidsequence = aminoacidsequence
        self.genesequence = genesequence
        self.pfams = pfams
        self.goclassifiersid = goclassifiersid
        self.source = source


class Polypeptideexternalidentifiers:
    def __init__(self, externalidentifier) -> None:
        self.externalidentifier = externalidentifier


class Polypeptideexternalidentifier:
    def __init__(self, resource, identifier) -> None:
        self.resource = resource
        self.identifier = identifier


class Polypeptidesynonyms:
    def __init__(self, synonym) -> None:
        self.synonym = synonym


class Sequence:
    def __init__(self, format) -> None:
        self.format = format


class Pfams:
    def __init__(self, pfam) -> None:
        self.pfam = pfam


class Pfam:
    def __init__(self, identifier, name) -> None:
        self.identifier = identifier
        self.name = name


class Goclassifiers:
    def __init__(self, goclassifier) -> None:
        self.goclassifier = goclassifier


class Goclassifier:
    def __init__(self, category, description) -> None:
        self.category = category
        self.description = description


class Actions:
    def __init__(self, action) -> None:
        self.action = action


class Targets:
    def __init__(self, target) -> None:
        self.target = target


class Target:
    def __init__(self, interactantgroup, position) -> None:
        self.interactantgroup = interactantgroup
        self.position = position


class Enzymes:
    def __init__(self, enzyme) -> None:
        self.enzyme = enzyme


class Enzyme:
    def __init__(
        self, interactantgroup, inhibitionstrength, inductionstrength, position
    ) -> None:
        self.interactantgroup = interactantgroup
        self.inhibitionstrength = inhibitionstrength
        self.inductionstrength = inductionstrength
        self.position = position


class Carriers:
    def __init__(self, carrier) -> None:
        self.carrier = carrier


class Carrier:
    def __init__(self, interactantgroup, position) -> None:
        self.interactantgroup = interactantgroup
        self.position = position


class Transporters:
    def __init__(self, transporter) -> None:
        self.transporter = transporter


class Transporter:
    def __init__(self, interactantgroup, position) -> None:
        self.interactantgroup = interactantgroup
        self.position = position
