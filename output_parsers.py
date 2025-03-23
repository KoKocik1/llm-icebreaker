from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}


class IceBreakers(BaseModel):
    ice_breakers: List[str] = Field(description="ice breakers")

    def to_dict(self) -> Dict[str, Any]:
        return {"ice_breakers": self.ice_breakers}


class TopicOfInterest(BaseModel):
    topics: List[str] = Field(description="topics of interest")

    def to_dict(self) -> Dict[str, Any]:
        return {"topics": self.topics}


summary_parser = PydanticOutputParser(pydantic_object=Summary)
ice_breaker_parser = PydanticOutputParser(pydantic_object=IceBreakers)
topics_of_interest_parser = PydanticOutputParser(
    pydantic_object=TopicOfInterest)
