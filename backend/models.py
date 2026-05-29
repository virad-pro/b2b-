from pydantic import BaseModel


class LinkedInRequest(BaseModel):
    linkedin_url: str