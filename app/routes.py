# app/routes.py
import json
from fastapi import APIRouter, HTTPException
from .models import NestedJSON1, NestedJSON2
from .transforms import transform_charge_code_data, transform_instance_data
from pathlib import Path

router = APIRouter()

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

@router.post("/transform/chargecodes")
async def transform_chargecodes():
    try:
        with open(DATA_DIR / 'chargecodes.json', 'r') as f:
            data = json.load(f)
        transformed_data = transform_charge_code_data(data)
        return {"transformed_data": transformed_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/transform/instances")
async def transform_instances():
    try:
        with open(DATA_DIR / 'instances.json', 'r') as f:
            data = json.load(f)
        transformed_data = transform_instance_data(data)
        return {"transformed_data": transformed_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#from elasticsearch

# # app/routes.py
# from fastapi import APIRouter, HTTPException
# from elasticsearch import Elasticsearch
# from .models import NestedJSON1, NestedJSON2
# from .transforms import transform_charge_code_data, transform_instance_data

# router = APIRouter()

# es = Elasticsearch(["http://localhost:9200"])

# @router.post("/transform/chargecodes")
# async def transform_chargecodes():
#     try:
#         result = es.search(index="your_index_name_1", body={"query": {"match_all": {}}})
#         data = [hit["_source"] for hit in result["hits"]["hits"]]
#         transformed_data = transform_charge_code_data(data)
#         return {"transformed_data": transformed_data}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @router.post("/transform/instances")
# async def transform_instances():
#     try:
#         result = es.search(index="your_index_name_2", body={"query": {"match_all": {}}})
#         data = [hit["_source"] for hit in result["hits"]["hits"]]
#         transformed_data = transform_instance_data(data)
#         return {"transformed_data": transformed_data}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


#for fetching it from file storage


# app/routes.py
# import httpx
# from fastapi import APIRouter, HTTPException
# from .models import NestedJSON1, NestedJSON2
# from .transforms import transform_charge_code_data, transform_instance_data

# router = APIRouter()

# @router.post("/transform/chargecodes")
# async def transform_chargecodes():
#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.get('URL_TO_FETCH_JSON_DATA_1')
#             response.raise_for_status()
#             data = response.json()
#         transformed_data = transform_charge_code_data(data)
#         return {"transformed_data": transformed_data}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @router.post("/transform/instances")
# async def transform_instances():
#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.get('URL_TO_FETCH_JSON_DATA_2')
#             response.raise_for_status()
#             data = response.json()
#         transformed_data = transform_instance_data(data)
#         return {"transformed_data": transformed_data}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))














# # app/routes.py
# from fastapi import APIRouter, HTTPException
# from .models import NestedJSON1, NestedJSON2
# from .transforms import transform_charge_code_data, transform_instance_data

# router = APIRouter()

# @router.post("/transform/chargecodes")
# async def transform_chargecodes(nested_json: NestedJSON1):
#     try:
#         transformed_data = transform_charge_code_data(nested_json.data)
#         return {"transformed_data": transformed_data}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @router.post("/transform/instances")
# async def transform_instances(nested_json: NestedJSON2):
#     try:
#         transformed_data = transform_instance_data(nested_json.data)
#         return {"transformed_data": transformed_data}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


# # app/routes.py
# import json
# from fastapi import APIRouter, HTTPException
# from .models import NestedJSON1, NestedJSON2
# from .transforms import transform_charge_code_data, transform_instance_data

# router = APIRouter()

# @router.post("/transform/chargecodes")
# async def transform_chargecodes():
#     try:
#         with open("data1.json", "r") as file:
#             data = json.load(file)
#         transformed_data = transform_charge_code_data(data)
#         return {"transformed_data": transformed_data}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @router.post("/transform/instances")
# async def transform_instances():
#     try:
#         with open("data2.json", "r") as file:
#             data = json.load(file)
#         transformed_data = transform_instance_data(data)
#         return {"transformed_data": transformed_data}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
