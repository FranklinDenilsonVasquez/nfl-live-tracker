from psycopg2.extras import execute_values

# Generic bulk inserts
def bulk_insert(cursor, table_name, columns, values, conflict_columns):
    if not values:
        return

    column_str = ", ".join(columns)
    conflict_str = ", ".join(conflict_columns)

    query = f"""
        INSERT INTO {table_name} ({column_str})
        VALUES %s 
        ON CONFLICT({conflict_str}) DO NOTHING
    """

    execute_values(cursor, query, values)