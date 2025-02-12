from back_hot.src.models.bookings import BookingsOrm
from back_hot.src.repositories.base import BaseRepository
from back_hot.src.schemas.bookings import Bookings


class BookingsRepository(BaseRepository):
    model = BookingsOrm
    schema = Bookings
