# EPIC - Semantic Models

### How to Get Started

Please refer to <https://docs.google.com/document/d/1_lV20-x_HxgRMlQRRjJrVF86w7g6BUqTT-VmE8jfoqM>

### Project Structure

### import 
contains all External Ontology Schemata which are imported by and integrated with EPIC schema. 
- import/OpenADR : Automatically Converted from XSD Schemas using TBCME's Import Tool.
### schemas 
contains the definitions of the core class and properties of the EPIC Information Model and helper extensions as well as integrations with the External Ontologies : BRICK, QUDT and SSN.
### sparqlmotion 
contains all scripts which define web service endpoints and enable the interaction with Topbraid’s Triple Store.
 - sparqlmotion/debug :  fully working parts of the production-ready triplestoreOperations.sms.ttl SPARQLMotion script - left to help future developers get accustomed and experiment with the basic flow of the underlying web services.
- sparqlmotion/triplestoreOperations.sms.ttl: Definition of web-services : XMLInsert and SelectByEventID.
### spin  
contains RDF/SPIN files that define SPIN rules and SPINMap functions which are used during and after the mapping procedures
- spin/namespace_functions.spin.ttl: a series of modified “buildURI”s spinmap:TargetFunctions for both mapping directions were constructed to facilitate and expedite the process of mapping.
- spin/postMappingFix.spin.ttl: SPIN Rules that fire after the creation of EPIC Instances mapped from OpenADR.
- spin/postReverseMappingFix.spin.ttl: SPIN Rules that fire after the creation of OpenADR Instances mapped from EPIC.
### spinmap 
contains SPINMap files which define rule-based mappings between EPIC and other Demand-Response Communication Protocols. Currently one OpenADR is supported.
 - mappings/oadr2epic.ttl: SPINMap definition for mapping OpenADR triples to EPIC triples.
 - mappings/epic2oadr.ttl: SPINMap definition for mapping EPIC triples to OpenADR triples.
### vocab 
contains all the instance vocabularies that refer to the EPIC schema.