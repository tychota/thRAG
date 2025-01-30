# Thrag

A super-performant RAG.
Most of the good ideas are originated from [dsRAG](https://github.com/D-Star-AI/dsRAG), licenced under MIT.

We adapated this internally to change some design decisions, and simplify the code.
Hopefully, you can use this in your project.


## Getting started

### Locally

First let's setup postgres:

1. Install `postgres` and `pgvector`.
   On mac, for example :
  - `brew install postgresql`
  - `brew services start postgresql`
  - `brew install pgvector`
2. Install [golang-migrate/migrate](https://github.com/golang-migrate/migrate): this golang project helps you setup the db. The RAG itself don't use GO at all.
3. Create a new postgres user and db:
  - `createuser thrag -P`
  - `createdb -O thrag thrag`
  - `psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE thrag TO thrag;"`

Then execute the migration


`migrate -database 'postgres://thrag:password@localhost:5432/thrag?sslmode=disable' -path db/migrations up`


### In the cloud

We recomend fly.io to get the project running cheap.

Else GCP or another cloud provider.

## Design

Work in progress.

## Results

Work in progress.
