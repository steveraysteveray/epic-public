# Web Service API calls

This section defines the web services and associated SPIN functions that can be invoked to interact internally with the Triple Store. All web services were implemented and tested locally using TopBraid Composer Maestro Edition (TBC-ME) version 6.1 from TopQuadrant and on an Amazon AWS instance using TopBraid Live.

## Listing of calls

Five insertion calls that make changes to the triple store:
- insertOadrMessagesDupCheck:XMLInsert
- insertConvertToPriceEvent:XMLInsert2Price
- epic-tariff:CreateDE
- ab:ArchiveBefore
- nmdc:nmDemandCap

Five retrieval calls (no changes made to the triple store):
- st:selectEventWithTag
- pilotBuildings:GetInfo
- sdd:selectDailyData
- sadd:selectAllDailyData
- smd:selectMaxDemand

## Environments

The entire library of supported TBL web services can be executed and tested as a Postman Collection, available for import to Postman using [this link](https://www.getpostman.com/collections/332ccd02b2ab03f6b775). To do this, open Postman, then find "Import From Link" under File/Import. A documentation-companion can be accessed by clicking on the icon ▶ next to TBL Webservices Public, then “View in Web”. 
Using Postman's Environment variables, you can test the collection of requests to a TBL Server running on your local machine or on the cloud instance, just by switching environments (i.e. url variable) via the dropdown menu located near the top right corner of Postman's workspace. A detailed step-by-step guide on how to setup Environments in Postman can be found in Appendix A.

## Local Server

Before testing the collection on your local machine, make sure that TBC-ME is already running. By default, a TBL Server is started and listening to : http://localhost:8083/tbl/sparqlmotion.
In case of errors due to web-service ids not being recognized, you can try refreshing the SPARQLMotion web-services by clicking 'Scripts > Refresh/Display SPARQLMotion functions'. This action will try to register again all web-services and display the results to TBC-ME's Console window.

It is strongly recommended to close any VOCAB*.ttl or VOCAB.tdb files while you are testing the collection as it might lead to TBC-ME crashing/hanging. After a successful INSERT or UPDATE operation, the corresponding VOCAB file will be opened and an asterisk() will be appended next to its filename, indicating that unsaved changes to the files. To ensure stable performance, you should either save or discard the changes, close the file and continue your testing.

## Return Codes

Due to limitations of TBL SPARQLMotion development framework, the implementation of the web-services do not comply with the REST API standards and cannot return “404 Not Found” status codes but only 200 OK. To accommodate for such limitations, an empty response with status code 200 is returned in case a specific resource could not be found. In case of an incomplete or malformed request (missing required arguments), TBL platform returns a 500 Internal Server Error and indicates the reason.

