from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from src.utils.utils import get_field_type, find_matching_template
from src.utils.validators import validate_form


app = FastAPI()


@app.post('/get_form')
async def get_form(form_data: dict):
    if not validate_form(form_data):
        return JSONResponse(
            content={"detail": "All fields must be of string type"},
            status_code=status.HTTP_400_BAD_REQUEST
        )

    validated_data = {field: get_field_type(value) for field, value in form_data.items()}
    matching_template = await find_matching_template(validated_data)

    if matching_template:
        return JSONResponse(
            content={"template_name": matching_template},
            status_code=status.HTTP_200_OK
        )
    else:
        return JSONResponse(content=validated_data, status_code=status.HTTP_200_OK)
