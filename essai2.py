# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:32:04 2019

@author: paul
"""
"""
Descriptif du programme:
    
Ce programme permet d'afficher tous les personnages de la base de donnée dbpédia,
avec leurs noms, leur date de naissance, leur date de décès, et une brève description
en français du personnage.

"""

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX : <http://dbpedia.org/resource/>
PREFIX dbpedia2: <http://dbpedia.org/property/>
PREFIX dbpedia: <http://dbpedia.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT DISTINCT ?name ?birth ?death ?BirthPlace ?description ?person 
WHERE {
      ?person a dbo:Person .
      ?person dbo:birthPlace ?BirthPlace .
      ?person dbo:birthDate ?birth .
      ?person dbo:deathDate ?death .
      ?person foaf:name ?name .
      ?person rdfs:comment ?description .
      FILTER (LANG(?description) = 'fr') .
} 
LIMIT 10000
"""       
)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()


T=[]
E=[]

c=0

for result in results["results"]["bindings"]:
    if c==0 or result["description"]["value"]!=T[c-1][3]:
        T.append([result["name"]["value"],result["birth"]["value"],result["death"]["value"],result["description"]["value"]])
        c=c+1

    
    
