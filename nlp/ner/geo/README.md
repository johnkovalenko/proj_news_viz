## Have a try at getting geo entities for future dictionary.

#### results so far:  
- extracted normal forms of russian cities, 
  geo objects and some regions.  
  
#### TO-DO:  
- try Petrovich (or similar) lib to conjugate
  already extracted normal forms.  
- scrapy http://geoportalwiki.wikidot.com/ and examine results.  
- merge https://github.com/mfursov/russian-cities/blob/master/database/cities_inflection.csv
  with relevant file of already extracted entities.  
  
cities_rf.csv - cities of Russian Federation.  
countries.csv - countries, global.  
geo.csv - mixed data with names of locations (villages, cities, objects, regions)
regions_rf.csv - a little bit of regions of Russian Federation.

Lines per file:
- 183554    cities_rf.csv
-    280    countries.csv
- 180136    geo.csv
-     57    regions_rf.csv
