import dagster as dg
from dagster_duckdb import DuckDBResource


class ETL(dg.Model):
    url_path: str
    table: str


def _make_asset(etl: ETL) -> dg.AssetsDefinition:
    @dg.asset(name=etl.table)
    def _table(duckdb: DuckDBResource):
        with duckdb.get_connection() as conn:
            conn.execute(
                f"""
                create or replace table {etl.table} as (
                    select * from read_csv_auto('{etl.url_path}')
                )
                """
            )

    return _table


class Tutorial(dg.Component, dg.Model, dg.Resolvable):
    duckdb_database: str
    etl_steps: list[ETL]

    def build_defs(self, context: dg.ComponentLoadContext) -> dg.Definitions:
        return dg.Definitions(
            assets=[_make_asset(etl) for etl in self.etl_steps],
            resources={"duckdb": DuckDBResource(database=self.duckdb_database)},
        )