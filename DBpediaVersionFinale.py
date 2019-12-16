# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:32:04 2019

@author: paul
"""
"""
Descriptif du programme:
    
Ce programme permet de créer un fichier au format .txt pouvant être utilsé par le programme ID3
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

SELECT DISTINCT ?name ?birth ?yearB ?yearD ?sexe ?death ?BirthPlace ?description ?person 
WHERE {
      
      ?person dbo:birthPlace ?BirthPlace .
      ?person dbo:birthPlace :France .
      ?person dbo:birthYear ?birth .
      ?person dbo:deathYear ?death .
      ?person foaf:name ?name .

      ?person rdfs:comment ?description .
      FILTER (LANG(?description) = 'fr') .
} 
LIMIT 100


"""       
)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()


T=[]
E=[]

c=0
mon_fichier = open("fichier.txt", "w") # Argh j'ai tout écrasé !
m='né avant 1860 ?'+";"+"mort avant 1930?"+";"+"né en France ?"+";"+"né en Allemagne ?"+";"+"né en espagne ?"+"\n"

for result in results["results"]["bindings"]:
    if c==0 or result["description"]["value"]!=T[c-1][3]:
        T.append([result["name"]["value"],result["birth"]["value"],result["death"]["value"],result["description"]["value"]])
        E.append(result["name"]["value"])
        if int(result["birth"]["value"])<1860 and int(result["death"]["value"])<1930 :
            m=m+"oui"+";"+"oui"+";"+"oui"+";"+"non"+";"+"non"+";"+(result["name"]["value"])+"\n"
        elif int(result["birth"]["value"])<1860 and int(result["death"]["value"])>1930:
            m=m+"oui"+";"+"non"+";"+"oui"+";"+"non"+";"+"non"+";"+(result["name"]["value"])+"\n"
        elif int(result["birth"]["value"])>1860 and int(result["death"]["value"])>1930:
            m=m+"non"+";"+"non"+";"+"oui"+";"+"non"+";"+"non"+";"+(result["name"]["value"])+"\n"
        elif int(result["birth"]["value"])>1860 and int(result["death"]["value"])<1930:
            m=m+"non"+";"+"oui"+";"+"oui"+";"+"non"+";"+"non"+";"+(result["name"]["value"])+"\n"
        
        c=c+1

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

SELECT DISTINCT ?name ?birth ?yearB ?yearD ?sexe ?death ?BirthPlace ?description ?person 
WHERE {
      
      ?person dbo:birthPlace ?BirthPlace .
      ?person dbo:birthPlace :Germany .
      ?person dbo:birthYear ?birth .
      ?person dbo:deathYear ?death .
      ?person foaf:name ?name .

      ?person rdfs:comment ?description .
      FILTER (LANG(?description) = 'fr') .
} 
LIMIT 100


"""       
)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    if c==0 or result["description"]["value"]!=T[c-1][3]:
        T.append([result["name"]["value"],result["birth"]["value"],result["death"]["value"],result["description"]["value"]])
        E.append(result["name"]["value"])
        if int(result["birth"]["value"])<1860 and int(result["death"]["value"])<1930 :
            m=m+"oui"+";"+"oui"+";"+"non"+";"+"oui"+";"+"non"+";"+(result["name"]["value"])+"\n"
        elif int(result["birth"]["value"])<1860 and int(result["death"]["value"])>1930:
            m=m+"oui"+";"+"non"+";"+"non"+";"+"oui"+";"+"non"+";"+(result["name"]["value"])+"\n"
        elif int(result["birth"]["value"])>1860 and int(result["death"]["value"])>1930:
            m=m+"non"+";"+"non"+";"+"non"+";"+"oui"+";"+"non"+";"+(result["name"]["value"])+"\n"
        elif int(result["birth"]["value"])>1860 and int(result["death"]["value"])<1930:
            m=m+"non"+";"+"oui"+";"+"non"+";"+"oui"+";"+"non"+";"+(result["name"]["value"])+"\n"

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

SELECT DISTINCT ?name ?birth ?yearB ?yearD ?sexe ?death ?BirthPlace ?description ?person 
WHERE {
      
      ?person dbo:birthPlace ?BirthPlace .
      ?person dbo:birthPlace :Spain .
      ?person dbo:birthYear ?birth .
      ?person dbo:deathYear ?death .
      ?person foaf:name ?name .

      ?person rdfs:comment ?description .
      FILTER (LANG(?description) = 'fr') .
} 
LIMIT 100


"""       
)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    if c==0 or result["description"]["value"]!=T[c-1][3]:
        T.append([result["name"]["value"],result["birth"]["value"],result["death"]["value"],result["description"]["value"]])
        E.append(result["name"]["value"])
        if int(result["birth"]["value"])<1860 and int(result["death"]["value"])<1930 :
            m=m+"oui"+";"+"oui"+";"+"non"+";"+"non"+";"+"oui"+";"+(result["name"]["value"])+"\n"
        elif int(result["birth"]["value"])<1860 and int(result["death"]["value"])>1930:
            m=m+"oui"+";"+"non"+";"+"non"+";"+"non"+";"+"oui"+";"+(result["name"]["value"])+"\n"
        elif int(result["birth"]["value"])>1860 and int(result["death"]["value"])>1930:
            m=m+"non"+";"+"non"+";"+"non"+";"+"non"+";"+"oui"+";"+(result["name"]["value"])+"\n"
        elif int(result["birth"]["value"])>1860 and int(result["death"]["value"])<1930:
            m=m+"non"+";"+"oui"+";"+"non"+";"+"non"+";"+"oui"+";"+(result["name"]["value"])+"\n"
        
        c=c+1





mon_fichier.write(m)
mon_fichier.close()



