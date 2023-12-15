# import re
from drugbank.enums import Experimentalpropertykind
from drugbank.models import *


class Action:
    ...


class Drugbankmetaboliteidvalue:
    DBMET = r"DBMET[0-9]{5}"


class Drugbankdrugsaltidvalue:
    DB = r"DB[0-9]{5}"
    DBSALT = r"DBSALT[0-9]{6}"
    APRD = r"APRD[0-9]{5}"
    BIOD = r"BIOD[0-9]{5}"
    BTD = r"BTD[0-9]{5}"
    EXPT = r"EXPT[0-9]{5}"
    NUTR = r"NUTR[0-9]{5}"


class TagIdentifier:
    Tags = {
        "drug": {
            "model": Drug,
            # pattern: <drug type="biotech" created="2005-06-13" updated="2023-01-03">
            "pattern": r"<drug type=\"[a-z]+\" created=\"[0-9]{4}-[0-9]{2}-[0-9]{2}\" updated=\"[0-9]{4}-[0-9]{2}-[0-9]{2}\">",
            "end_pattern": r"</drug>",
        },
        "drugbank-id": {
            "model": str,
            # pattern: <drugbank-id primary="true">DB00001</drugbank-id>
            "pattern": r"<drugbank-id primary=\"[a-z]+\">[A-Z]{2}[0-9]{5}</drugbank-id>",
            "end_pattern": r"</drugbank-id>",
        },
        "name": {
            "model": str,
            # pattern: <name>Lepirudin</name>
            "pattern": r"<name>[a-zA-Z0-9]+</name>",
            "end_pattern": r"</name>",
        },
        "description": {
            "model": str,
            # pattern: <description>Lepirudin is identical to natural hirudin except for substitution of leucine for isoleucine at the N-terminal end of the molecule and the absence of a sulfate group on the tyrosine at position 63. It is produced via yeast cells. Bayer ceased the production of lepirudin (Refludan) effective May 31, 2012.</description>
            "pattern": r"<description>[a-zA-Z0-9]+</description>",
            "end_pattern": r"</description>",
        },
        "cas-number": {
            "model": str,
            # pattern: <cas-number>138068-37-8</cas-number>
            "pattern": r"<cas-number>[0-9]+-[0-9]+-[0-9]+</cas-number>",
            "end_pattern": r"</cas-number>",
        },
        "unii": {
            "model": str,
            # pattern: <unii>Y43GF64R34</unii>
            "pattern": r"<unii>[A-Z0-9]+</unii>",
            "end_pattern": r"</unii>",
        },
        "state": {
            "model": str,
            # pattern: <state>liquid</state>
            "pattern": r"<state>[a-z]+</state>",
            "end_pattern": r"</state>",
        },
        "groups": {
            "model": Groups,
            # pattern: <groups>
            "pattern": r"<groups>",
            "end_pattern": r"</groups>",
        },
        "group": {
            "model": str,
            # pattern: <group>approved</group>
            "pattern": r"<group>[a-z]+</group>",
            "end_pattern": r"</group>",
        },
        "general-references": {
            #! TODO: Bug
            "model": str,
            # pattern: <general-references>
            "pattern": r"<general-references>",
            "end_pattern": r"</general-references>",
        },
        "articles": {
            "model": Articles,
            # pattern: <articles>
            "pattern": r"<articles>",
            "end_pattern": r"</articles>",
        },
        "article": {
            "model": Article,
            # pattern: <article>
            "pattern": r"<article>",
            "end_pattern": r"</article>",
        },
        "pubmed-id": {
            "model": str,
            # pattern: <pubmed-id>11090226</pubmed-id>
            "pattern": r"<pubmed-id>[0-9]+</pubmed-id>",
            "end_pattern": r"</pubmed-id>",
        },
        "mesh-id": {
            "model": str,
            # pattern: <mesh-id>D007333</mesh-id>
            "pattern": r"<mesh-id>[A-Z0-9]+</mesh-id>",
            "end_pattern": r"</mesh-id>",
        },
        "synthesis-reference": {
            "model": str,
            # pattern: <synthesis-reference>Markwardt F, Walsmann P: Hirudin as an inhibitor of thrombin. Science. 1954 Aug 13;120(3118):234-8. [PubMed:13174787]</synthesis-reference>
            "pattern": r"<synthesis-reference>[a-zA-Z0-9]+</synthesis-reference>",
            "end_pattern": r"</synthesis-reference>",
        },
        "indication": {
            "model": str,
            # pattern: <indication>For the treatment of heparin-induced thrombocytopenia</indication>
            "pattern": r"<indication>[a-zA-Z0-9]+</indication>",
            "end_pattern": r"</indication>",
        },
        "pharmacodynamics": {
            "model": str,
            # pattern: <pharmacodynamics>Lepirudin is used to break up clots and to reduce thrombocytopenia.</pharmacodynamics>
            "pattern": r"<pharmacodynamics>[a-zA-Z0-9]+</pharmacodynamics>",
            "end_pattern": r"</pharmacodynamics>",
        },
        "mechanism-of-action": {
            "model": str,
            # pattern: <mechanism-of-action>Lepirudin forms a stable non-covalent complex with alpha-thrombin, thereby abolishing its ability to cleave fibrinogen and initiate the clotting cascade.</mechanism-of-action>
            "pattern": r"<mechanism-of-action>[a-zA-Z0-9]+</mechanism-of-action>",
            "end_pattern": r"</mechanism-of-action>",
        },
        "toxicity": {
            "model": str,
            # pattern: <toxicity>LD50=32 mg/kg (orally in mice)</toxicity>
            "pattern": r"<toxicity>[a-zA-Z0-9]+</toxicity>",
            "end_pattern": r"</toxicity>",
        },
        "metabolism": {
            "model": str,
            # pattern: <metabolism>Not Available</metabolism>
            "pattern": r"<metabolism>[a-zA-Z0-9]+</metabolism>",
            "end_pattern": r"</metabolism>",
        },
        "absorption": {
            "model": str,
            # pattern: <absorption>Not Available</absorption>
            "pattern": r"<absorption>[a-zA-Z0-9]+</absorption>",
            "end_pattern": r"</absorption>",
        },
        "half-life": {
            "model": str,
            # pattern: <half-life>1.3 hours</half-life>
            "pattern": r"<half-life>[a-zA-Z0-9]+</half-life>",
            "end_pattern": r"</half-life>",
        },
        "protein-binding": {
            "model": str,
            # pattern: <protein-binding>Not Available</protein-binding>
            "pattern": r"<protein-binding>[a-zA-Z0-9]+</protein-binding>",
            "end_pattern": r"</protein-binding>",
        },
        "route-of-elimination": {
            "model": str,
            # pattern: <route-of-elimination>Not Available</route-of-elimination>
            "pattern": r"<route-of-elimination>[a-zA-Z0-9]+</route-of-elimination>",
            "end_pattern": r"</route-of-elimination>",
        },
        "volume-of-distribution": {
            "model": str,
            # pattern: <volume-of-distribution>Not Available</volume-of-distribution>
            "pattern": r"<volume-of-distribution>[a-zA-Z0-9]+</volume-of-distribution>",
            "end_pattern": r"</volume-of-distribution>",
        },
        "clearance": {
            "model": str,
            # pattern: <clearance>Not Available</clearance>
            "pattern": r"<clearance>[a-zA-Z0-9]+</clearance>",
            "end_pattern": r"</clearance>",
        },
        "classification": {
            "model": Classification,
            # pattern: <classification>
            "pattern": r"<classification>",
            "end_pattern": r"</classification>",
        },
        "direct-parent": {
            "model": str,
            # pattern: <direct-parent>Peptides</direct-parent>
            "pattern": r"<direct-parent>[a-zA-Z0-9]+</direct-parent>",
            "end_pattern": r"</direct-parent>",
        },
        "kingdom": {
            "model": str,
            # pattern: <kingdom>Organic Compounds</kingdom>
            "pattern": r"<kingdom>[a-zA-Z0-9]+</kingdom>",
            "end_pattern": r"</kingdom>",
        },
        "superclass": {
            "model": str,
            # pattern: <superclass>Organic Acids and Derivatives</superclass>
            "pattern": r"<superclass>[a-zA-Z0-9]+</superclass>",
            "end_pattern": r"</superclass>",
        },
        "class": {
            "model": str,
            # pattern: <class>Carboxylic Acids and Derivatives</class>
            "pattern": r"<class>[a-zA-Z0-9]+</class>",
            "end_pattern": r"</class>",
        },
        "subclass": {
            "model": str,
            # pattern: <subclass>Amino Acids, Peptides, and Analogues</subclass>
            "pattern": r"<subclass>[a-zA-Z0-9]+</subclass>",
            "end_pattern": r"</subclass>",
        },
        "alternative-parent": {
            "model": str,
            # pattern: <alternative-parent>Not Available</alternative-parent>
            "pattern": r"<alternative-parent>[a-zA-Z0-9]+</alternative-parent>",
            "end_pattern": r"</alternative-parent>",
        },
        "substituent": {
            "model": str,
            # pattern: <substituent>Not Available</substituent>
            "pattern": r"<substituent>[a-zA-Z0-9]+</substituent>",
            "end_pattern": r"</substituent>",
        },
        "description": {
            "model": str,
            # pattern: <description>Not Available</description>
            "pattern": r"<description>[a-zA-Z0-9]+</description>",
            "end_pattern": r"</description>",
        },
        "synonyms": {
            "model": Synonyms,
            # pattern: <synonyms>
            "pattern": r"<synonyms>",
            "end_pattern": r"</synonyms>",
        },
        "synonym": {
            "model": str,
            # pattern: <synonym>Lepirudin</synonym>
            "pattern": r"<synonym>[a-zA-Z0-9]+</synonym>",
            "end_pattern": r"</synonym>",
        },
        "international-brands": {
            "model": Internationalbrands,
            # pattern: <international-brands>
            "pattern": r"<international-brands>",
            "end_pattern": r"</international-brands>",
        },
        "international-brand": {
            "model": Internationalbrand,
            # pattern: <international-brand>Refludan</international-brand>
            "pattern": r"<international-brand>[a-zA-Z0-9]+</international-brand>",
            "end_pattern": r"</international-brand>",
        },
        "mixtures": {
            "model": Mixtures,
            # pattern: <mixtures>
            "pattern": r"<mixtures>",
            "end_pattern": r"</mixtures>",
        },
        "mixture": {
            "model": str,
            # pattern: <mixture>Angiomax</mixture>
            "pattern": r"<mixture>[a-zA-Z0-9]+</mixture>",
            "end_pattern": r"</mixture>",
        },
        "salts": {
            "model": Salts,
            # pattern: <salts>
            "pattern": r"<salts>",
            "end_pattern": r"</salts>",
        },
        "salt": {
            "model": str,
            # pattern: <salt>Not Available</salt>
            "pattern": r"<salt>[a-zA-Z0-9]+</salt>",
            "end_pattern": r"</salt>",
        },
        "brands": {
            "model": str,
            # pattern: <brands>
            "pattern": r"<brands>",
            "end_pattern": r"</brands>",
        },
        "brand": {
            "model": str,
            # pattern: <brand>Refludan</brand>
            "pattern": r"<brand>[a-zA-Z0-9]+</brand>",
            "end_pattern": r"</brand>",
        },
        "categories": {
            "model": Categorys,
            # pattern: <categories>
            "pattern": r"<categories>",
            "end_pattern": r"</categories>",
        },
        "category": {
            "model": str,
            # pattern: <category>Anticoagulants</category>
            "pattern": r"<category>[a-zA-Z0-9]+</category>",
            "end_pattern": r"</category>",
        },
        "affected-organisms": {
            "model": Affectedorganisms,
            # pattern: <affected-organisms>
            "pattern": r"<affected-organisms>",
            "end_pattern": r"</affected-organisms>",
        },
        "affected-organism": {
            "model": str,
            # pattern: <affected-organism>Humans and other mammals</affected-organism>
            "pattern": r"<affected-organism>[a-zA-Z0-9]+</affected-organism>",
            "end_pattern": r"</affected-organism>",
        },
        "dosages": {
            "model": Dosages,
            # pattern: <dosages>
            "pattern": r"<dosages>",
            "end_pattern": r"</dosages>",
        },
        "dosage": {
            "model": str,
            # pattern: <dosage>
            "pattern": r"<dosage>",
            "end_pattern": r"</dosage>",
        },
        "form": {
            "model": str,
            # pattern: <form>Not Available</form>
            "pattern": r"<form>[a-zA-Z0-9]+</form>",
            "end_pattern": r"</form>",
        },
        "route": {
            "model": str,
            # pattern: <route>Not Available</route>
            "pattern": r"<route>[a-zA-Z0-9]+</route>",
            "end_pattern": r"</route>",
        },
        "strength": {
            "model": str,
            # pattern: <strength>Not Available</strength>
            "pattern": r"<strength>[a-zA-Z0-9]+</strength>",
            "end_pattern": r"</strength>",
        },
        "overdosage": {
            "model": str,
            # pattern: <overdosage>Not Available</overdosage>
            "pattern": r"<overdosage>[a-zA-Z0-9]+</overdosage>",
            "end_pattern": r"</overdosage>",
        },
        "route-of-administration": {
            "model": str,
            # pattern: <route-of-administration>intravenous</route-of-administration>
            "pattern": r"<route-of-administration>[a-zA-Z0-9]+</route-of-administration>",
            "end_pattern": r"</route-of-administration>",
        },
        "ahfs-codes": {
            "model": Ahfscodes,
            # pattern: <ahfs-codes>
            "pattern": r"<ahfs-codes>",
            "end_pattern": r"</ahfs-codes>",
        },
        "ahfs-code": {
            "model": str,
            # pattern: <ahfs-code>92:00.00</ahfs-code>
            "pattern": r"<ahfs-code>[a-zA-Z0-9]+</ahfs-code>",
            "end_pattern": r"</ahfs-code>",
        },
        "pdb-entries": {
            "model": Pdbentrys,
            # pattern: <pdb-entries>
            "pattern": r"<pdb-entries>",
            "end_pattern": r"</pdb-entries>",
        },
        "pdb-entry": {
            "model": str,
            # pattern: <pdb-entry>1D9G</pdb-entry>
            "pattern": r"<pdb-entry>[a-zA-Z0-9]+</pdb-entry>",
            "end_pattern": r"</pdb-entry>",
        },
        "fdas": {
            #!Bug
            "model": str,
            # pattern: <fdas>
            "pattern": r"<fdas>",
            "end_pattern": r"</fdas>",
        },
        "fda": {
            "model": str,
            # pattern: <fda>Not Available</fda>
            "pattern": r"<fda>[a-zA-Z0-9]+</fda>",
            "end_pattern": r"</fda>",
        },
        "msds": {
            #! Bug
            "model": str,
            # pattern: <msds>
            "pattern": r"<msds>",
            "end_pattern": r"</msds>",
        },
        "msds": {
            "model": str,
            # pattern: <msds>Not Available</msds>
            "pattern": r"<msds>[a-zA-Z0-9]+</msds>",
            "end_pattern": r"</msds>",
        },
        "patents": {
            "model": Patents,
            # pattern: <patents>
            "pattern": r"<patents>",
            "end_pattern": r"</patents>",
        },
        "patent": {
            "model": str,
            # pattern: <patent>
            "pattern": r"<patent>",
            "end_pattern": r"</patent>",
        },
        "number": {
            "model": str,
            # pattern: <number>US20080015107</number>
            "pattern": r"<number>[a-zA-Z0-9]+</number>",
            "end_pattern": r"</number>",
        },
        "country": {
            "model": str,
            # pattern: <country>United States</country>
            "pattern": r"<country>[a-zA-Z0-9]+</country>",
            "end_pattern": r"</country>",
        },
        "approved": {
            "model": str,
            # pattern: <approved>2008-01-17</approved>
            "pattern": r"<approved>[a-zA-Z0-9]+</approved>",
            "end_pattern": r"</approved>",
        },
        "expires": {
            "model": str,
            # pattern: <expires>2026-01-17</expires>
            "pattern": r"<expires>[a-zA-Z0-9]+</expires>",
            "end_pattern": r"</expires>",
        },
        "pediatric-extension": {
            "model": str,
            # pattern: <pediatric-extension>No</pediatric-extension>
            "pattern": r"<pediatric-extension>[a-zA-Z0-9]+</pediatric-extension>",
            "end_pattern": r"</pediatric-extension>",
        },
        "supplements": {
            #! Bug
            "model": str,
            # pattern: <supplements>
            "pattern": r"<supplements>",
            "end_pattern": r"</supplements>",
        },
        "supplement": {
            "model": str,
            # pattern: <supplement>
            "pattern": r"<supplement>",
            "end_pattern": r"</supplement>",
        },
        "number": {
            "model": str,
            # pattern: <number>US20080015107</number>
            "pattern": r"<number>[a-zA-Z0-9]+</number>",
            "end_pattern": r"</number>",
        },
        "country": {
            "model": str,
            # pattern: <country>United States</country>
            "pattern": r"<country>[a-zA-Z0-9]+</country>",
            "end_pattern": r"</country>",
        },
        "approved": {
            "model": str,
            # pattern: <approved>2008-01-17</approved>
            "pattern": r"<approved>[a-zA-Z0-9]+</approved>",
            "end_pattern": r"</approved>",
        },
        "expires": {
            "model": str,
            # pattern: <expires>2026-01-17</expires>
            "pattern": r"<expires>[a-zA-Z0-9]+</expires>",
            "end_pattern": r"</expires>",
        },
        "pediatric-extension": {
            "model": str,
            # pattern: <pediatric-extension>No</pediatric-extension>
            "pattern": r"<pediatric-extension>[a-zA-Z0-9]+</pediatric-extension>",
            "end_pattern": r"</pediatric-extension>",
        },
        "packagers": {
            "model": Packagers,
            # pattern: <packagers>
            "pattern": r"<packagers>",
            "end_pattern": r"</packagers>",
        },
        "packager": {
            "model": str,
            # pattern: <packager>
            "pattern": r"<packager>",
            "end_pattern": r"</packager>",
        },
        "name": {
            "model": str,
            # pattern: <name>Cardinal Health</name>
            "pattern": r"<name>[a-zA-Z0-9]+</name>",
            "end_pattern": r"</name>",
        },
        "url": {
            "model": str,
            # pattern: <url>http://www.cardinal.com</url>
            "pattern": r"<url>[a-zA-Z0-9]+</url>",
            "end_pattern": r"</url>",
        },
        "prices": {
            "model": Prices,
            # pattern: <prices>
            "pattern": r"<prices>",
            "end_pattern": r"</prices>",
        },
        "price": {
            "model": str,
            # pattern: <price>
            "pattern": r"<price>",
            "end_pattern": r"</price>",
        },
        "description": {
            "model": str,
            # pattern: <description>Not Available</description>
            "pattern": r"<description>[a-zA-Z0-9]+</description>",
            "end_pattern": r"</description>",
        },
        "cost": {
            "model": str,
            # pattern: <cost>Not Available</cost>
            "pattern": r"<cost>[a-zA-Z0-9]+</cost>",
            "end_pattern": r"</cost>",
        },
        "unit": {
            "model": str,
            # pattern: <unit>Not Available</unit>
            "pattern": r"<unit>[a-zA-Z0-9]+</unit>",
            "end_pattern": r"</unit>",
        },
        "ndcs": {
            #!bug
            "model": str,
            # pattern: <ndcs>
            "pattern": r"<ndcs>",
            "end_pattern": r"</ndcs>",
        },
        "ndc": {
            "model": str,
            # pattern: <ndc>
            "pattern": r"<ndc>",
            "end_pattern": r"</ndc>",
        },
        "ndc-id": {
            "model": str,
            # pattern: <ndc-id>0002-1200</ndc-id>
            "pattern": r"<ndc-id>[a-zA-Z0-9]+</ndc-id>",
            "end_pattern": r"</ndc-id>",
        },
        "product": {
            "model": Product,
            # pattern: <product>
            "pattern": r"<product>",
            "end_pattern": r"</product>",
        },
        "name": {
            "model": str,
            # pattern: <name>Refludan</name>
            "pattern": r"<name>[a-zA-Z0-9]+</name>",
            "end_pattern": r"</name>",
        },
        "labeller": {
            "model": str,
            # pattern: <labeller>Bayer</labeller>
            "pattern": r"<labeller>[a-zA-Z0-9]+</labeller>",
            "end_pattern": r"</labeller>",
        },
        "ndc-product-code": {
            "model": str,
            # pattern: <ndc-product-code>0002-1200</ndc-product-code>
            "pattern": r"<ndc-product-code>[a-zA-Z0-9]+</ndc-product-code>",
            "end_pattern": r"</ndc-product-code>",
        },
        "dpd-id": {
            "model": str,
            # pattern: <dpd-id>00021200</dpd-id>
            "pattern": r"<dpd-id>[a-zA-Z0-9]+</dpd-id>",
            "end_pattern": r"</dpd-id>",
        },
        "ema-product-code": {
            "model": str,
            # pattern: <ema-product-code>Not Available</ema-product-code>
            "pattern": r"<ema-product-code>[a-zA-Z0-9]+</ema-product-code>",
            "end_pattern": r"</ema-product-code>",
        },
        "started-marketing-on": {
            "model": str,
            # pattern: <started-marketing-on>1998-05-01</started-marketing-on>
            "pattern": r"<started-marketing-on>[a-zA-Z0-9]+</started-marketing-on>",
            "end_pattern": r"</started-marketing-on>",
        },
        "ended-marketing-on": {
            "model": str,
            # pattern: <ended-marketing-on>2012-05-31</ended-marketing-on>
            "pattern": r"<ended-marketing-on>[a-zA-Z0-9]+</ended-marketing-on>",
            "end_pattern": r"</ended-marketing-on>",
        },
        "dosage-form": {
            "model": str,
            # pattern: <dosage-form>Injection, powder, lyophilized, for solution</dosage-form>
            "pattern": r"<dosage-form>[a-zA-Z0-9]+</dosage-form>",
            "end_pattern": r"</dosage-form>",
        },
        "strength": {
            "model": str,
            # pattern: <strength>50 mg</strength>
            "pattern": r"<strength>[a-zA-Z0-9]+</strength>",
            "end_pattern": r"</strength>",
        },
        "route": {
            "model": str,
            # pattern: <route>intravenous</route>
            "pattern": r"<route>[a-zA-Z0-9]+</route>",
            "end_pattern": r"</route>",
        },
        "fda-application-number": {
            "model": str,
            # pattern: <fda-application-number>ANDA076276</fda-application-number>
            "pattern": r"<fda-application-number>[a-zA-Z0-9]+</fda-application-number>",
            "end_pattern": r"</fda-application-number>",
        },
        "generic": {
            "model": str,
            # pattern: <generic>No</generic>
            "pattern": r"<generic>[a-zA-Z0-9]+</generic>",
            "end_pattern": r"</generic>",
        },
        "over-the-counter": {
            "model": str,
            # pattern: <over-the-counter>No</over-the-counter>
            "pattern": r"<over-the-counter>[a-zA-Z0-9]+</over-the-counter>",
            "end_pattern": r"</over-the-counter>",
        },
        "approved": {
            "model": str,
            # pattern: <approved>Yes</approved>
            "pattern": r"<approved>[a-zA-Z0-9]+</approved>",
            "end_pattern": r"</approved>",
        },
        "country": {
            "model": str,
            # pattern: <country>United States</country>
            "pattern": r"<country>[a-zA-Z0-9]+</country>",
            "end_pattern": r"</country>",
        },
        "source": {
            "model": str,
            # pattern: <source>DrugBank</source>
            "pattern": r"<source>[a-zA-Z0-9]+</source>",
            "end_pattern": r"</source>",
        },
        "products": {
            "model": Products,
            # pattern: <products>
            "pattern": r"<products>",
            "end_pattern": r"</products>",
        },
        "atc-codes": {
            "model": Atccodes,
            "pattern": r"<atc-codes>",
            "end_pattern": r"</atc-codes>",
        },
        "ahfs-codes": {
            "model": Ahfscodes,
            # pattern: <ahfs-codes>
            "pattern": r"<ahfs-codes>",
            "end_pattern": r"</ahfs-codes>",
        },
        "level": {
            "model": Atccodelevel,
            # pattern:<level code="B01AE">Direct thrombin inhibitors</level>
            "pattern": r"<level code=\"[a-zA-Z0-9]+\">[a-zA-Z0-9]+</level>",
            "end_pattern": r"</level>",
        },
        "atc-code": {
            "model": Atccode,
            # pattern: <atc-code>B01AE02</atc-code>
            "pattern": r"<atc-code>[a-zA-Z0-9]+</atc-code>",
            "end_pattern": r"</atc-code>",
        },
        "food-interactions": {
            "model": Foodinteractions,
            # pattern: <food-interactions>
            "pattern": r"<food-interactions>",
            "end_pattern": r"</food-interactions>",
        },
        "food-interaction": {
            "model": str,
            # pattern: <food-interaction>Not Available</food-interaction>
            "pattern": r"<food-interaction>[a-zA-Z0-9]+</food-interaction>",
            "end_pattern": r"</food-interaction>",
        },
        "sequences": {
            "model": Sequences,
            # pattern: <sequences>
            "pattern": r"<sequences>",
            "end_pattern": r"</sequences>",
        },
        "sequence": {
            "model": str,
            # pattern: <sequence>
            "pattern": r"<sequence>",
            "end_pattern": r"</sequence>",
        },
        "format": {
            "model": str,
            # pattern: <format>FASTA</format>
            "pattern": r"<format>[a-zA-Z0-9]+</format>",
            "end_pattern": r"</format>",
        },
        "id": {
            "model": str,
            # pattern: <id>Not Available</id>
            "pattern": r"<id>[a-zA-Z0-9]+</id>",
            "end_pattern": r"</id>",
        },
        "drug-interactions": {
            "model": Druginteractions,
            # pattern: <drug-interactions>
            "pattern": r"<drug-interactions>",
            "end_pattern": r"</drug-interactions>",
        },
        "drug-interaction": {
            "model": Druginteraction,
            # pattern: <drug-interaction>
            "pattern": r"<drug-interaction>",
            "end_pattern": r"</drug-interaction>",
        },
        "drugbank-id": {
            "model": str,
            # pattern: <drugbank-id>DB00001</drugbank-id>
            "pattern": r"<drugbank-id>[a-zA-Z0-9]+</drugbank-id>",
            "end_pattern": r"</drugbank-id>",
        },
        "name": {
            "model": str,
            # pattern: <name>Leuprolide</name>
            "pattern": r"<name>[a-zA-Z0-9]+</name>",
            "end_pattern": r"</name>",
        },
        "sequence": {
            "model": str,
            # pattern: <sequence>GPMAHPR</sequence>
            "pattern": r"<sequence>[a-zA-Z0-9]+</sequence>",
            "end_pattern": r"</sequence>",
        },
        "experimental-properties": {
            "model": Experimentalpropertykind,
            # pattern: <experimental-properties>
            "pattern": r"<experimental-properties>",
            "end_pattern": r"</experimental-properties>",
        },
        "property": {
            "model": str,
            # pattern: <property>
            "pattern": r"<property>",
            "end_pattern": r"</property>",
        },
        "kind": {
            "model": str,
            # pattern: <kind>logP</kind>
            "pattern": r"<kind>[a-zA-Z0-9]+</kind>",
            "end_pattern": r"</kind>",
        },
        "value": {
            "model": str,
            # pattern: <value>0.41</value>
            "pattern": r"<value>[a-zA-Z0-9]+</value>",
            "end_pattern": r"</value>",
        },
        "source": {
            "model": str,
            # pattern: <source>Not Available</source>
            "pattern": r"<source>[a-zA-Z0-9]+</source>",
            "end_pattern": r"</source>",
        },
        "external-identifiers": {
            "model": Externalidentifiers,
            # pattern: <external-identifiers>
            "pattern": r"<external-identifiers>",
            "end_pattern": r"</external-identifiers>",
        },
        "external-identifier": {
            "model": str,
            # pattern: <external-identifier>
            "pattern": r"<external-identifier>",
            "end_pattern": r"</external-identifier>",
        },
        "resource": {
            "model": str,
            # pattern: <resource>Not Available</resource>
            "pattern": r"<resource>[a-zA-Z0-9]+</resource>",
            "end_pattern": r"</resource>",
        },
        "identifier": {
            "model": str,
            # pattern: <identifier>Not Available</identifier>
            "pattern": r"<identifier>[a-zA-Z0-9]+</identifier>",
            "end_pattern": r"</identifier>",
        },
        "protein-sequences": {
            #! Bug
            "model": str,
            # pattern: <protein-sequences>
            "pattern": r"<protein-sequences>",
            "end_pattern": r"</protein-sequences>",
        },
        "protein-sequence": {
            "model": str,
            # pattern: <protein-sequence>
            "pattern": r"<protein-sequence>",
            "end_pattern": r"</protein-sequence>",
        },
        "pathways": {
            "model": Pathways,
            # pattern: <pathways>
            "pattern": r"<pathways>",
            "end_pattern": r"</pathways>",
        },
        "pathway": {
            "model": str,
            # pattern: <pathway>
            "pattern": r"<pathway>",
            "end_pattern": r"</pathway>",
        },
        "smpdb-id": {
            "model": str,
            # pattern: <smpdb-id>Not Available</smpdb-id>
            "pattern": r"<smpdb-id>[a-zA-Z0-9]+</smpdb-id>",
            "end_pattern": r"</smpdb-id>",
        },
        "name": {
            "model": str,
            # pattern: <name>Not Available</name>
            "pattern": r"<name>[a-zA-Z0-9]+</name>",
            "end_pattern": r"</name>",
        },
        "enzymes": {
            "model": Enzymes,
            # pattern: <enzymes>
            "pattern": r"<enzymes>",
            "end_pattern": r"</enzymes>",
        },
        "uniprot-id": {
            "model": str,
            # pattern: <uniprot-id>Not Available</uniprot-id>
            "pattern": r"<uniprot-id>[a-zA-Z0-9]+</uniprot-id>",
            "end_pattern": r"</uniprot-id>",
        },
        "reactions": {
            "model": Reactions,
            # pattern: <reactions>
            "pattern": r"<reactions>",
            "end_pattern": r"</reactions>",
        },
        "reaction": {
            "model": str,
            # pattern: <reaction>
            "pattern": r"<reaction>",
            "end_pattern": r"</reaction>",
        },
        "sequence": {
            "model": str,
            # pattern: <sequence>Not Available</sequence>
            "pattern": r"<sequence>[a-zA-Z0-9]+</sequence>",
            "end_pattern": r"</sequence>",
        },
        "left-element": {
            "model": str,
            # pattern: <left-element>Not Available</left-element>
            "pattern": r"<left-element>[a-zA-Z0-9]+</left-element>",
            "end_pattern": r"</left-element>",
        },
        "right-element": {
            "model": str,
            # pattern: <right-element>Not Available</right-element>
            "pattern": r"<right-element>[a-zA-Z0-9]+</right-element>",
            "end_pattern": r"</right-element>",
        },
        "targets": {
            "model": Targets,
            # pattern: <targets>
            "pattern": r"<targets>",
            "end_pattern": r"</targets>",
        },
        "target": {
            "model": Target,
            # pattern: <target position="1">
            "pattern": r"<target position=\"[0-9]+\">",
            "end_pattern": r"</target>",
        },
        "id": {
            "model": str,
            # pattern: <id>BE0000048</id>
            "pattern": r"<id>[a-zA-Z0-9]+</id>",
            "end_pattern": r"</id>",
        },
        "organism": {
            "model": str,
            # pattern: <organism>Humans</organism>
            "pattern": r"<organism>[a-zA-Z0-9]+</organism>",
            "end_pattern": r"</organism>",
        },
        "known-action": {
            "model": str,
            # pattern: <known-action>yes</known-action>
            "pattern": r"<known-action>[a-zA-Z0-9]+</known-action>",
            "end_pattern": r"</known-action>",
        },
        "actions": {
            "model": Actions,
            # pattern: <actions>
            "pattern": r"<actions>",
            "end_pattern": r"</actions>",
        },
        "action": {
            "model": str,
            # pattern: <action>inhibitor</action>
            "pattern": r"<action>[a-zA-Z0-9]+</action>",
            "end_pattern": r"</action>",
        },
        "general-function": {
            "model": str,
            # pattern: <general-function>Not Available</general-function>
            "pattern": r"<general-function>[a-zA-Z0-9]+</general-function>",
            "end_pattern": r"</general-function>",
        },
        "specific-function": {
            "model": str,
            # pattern: <specific-function>Not Available</specific-function>
            "pattern": r"<specific-function>[a-zA-Z0-9]+</specific-function>",
            "end_pattern": r"</specific-function>",
        },
        "gene-name": "",
    }
