from fastapi import FastAPI, Query
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(title="LLM Backend Service")

def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Qq24112004",
        host="localhost",
        port="5432",
        cursor_factory=RealDictCursor
    )

@app.get("/filter_models")
def filter_models(
    name: Optional[str] = Query(None, description="Название модели"),
    description: Optional[str] = Query(None, description="Часть текста описания"),
    minPrice: Optional[int] = Query(None, description="Минимальная цена"),
    maxPrice: Optional[int] = Query(None, description="Максимальная цена"),
    availability: Optional[bool] = Query(None, description="Доступность модели")
):
    query = (
        "SELECT llm.name, llm.description "
        "FROM llm "
        "JOIN tariff ON llm.id = tariff.llm_id "
        "JOIN availability ON llm.id = availability.llm_id "
        "WHERE 1=1"
    )
    params = []

    if name:
        query += " AND llm.name ILIKE %s"
        params.append(f"%{name}%")

    if description:
        query += " AND llm.description ILIKE %s"
        params.append(f"%{description}%")

    if minPrice:
        query += " AND tariff.price >= %s"
        params.append(minPrice)

    if maxPrice:
        query += " AND tariff.price <= %s"
        params.append(maxPrice)

    if availability is not None:
        query += " AND availability.status = %s"
        params.append(availability)

    query += " ORDER BY llm.name ASC;"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            results = cur.fetchall()

    return results


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
