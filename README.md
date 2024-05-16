# Triplestore (virtuoso)

Component: Triple Store
Lead: Rob, Anna

A triple store to store the soilwise knowledge graph

The triple store contains:
- the [Soilhealth ontology]()
- the [harvested](https://github.com/soilwise-he/harvesters) metadata records
- results of [link liveness assessment]() and [metadata validation]()

The triple store is used by the dashboard to query metadata records. The current [pycsw](https://github.com/soilwise-he/pycsw) instance requires a relational backend, a script will dump the metadata from the triple store into the [postgres database](https://github.com/soilwise-he/PostGreSQL) at intervals.


