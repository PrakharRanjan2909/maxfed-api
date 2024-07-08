
from typing import List
from pydantic import BaseModel

# Data models for the first type of JSON data
class Cost(BaseModel):
    costs: List[float]

class Account(BaseModel):
    account: str
    friendlyName: str
    cost: float
    costs: List[float]

class ChargeCodeData(BaseModel):
    chargeCode: str
    total: str
    accounts: List[Account]

# Data models for the second type of JSON data
class InstanceAccount(BaseModel):
    friendlyName: str
    countOfServices: int
    accountCost: float

class InstanceData(BaseModel):
    instanceCount: int
    instanceName: str
    cost: float
    account: List[InstanceAccount]

class NestedJSON1(BaseModel):
    data: List[ChargeCodeData]

class NestedJSON2(BaseModel):
    data: List[InstanceData]
