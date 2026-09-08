import typing
import sqlalchemy.util.typing as _satyping

try:
    _satyping.make_union_type = lambda *types: typing.Union[tuple(types)] if len(types) > 1 else types[0]
except Exception:
    pass

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

