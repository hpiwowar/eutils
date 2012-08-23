"""Configuration information about NCBI's databases"""

# Used to figure out if efetch supports the start, stop, strand, and
# complexity fields
PUBLICATION_TYPE = 0
SEQUENCE_TYPE = 1

# Map from database name to database type
class DatabaseInfo:
    """stores NCBI's name for the database and its type"""
    def __init__(self, db, dbtype):
        self.db = db
        self.dbtype = dbtype

class DatabaseDict(dict):
    """map from name to DatabaseInfo for that database name

    Entries are also available through attributes like PUBMED,
    OMIM, and NUCLEOTIDE.
    """
    def gettype(self, db, dbtype = None):
        """Given a database name and optional type, return the database type"""
        if dbtype not in (None, SEQUENCE_TYPE, PUBLICATION_TYPE):
            raise TypeError("Unknown database type: %r" % (dbtype,))
        if dbtype is None:
            dbtype = self[db].dbtype
        return dbtype

databases = DatabaseDict()

def _add_db(x):
    databases[x.db] = x
    return x.db

# XXX Try these
# <option value="structure">Structure</option>
# <option value="taxonomy">Taxonomy</option>
# <option value="books">Books</option>
# <option value="geo">ProbeSet</option>
# <option value="domains">3D Domains</option>
# <option value="UniSts">UniSTS</option>
# <option value="cdd">Domains</option>
# <option value="snp">SNP</option>
# <option value="unigene">UniGene</option>
# <option value="popset">PopSet</option>

databases.PUBMED = _add_db(DatabaseInfo("pubmed", PUBLICATION_TYPE))
databases.PUBMEDCENTRAL = _add_db(DatabaseInfo("pmc", PUBLICATION_TYPE))
databases.OMIM = _add_db(DatabaseInfo("omim", PUBLICATION_TYPE))
databases.JOURNALS = _add_db(DatabaseInfo("journals", PUBLICATION_TYPE))
                
databases.GENOME = _add_db(DatabaseInfo("genome", SEQUENCE_TYPE))
databases.NUCLEOTIDE = _add_db(DatabaseInfo("nucleotide", SEQUENCE_TYPE))
databases.PROTEIN = _add_db(DatabaseInfo("protein", SEQUENCE_TYPE))
databases.POPSET = _add_db(DatabaseInfo("popset", SEQUENCE_TYPE))
databases.SEQUENCES = _add_db(DatabaseInfo("sequences", SEQUENCE_TYPE))
databases.GEODATASET = _add_db(DatabaseInfo("gds", SEQUENCE_TYPE))


# Someday I want to make it easier to get a given format.  I would
# rather not have to specify the retmode/rettype pair, but I don't
# know what people want from this feature, so skip for now.  Plus,
# it's harder than I thought.

##class FormatInfo:
##    def __init__(self, name, retmode):
##        self.name = name
##        self.retmode = retmode
##        self.rettype = rettype
