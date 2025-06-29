# api/validators.py
from marshmallow import Schema, fields, validate, ValidationError

class AnalyticsEventSchema(Schema):
    """
    Schema for validating analytics event data.
    """
    event_type = fields.Str(required=True, validate=validate.Length(min=1))
    user_id = fields.UUID(required=True)
    session_id = fields.UUID(required=True)
    timestamp = fields.DateTime(required=True)
    properties = fields.Dict(keys=fields.Str(), values=fields.Raw(), required=True)

    class Meta:
        ordered = True

def validate_analytics_data(data):
    """
    Validate analytics data against the AnalyticsEventSchema.
    """
    schema = AnalyticsEventSchema()
    errors = schema.validate(data)
    if errors:
        raise ValidationError(errors)
    return data

# Example usage:
# try:
#     validated_data = validate_analytics_data(event_data)
# except ValidationError as e:
#     # Handle validation error
#     print(e.messages)