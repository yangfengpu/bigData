from django.db import models

class TripleContext(models.Model):
    name          = models.CharField(max_length= 100)
    def __str__(self): 
        return self.name

class KeyVal(models.Model):
    container     = models.ForeignKey(TripleContext, db_index=True)
    key           = models.CharField(max_length=240, db_index=True)
    valueDescr    = models.CharField(max_length=240, db_index=True)

class Tag(models.Model):
    tag           = models.CharField(max_length=200, unique=True)
    description   = models.TextField()
    def __str__(self): 
        return self.tag


class LiteralType(models.Model):
    lType         = models.CharField(max_length=200, unique=True)
    description   = models.TextField()
    def __str__(self): 
        return self.lType

class EducocoNode(models.Model): # This is the vocabulary
    description   = models.TextField()
    showName      = models.CharField(max_length = 100)
    nodeType      = models.CharField(max_length = 100) # Literal or URIRef
    literalType   = models.ForeignKey(LiteralType)
    uriDomain     = models.CharField(max_length=300)
    uriIdentifier = models.CharField(max_length=500,  unique=True) #full_name
    tag           = models.ManyToManyField(Tag, related_name='vocabulary_tag', db_index=True)
    def __str__(self): 
        return self.uriIdentifier


class EducocoTriplePattern(models.Model):
    name          = models.CharField(max_length = 100)
    description   = models.TextField()
    subject       = models.ForeignKey(EducocoNode, related_name='triple_subject', db_index=True)
    predicate     = models.ForeignKey(EducocoNode, related_name='triple_predicate', db_index=True)
    subject       = models.ForeignKey(EducocoNode, related_name='triple_object', db_index=True)
    context       = models.ForeignKey(TripleContext, related_name='triple_context')
    def __str__(self): 
        return self.name
