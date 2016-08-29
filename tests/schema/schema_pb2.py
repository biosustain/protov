# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema/schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema/schema.proto',
  package='v',
  syntax='proto3',
  serialized_pb=_b('\n\x13schema/schema.proto\x12\x01v\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x19google/protobuf/any.proto\"\xd5\x02\n\nJSONSchema\x12\x12\n\nmin_length\x18\x01 \x01(\r\x12\x12\n\nmax_length\x18\x02 \x01(\r\x12\x0f\n\x07pattern\x18\x03 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x04 \x01(\t\x12-\n\x07minimum\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12-\n\x07maximum\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x19\n\x11\x65xclusive_minimum\x18\x07 \x01(\x08\x12\x19\n\x11\x65xclusive_maximum\x18\x08 \x01(\x08\x12\x11\n\tmin_items\x18\t \x01(\r\x12\x11\n\tmax_items\x18\n \x01(\r\x12\x14\n\x0cunique_items\x18\x0b \x01(\x08\x12\x16\n\x0emin_properties\x18\x0c \x01(\r\x12\x16\n\x0emax_properties\x18\r \x01(\r\"\x9f\x01\n\x14RequestSchemaOptions\x12-\n\x07\x65xclude\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskH\x00\x12-\n\x07include\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskH\x00\x12\x0f\n\x07require\x18\x03 \x03(\tB\x18\n\x16include_exclude_fieldsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_JSONSCHEMA = _descriptor.Descriptor(
  name='JSONSchema',
  full_name='v.JSONSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_length', full_name='v.JSONSchema.min_length', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_length', full_name='v.JSONSchema.max_length', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pattern', full_name='v.JSONSchema.pattern', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='format', full_name='v.JSONSchema.format', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum', full_name='v.JSONSchema.minimum', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='v.JSONSchema.maximum', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exclusive_minimum', full_name='v.JSONSchema.exclusive_minimum', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exclusive_maximum', full_name='v.JSONSchema.exclusive_maximum', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_items', full_name='v.JSONSchema.min_items', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_items', full_name='v.JSONSchema.max_items', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_items', full_name='v.JSONSchema.unique_items', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_properties', full_name='v.JSONSchema.min_properties', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_properties', full_name='v.JSONSchema.max_properties', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=461,
)


_REQUESTSCHEMAOPTIONS = _descriptor.Descriptor(
  name='RequestSchemaOptions',
  full_name='v.RequestSchemaOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exclude', full_name='v.RequestSchemaOptions.exclude', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include', full_name='v.RequestSchemaOptions.include', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='require', full_name='v.RequestSchemaOptions.require', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='include_exclude_fields', full_name='v.RequestSchemaOptions.include_exclude_fields',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=464,
  serialized_end=623,
)

_JSONSCHEMA.fields_by_name['minimum'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT64VALUE
_JSONSCHEMA.fields_by_name['maximum'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT64VALUE
_REQUESTSCHEMAOPTIONS.fields_by_name['exclude'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_REQUESTSCHEMAOPTIONS.fields_by_name['include'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_REQUESTSCHEMAOPTIONS.oneofs_by_name['include_exclude_fields'].fields.append(
  _REQUESTSCHEMAOPTIONS.fields_by_name['exclude'])
_REQUESTSCHEMAOPTIONS.fields_by_name['exclude'].containing_oneof = _REQUESTSCHEMAOPTIONS.oneofs_by_name['include_exclude_fields']
_REQUESTSCHEMAOPTIONS.oneofs_by_name['include_exclude_fields'].fields.append(
  _REQUESTSCHEMAOPTIONS.fields_by_name['include'])
_REQUESTSCHEMAOPTIONS.fields_by_name['include'].containing_oneof = _REQUESTSCHEMAOPTIONS.oneofs_by_name['include_exclude_fields']
DESCRIPTOR.message_types_by_name['JSONSchema'] = _JSONSCHEMA
DESCRIPTOR.message_types_by_name['RequestSchemaOptions'] = _REQUESTSCHEMAOPTIONS

JSONSchema = _reflection.GeneratedProtocolMessageType('JSONSchema', (_message.Message,), dict(
  DESCRIPTOR = _JSONSCHEMA,
  __module__ = 'schema.schema_pb2'
  # @@protoc_insertion_point(class_scope:v.JSONSchema)
  ))
_sym_db.RegisterMessage(JSONSchema)

RequestSchemaOptions = _reflection.GeneratedProtocolMessageType('RequestSchemaOptions', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSCHEMAOPTIONS,
  __module__ = 'schema.schema_pb2'
  # @@protoc_insertion_point(class_scope:v.RequestSchemaOptions)
  ))
_sym_db.RegisterMessage(RequestSchemaOptions)


# @@protoc_insertion_point(module_scope)