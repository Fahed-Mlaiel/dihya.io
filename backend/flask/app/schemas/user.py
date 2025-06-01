"""
Schéma de validation pour les utilisateurs Dihya Coding.
Utilise Marshmallow pour sérialisation, validation et sécurité des données utilisateur.
"""

from marshmallow import Schema, fields, validate, validates, ValidationError

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=32),
        error_messages={"required": "Le nom d'utilisateur est requis."}
    )
    email = fields.Email(
        required=True,
        validate=validate.Length(max=128),
        error_messages={"required": "L'email est requis."}
    )
    password = fields.Str(
        load_only=True,
        required=True,
        validate=validate.Length(min=6, max=128),
        error_messages={"required": "Le mot de passe est requis."}
    )
    role = fields.Str(
        dump_only=True,
        default="user"
    )
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @validates("username")
    def validate_username(self, value):
        if " " in value:
            raise ValidationError("Le nom d'utilisateur ne doit pas contenir d'espaces.")

class UserUpdateSchema(Schema):
    username = fields.Str(validate=validate.Length(min=3, max=32))
    email = fields.Email(validate=validate.Length(max=128))
    password = fields.Str(load_only=True, validate=validate.Length(min=6, max=128))

class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)

class UserRegisterSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=32))
    email = fields.Email(required=True, validate=validate.Length(max=128))
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6, max=128))