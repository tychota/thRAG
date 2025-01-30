from typing import List, Optional

from pydantic import BaseModel, Field


class Section(BaseModel):
    title: str = Field(..., description="Title of this section")
    content: str = Field(..., description="Full text content of the section")


class Chunk(BaseModel):
    content: str = Field(..., description="Snippet or chunk of text")
    section_index: int = Field(..., description="Index referencing which section this chunk belongs to")


class VLMConfig(BaseModel):
    provider: str = Field(..., description="Name of the provider, e.g. 'vlm_1', 'human'")
    model: Optional[str] = Field(None, description="If relevant, name of the model")


class IngestionConfig(BaseModel):
    fallback_plan: List[VLMConfig] = Field(
        default_factory=list, description="List of fallback providers, e.g. [vlm1, vlm2, human]"
    )
    metadata: Optional[str] = Field(None, description="Optional metadata string (no kb_id/doc_id needed)")

    # you might store chunk_size, DPI, etc. in here
    dpi: int = 200
    chunk_size: int = 800
