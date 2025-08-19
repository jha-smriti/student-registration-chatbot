from marshmallow import Schema, fields

class ChatRequestSchema(Schema):
session_id = fields.Str(required=True)
message = fields.Str(required=True)