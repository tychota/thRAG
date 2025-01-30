from typing import List, Optional

from pydantic import BaseModel, Field


class Section(BaseModel):
    title: str = Field(..., description="Section title")
    content: str = Field(..., description="Text content of the section")
    page_numbers: Optional[List[int]] = Field(default=None, description="Pages where this section appears")


class Chunk(BaseModel):
    content: str = Field(..., description="Chunk of text")
    section_index: int = Field(..., description="Index referencing which section this chunk belongs to")
