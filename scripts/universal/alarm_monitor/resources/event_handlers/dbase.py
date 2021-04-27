# -*- coding: utf-8 -*-

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


from sqlalchemy import Column, String, LargeBinary, BigInteger, BINARY, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import host

logger.debug("dbase module is uploaded")

engine = host.get_database_connection()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class PersonImage(Base):
    __tablename__ = "persons_images_t"
    person_guid = Column(String(8))
    image_guid = Column(String(8), primary_key=True, nullable=False, unique=True)
    image = Column(BINARY)
    thumbnail = Column(BINARY)
    remote_server_guid = Column(String(8))
    modification_id = Column(BIGINT)
    deleted_ts = Column(BIGINT)

    @classmethod
    def get(cls):
        return session.query(cls)

    @classmethod
    def get_image(cls, person_guid):
        """

        Args:
            person_guid (str):

        Returns:
            (list | None): returns list of bytes

        """
        # img = cls.get().filter(cls.person_guid == person_guid)

        # if img is not None:
        #     images = [i.image for i in img]
        #     return images


Base.metadata.create_all(engine)


def person_image(person_guid):
    """
    Args:
        person_guid (str):

    Returns: (list): список из фото персоны из базы в байтах, фото м.б. несколько

    """
    logger.debug("searching images for person guid: %s", person_guid)
    res = PersonImage.get_image(person_guid)
    if res:
        return res

