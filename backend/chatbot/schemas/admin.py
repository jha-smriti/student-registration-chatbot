
from marshmallow import Schema, fields

class FAQCreateSchema(Schema):
question = fields.Str(required=True)
answer = fields.Str(required=True)
tags = fields.List(fields.Str(), required=False)