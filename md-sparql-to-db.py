# records from rdf to pycsw

# a SPARQL query to fetch all (updated?) metadata records in the triple store

# Transform to pycsw schema and insert in database

# optional, store the hash of the record as a column, and check before insert if hash already exists
# id the same, hash the same -> skip
# id the same, hash different -> overwrite
# id-source not available -> create
# id-target not available -> remove

# --pycsw data model
# identifier text,
# typename text,
# schema text,
# mdsource text,
# insert_date text,
# xml character varying,
# anytext text,
# metadata character varying,
# metadata_type text,
# language text,
# type text,
# title text,
# title_alternate text,
# abstract text,
# edition text,
# keywords text,
# keywordstype text,
# themes text,
# parentidentifier text,
# relation text,
# time_begin text,
# time_end text,
# topicategory text,
# resourcelanguage text,
# creator text,
# publisher text,
# contributor text,
# organization text,
# securityconstraints text,
# accessconstraints text,
# otherconstraints text,
# date text,
# date_revision text,
# date_creation text,
# date_publication text,
# date_modified text,
# format text,
# source text,
# crs text,
# geodescode text,
# denominator text,
# distancevalue text,
# distanceuom text,
# wkt_geometry text,
# servicetype text,
# servicetypeversion text,
# operation text,
# couplingtype text,
# operateson text,
# operatesonidentifier text,
# operatesoname text,
# degree text,
# classification text,
# conditionapplyingtoaccessanduse text,
# lineage text,
# responsiblepartyrole text,
# specificationtitle text,
# specificationdate text,
# specificationdatetype text,
# platform text,
# instrument text,
# sensortype text,
# cloudcover text,
# bands text,
# links text,
# contacts text,
# anytext_tsvector tsvector,
# wkb_geometry geometry(Geometry,4326)


