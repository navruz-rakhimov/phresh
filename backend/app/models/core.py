from pydantic import BaseModel


# Almost every new model we create will inherit from CoreModel
class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here.
    """
    pass


# This class will be used for all resources coming out of the database
class IDModelMixin(BaseModel):
    id: int  # this field is required
