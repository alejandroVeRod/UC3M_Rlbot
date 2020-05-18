# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/metadata/game_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...api import player_id_pb2
from ...api.stats import extra_mode_stats_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/metadata/game_metadata.proto',
  package='api.metadata',
  serialized_pb=_b('\n api/metadata/game_metadata.proto\x12\x0c\x61pi.metadata\x1a\x13\x61pi/player_id.proto\x1a api/stats/extra_mode_stats.proto\"7\n\tGameScore\x12\x14\n\x0cteam_0_score\x18\x01 \x01(\x05\x12\x14\n\x0cteam_1_score\x18\x02 \x01(\x05\"u\n\x04Goal\x12\x14\n\x0c\x66rame_number\x18\x01 \x01(\x05\x12 \n\tplayer_id\x18\x02 \x01(\x0b\x32\r.api.PlayerId\x12\x35\n\x0f\x65xtra_mode_info\x18\x03 \x01(\x0b\x32\x1c.api.stats.ExtraModeGoalInfo\"b\n\x04\x44\x65mo\x12\x14\n\x0c\x66rame_number\x18\x01 \x01(\x05\x12\"\n\x0b\x61ttacker_id\x18\x02 \x01(\x0b\x32\r.api.PlayerId\x12 \n\tvictim_id\x18\x03 \x01(\x0b\x32\r.api.PlayerId\"\xbe\x03\n\x0cGameMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03map\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\x03\x12\x0e\n\x06\x66rames\x18\x06 \x01(\x05\x12&\n\x05score\x18\x07 \x01(\x0b\x32\x17.api.metadata.GameScore\x12!\n\x05goals\x18\t \x03(\x0b\x32\x12.api.metadata.Goal\x12!\n\x05\x64\x65mos\x18\n \x03(\x0b\x32\x12.api.metadata.Demo\x12%\n\x0eprimary_player\x18\x0b \x01(\x0b\x32\r.api.PlayerId\x12\x0e\n\x06length\x18\x0c \x01(\x02\x12\x16\n\x0egame_server_id\x18\r \x01(\t\x12\x13\n\x0bserver_name\x18\x0e \x01(\t\x12\x12\n\nmatch_guid\x18\x0f \x01(\t\x12\x11\n\tteam_size\x18\x10 \x01(\x05\x12(\n\x08playlist\x18\x11 \x01(\x0e\x32\x16.api.metadata.Playlist\x12\x1b\n\x13is_invalid_analysis\x18\x12 \x01(\x08\x12\x18\n\x10unknown_playlist\x18\x13 \x01(\x05*\xd5\x03\n\x08Playlist\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0eUNRANKED_DUELS\x10\x01\x12\x14\n\x10UNRANKED_DOUBLES\x10\x02\x12\x15\n\x11UNRANKED_STANDARD\x10\x03\x12\x12\n\x0eUNRANKED_CHAOS\x10\x04\x12\x10\n\x0c\x43USTOM_LOBBY\x10\x06\x12\x17\n\x13OFFLINE_SPLITSCREEN\x10\x08\x12\x10\n\x0cRANKED_DUELS\x10\n\x12\x12\n\x0eRANKED_DOUBLES\x10\x0b\x12\x18\n\x14RANKED_SOLO_STANDARD\x10\x0c\x12\x13\n\x0fRANKED_STANDARD\x10\r\x12\x15\n\x11UNRANKED_SNOW_DAY\x10\x0f\x12\x0f\n\x0bROCKET_LABS\x10\x10\x12\x12\n\x0eUNRANKED_HOOPS\x10\x11\x12\x13\n\x0fUNRANKED_RUMBLE\x10\x12\x12\x0e\n\nTOURNAMENT\x10\x16\x12\x15\n\x11UNRANKED_DROPSHOT\x10\x17\x12\x0f\n\x0b\x41NNIVERSARY\x10\x19\x12\x0f\n\x0bTHIRD_PARTY\x10\x1a\x12\x10\n\x0cRANKED_HOOPS\x10\x1b\x12\x11\n\rRANKED_RUMBLE\x10\x1c\x12\x13\n\x0fRANKED_DROPSHOT\x10\x1d\x12\x13\n\x0fRANKED_SNOW_DAY\x10\x1e')
  ,
  dependencies=[player_id_pb2.DESCRIPTOR,extra_mode_stats_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PLAYLIST = _descriptor.EnumDescriptor(
  name='Playlist',
  full_name='api.metadata.Playlist',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRANKED_DUELS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRANKED_DOUBLES', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRANKED_STANDARD', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRANKED_CHAOS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_LOBBY', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFLINE_SPLITSCREEN', index=6, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKED_DUELS', index=7, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKED_DOUBLES', index=8, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKED_SOLO_STANDARD', index=9, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKED_STANDARD', index=10, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRANKED_SNOW_DAY', index=11, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROCKET_LABS', index=12, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRANKED_HOOPS', index=13, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRANKED_RUMBLE', index=14, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOURNAMENT', index=15, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRANKED_DROPSHOT', index=16, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANNIVERSARY', index=17, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THIRD_PARTY', index=18, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKED_HOOPS', index=19, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKED_RUMBLE', index=20, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKED_DROPSHOT', index=21, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKED_SNOW_DAY', index=22, number=30,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=831,
  serialized_end=1300,
)
_sym_db.RegisterEnumDescriptor(_PLAYLIST)

Playlist = enum_type_wrapper.EnumTypeWrapper(_PLAYLIST)
UNKNOWN = 0
UNRANKED_DUELS = 1
UNRANKED_DOUBLES = 2
UNRANKED_STANDARD = 3
UNRANKED_CHAOS = 4
CUSTOM_LOBBY = 6
OFFLINE_SPLITSCREEN = 8
RANKED_DUELS = 10
RANKED_DOUBLES = 11
RANKED_SOLO_STANDARD = 12
RANKED_STANDARD = 13
UNRANKED_SNOW_DAY = 15
ROCKET_LABS = 16
UNRANKED_HOOPS = 17
UNRANKED_RUMBLE = 18
TOURNAMENT = 22
UNRANKED_DROPSHOT = 23
ANNIVERSARY = 25
THIRD_PARTY = 26
RANKED_HOOPS = 27
RANKED_RUMBLE = 28
RANKED_DROPSHOT = 29
RANKED_SNOW_DAY = 30



_GAMESCORE = _descriptor.Descriptor(
  name='GameScore',
  full_name='api.metadata.GameScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_0_score', full_name='api.metadata.GameScore.team_0_score', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team_1_score', full_name='api.metadata.GameScore.team_1_score', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=160,
)


_GOAL = _descriptor.Descriptor(
  name='Goal',
  full_name='api.metadata.Goal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_number', full_name='api.metadata.Goal.frame_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='api.metadata.Goal.player_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra_mode_info', full_name='api.metadata.Goal.extra_mode_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=279,
)


_DEMO = _descriptor.Descriptor(
  name='Demo',
  full_name='api.metadata.Demo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_number', full_name='api.metadata.Demo.frame_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attacker_id', full_name='api.metadata.Demo.attacker_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='victim_id', full_name='api.metadata.Demo.victim_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=379,
)


_GAMEMETADATA = _descriptor.Descriptor(
  name='GameMetadata',
  full_name='api.metadata.GameMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.metadata.GameMetadata.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.metadata.GameMetadata.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map', full_name='api.metadata.GameMetadata.map', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='api.metadata.GameMetadata.version', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='api.metadata.GameMetadata.time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frames', full_name='api.metadata.GameMetadata.frames', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='api.metadata.GameMetadata.score', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goals', full_name='api.metadata.GameMetadata.goals', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demos', full_name='api.metadata.GameMetadata.demos', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primary_player', full_name='api.metadata.GameMetadata.primary_player', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='api.metadata.GameMetadata.length', index=10,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_server_id', full_name='api.metadata.GameMetadata.game_server_id', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_name', full_name='api.metadata.GameMetadata.server_name', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_guid', full_name='api.metadata.GameMetadata.match_guid', index=13,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team_size', full_name='api.metadata.GameMetadata.team_size', index=14,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playlist', full_name='api.metadata.GameMetadata.playlist', index=15,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_invalid_analysis', full_name='api.metadata.GameMetadata.is_invalid_analysis', index=16,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_playlist', full_name='api.metadata.GameMetadata.unknown_playlist', index=17,
      number=19, type=5, cpp_type=1, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=828,
)

_GOAL.fields_by_name['player_id'].message_type = player_id_pb2._PLAYERID
_GOAL.fields_by_name['extra_mode_info'].message_type = extra_mode_stats_pb2._EXTRAMODEGOALINFO
_DEMO.fields_by_name['attacker_id'].message_type = player_id_pb2._PLAYERID
_DEMO.fields_by_name['victim_id'].message_type = player_id_pb2._PLAYERID
_GAMEMETADATA.fields_by_name['score'].message_type = _GAMESCORE
_GAMEMETADATA.fields_by_name['goals'].message_type = _GOAL
_GAMEMETADATA.fields_by_name['demos'].message_type = _DEMO
_GAMEMETADATA.fields_by_name['primary_player'].message_type = player_id_pb2._PLAYERID
_GAMEMETADATA.fields_by_name['playlist'].enum_type = _PLAYLIST
DESCRIPTOR.message_types_by_name['GameScore'] = _GAMESCORE
DESCRIPTOR.message_types_by_name['Goal'] = _GOAL
DESCRIPTOR.message_types_by_name['Demo'] = _DEMO
DESCRIPTOR.message_types_by_name['GameMetadata'] = _GAMEMETADATA
DESCRIPTOR.enum_types_by_name['Playlist'] = _PLAYLIST

GameScore = _reflection.GeneratedProtocolMessageType('GameScore', (_message.Message,), dict(
  DESCRIPTOR = _GAMESCORE,
  __module__ = 'api.metadata.game_metadata_pb2'
  # @@protoc_insertion_point(class_scope:api.metadata.GameScore)
  ))
_sym_db.RegisterMessage(GameScore)

Goal = _reflection.GeneratedProtocolMessageType('Goal', (_message.Message,), dict(
  DESCRIPTOR = _GOAL,
  __module__ = 'api.metadata.game_metadata_pb2'
  # @@protoc_insertion_point(class_scope:api.metadata.Goal)
  ))
_sym_db.RegisterMessage(Goal)

Demo = _reflection.GeneratedProtocolMessageType('Demo', (_message.Message,), dict(
  DESCRIPTOR = _DEMO,
  __module__ = 'api.metadata.game_metadata_pb2'
  # @@protoc_insertion_point(class_scope:api.metadata.Demo)
  ))
_sym_db.RegisterMessage(Demo)

GameMetadata = _reflection.GeneratedProtocolMessageType('GameMetadata', (_message.Message,), dict(
  DESCRIPTOR = _GAMEMETADATA,
  __module__ = 'api.metadata.game_metadata_pb2'
  # @@protoc_insertion_point(class_scope:api.metadata.GameMetadata)
  ))
_sym_db.RegisterMessage(GameMetadata)


# @@protoc_insertion_point(module_scope)
